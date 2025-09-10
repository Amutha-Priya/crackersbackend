from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# create router
router = DefaultRouter()

router.register(r'products', ProducttableViewSet) 

urlpatterns = [
     path('product-api/', ProductCreateView.as_view()), 
        path('', include(router.urls)),
]
