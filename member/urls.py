from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('<int:pk>', views.member),
    path('<str:nick>', views.checkNick),
    path('sms-auth/<str:phone>', views.smsAuth)
]




