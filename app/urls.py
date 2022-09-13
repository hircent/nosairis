from django.urls import path
from .views import home,alert,graph

urlpatterns = [
    path("",home,name='home'),
    path("alert",alert,name='alert'),
    path("graph",graph,name='graph')
]