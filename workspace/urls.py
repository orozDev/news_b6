from django.urls import path

from workspace import views

urlpatterns = [
    path('create_news/', views.create_news, name='create_news'),
    path('update_news/<int:id>/', views.update_news, name='update_news'),
    path('delete_news/<int:id>/', views.delete_news, name='delete_news'),
    path('', views.main, name='workspace'),
]
