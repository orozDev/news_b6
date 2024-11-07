from django.urls import path

from workspace import views

urlpatterns = [
    path('create_news/', views.create_news, name='create_news'),
    path('update_news/<int:id>/', views.update_news, name='update_news'),
    path('delete_news/<int:id>/', views.delete_news, name='delete_news'),

    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),

    path('', views.main, name='workspace'),
]
