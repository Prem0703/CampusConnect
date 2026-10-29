from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('report/new/', views.report_create, name='report_create'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/<int:pk>/claim/', views.claim_item, name='claim_item'),
    path('report/<int:pk>/claim/<int:claim_id>/review/', views.review_claim, name='review_claim'),
    path('report/<int:pk>/returned/', views.mark_returned, name='mark_returned'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='items/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
