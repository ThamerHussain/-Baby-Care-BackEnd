from django.contrib.auth import get_user_model
from ninja import Router

from config import status
from .authotization import create_token_for_user
from .schemas import AccountIn, AuthOut, SigninIn, details
from baby_care.models import Profile

auth_router = Router(tags=['auth'])
User = get_user_model()


@auth_router.post('signup', response={
    201: AuthOut,
    400: details,
})
def signup(request, account_in: AccountIn):
    if account_in.password1 != account_in.password2:
        return status.BAD_REQUEST_400, {'detail': 'Passwords should be the same'}

    try:
        User.objects.get(email=account_in.email)
    except User.DoesNotExist:
        new_user = User.objects.create_user(
            first_name=account_in.first_name,
            last_name=account_in.last_name,
            email=account_in.email,
            password=account_in.password1
        )
        Profile.objects.create(user=new_user, name=new_user.first_name+" "+new_user.last_name, phone_number=" ", city=" ")
        token = create_token_for_user(new_user)

        return status.CREATED_201, {
            'token': token,
            'account': new_user
        }

    return status.BAD_REQUEST_400, {'detail': 'Email is taken'}


@auth_router.post('signin', response={
    200: AuthOut,
    404: details,
    406: details
})
def signin(request, signin_in: SigninIn):
    
    try:
        user = User.objects.get(email=signin_in.email)
    except User.DoesNotExist:
        user = None

    else:
        if user.check_password(signin_in.password):
            token = create_token_for_user(user)

            return {
                'token': token,
                'account': user
            }
        else: return status.NOT_ACCEPTABLE_406, {'detail': 'the password is not true'}

    if not user:
        return status.NOT_FOUND_404, {'detail': 'User is not registered'}