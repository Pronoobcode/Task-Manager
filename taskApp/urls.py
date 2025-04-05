from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('create/', views.TaskCreate.as_view(), name='task-create'),
    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='task-edit'),
    path('task/<int:pk>/', views.DetailView.as_view(), name='task-detail'),
    path('task-delete/<int:pk>/', views.DeleteView.as_view(), name='task-delete'),
]