from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home')
    # path('about/',views.about,name = 'about'),
    # path('contact/',views.contact,name= 'contact'),
    # path('details/',views.details,name = 'details'),
    # path('thank/',views.thanks, name = 'thanks'),
    # path('result/',views.result,name = 'result')
]