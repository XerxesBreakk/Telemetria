from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'records',views.RecordViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('lightStatus/',views.lightStatus,name="lightStatus"),
    path('history/',views.lightHistory,name='lightHistory'),
    path('light/',views.RecordStatusView.as_view(),name='light'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('permissions/',views.PermissionsListView.as_view(),name='permissions'),
    path('user/',views.UserListView.as_view(),name='UserListView'),
    path('create_user/',views.UserCreate.as_view(),name='UserCreateView'),
    path('user_edit/<int:id>/',views.UserUpdate.as_view(),name='UserUpdate'),
    path('delete_user/<int:id>/',views.UserDeleteView.as_view(),name='UserDelete'),
    path('group/',views.GroupListView.as_view(),name='GroupListView'),
    path('create_group/',views.GroupCreate.as_view(),name='GroupCreateView'),
    path('group_edit/<int:id>/',views.GroupUpdate.as_view(),name='GroupUpdate'),
]
