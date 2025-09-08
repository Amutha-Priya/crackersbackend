from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# create router
router = DefaultRouter()

router.register(r'products', ProducttableViewSet) 

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),  
        path('', include(router.urls)),
]
