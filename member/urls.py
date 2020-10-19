from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_member),
    path('<int:pk>', views.member),
    path('check-nick', views.checkNick),
    path('sms-auth/<str:phone>', views.smsAuth)
]




