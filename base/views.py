# views.py
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import task
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class tasklist(LoginRequiredMixin, ListView):
    model = task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.model.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search_area')
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)  # Adjusted filter here
            context['search_input'] = search_input
        
        return context
    

        

class taskdetail(LoginRequiredMixin,DetailView):
    model = task    
    context_object_name = 'task_detail'  
    template_name = 'base/task.html'


class taskcreate(LoginRequiredMixin,CreateView):
    model = task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(taskcreate,self).form_valid(form)
    

class taskupdate(LoginRequiredMixin,UpdateView):
    model=task
    fields=['title','description','complete']
    success_url = reverse_lazy('task_list')

class taskdelete(LoginRequiredMixin,DeleteView):
    model = task
    context_object_name = 'tasks'
    template_name = 'base/task_delete.html' 

    def get_success_url(self):
        return reverse_lazy('task_list')
    

class userlogin(LoginView):
    template_name = 'base/login.html'  
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list') 
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

    def form_valid(self, form) :
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(RegisterPage,self).get(*args,**kwargs)
        

    
        