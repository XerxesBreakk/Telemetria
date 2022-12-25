from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'records',views.RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lightStatus/',views.lightStatus,name="lightStatus"),
    path('history/',views.lightHistory,name='lightHistory'),
]
