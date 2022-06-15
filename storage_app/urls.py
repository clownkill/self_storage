from django.urls import path, include

from .views import index, boxes, faq, my_rent

urlpatterns = [
    path('', index, name='index'),
    path('boxes', boxes, name='boxes'),
    path('faq', faq, name='faq'),
    path('my-rent', my_rent, name='my-rent'),
    path('users/', include('django.contrib.auth.urls')),
]
