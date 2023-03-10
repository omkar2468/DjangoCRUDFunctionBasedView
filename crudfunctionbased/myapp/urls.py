from django.urls import path
from . import views

urlpatterns = [
    path("", views.addshow, name="addandshow"),     

    path("delete/<int:id>", views.deletedata, name="deletedata"), 

    path("updatedata/<int:id>", views.updatedata, name="updatedata"), 
]   
 