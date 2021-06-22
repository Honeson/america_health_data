from django.urls import path

from .views import index, predict

urlpatterns = [
    path('', index, name='home'),
    path('predict',predict, name='predict' )
]