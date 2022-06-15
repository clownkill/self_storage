from django.urls import path, include

from .views import index, boxes, faq, my_rent
from storage_app import views

urlpatterns = [
    path('', index, name='index'),
    path('boxes', boxes, name='boxes'),
    path('faq', faq, name='faq'),
    path('my-rent', my_rent, name='my_rent'),
    path('users/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
