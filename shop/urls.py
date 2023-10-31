from django.urls import path, include
from shop.views import index, show

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', show, name='show')
]