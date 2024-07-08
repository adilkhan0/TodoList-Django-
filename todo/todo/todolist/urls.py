from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', )
    path('',home,name='home'),
    path('updatetask/<str:pk>/',updatetask,name ='update_task'),
    path('delete/<str:pk>/',deletetask,name='delete')
]
