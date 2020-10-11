from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('/<int:pk>', views.member),
    path('/sms-auth/<str:phone>', views.smsAuth)
]




