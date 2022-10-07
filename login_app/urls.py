from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.MySignupView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('user/', views.MyUserView.as_view(), name='user'),
    path('other/', views.MyOtherView.as_view(), name='other'),
    path('portal_1/', views.Portal_1_View.as_view(), name='portal_1'),
    path('portal_2/', views.Portal_2_View.as_view(), name='portal_2'),
    path('portal/', views.Portal_View.as_view(), name='portal'),
    path('login_error/', views.LoginErrorView.as_view(), name='login_error'),
]
