from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import tasklist, taskdetail, taskcreate, taskupdate, taskdelete, RegisterPage

urlpatterns = [
    path('', tasklist.as_view(), name='task_list'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task_detail'),
    path('task/create/', taskcreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', taskupdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', taskdelete.as_view(), name='task_delete'),
    path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),  
]
