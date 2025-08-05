from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('findpath/', views.findPath, name='add_user'),
]
