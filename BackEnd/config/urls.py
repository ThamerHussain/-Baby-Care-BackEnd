from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from baby_care.api import baby_router

api = NinjaAPI(
    title='Baby Care App',
    version='0.1',
    description='A BackEnd to offer an APIs to a baby care application',
    csrf=True,
)

api.add_router('/endpoints', baby_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
