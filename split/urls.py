from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homePage.urls')),
    #회원관련 restful_API
    path('member', include('member.urls')),
]