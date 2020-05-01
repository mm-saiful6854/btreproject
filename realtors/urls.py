from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='realtors'),
    path('<int:realtor>',views.realtor,name='realtor')
]