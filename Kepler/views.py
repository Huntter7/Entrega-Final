from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Kepler.models import Posteo, Profile, Mensajes
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'Kepler/about.html')

def index(request):
    context = {
        'posts':Posteo.objects.all()
    }
    return render(request, 'Kepler/index.html', context)

class PostList(ListView):
    model = Posteo

class PostDetail(DetailView):
    model = Posteo

class PostCreate(LoginRequiredMixin,CreateView):
    model = Posteo
    success_url = reverse_lazy('post-list')
    fields = '__all__'

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posteo
    success_url = reverse_lazy('post-list')
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Posteo.objects.filter(owner=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'Kepler/not_found.html')

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posteo
    success_url = reverse_lazy('post-list')

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Posteo.objects.filter(owner=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'Kepler/not_found.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')

class Login(LoginView):
    next_page = reverse_lazy('post-list')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileList(ListView):
    model = Profile

class ProfileDetail(DetailView):
    model = Profile

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy('post-list')
    fields = '__all__'

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Profile
    fields = '__all__'
    success_url = ('profile-detail')

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'Kepler/not_found.html')

class MensajeCreate(CreateView):
    model = Mensajes
    fields = '__all__'
    success_url = reverse_lazy('index')

class MensajeList(LoginRequiredMixin,ListView):
    model = Mensajes
    context_object_name = 'mensaje'

    def get_queryset(self):
        return Mensajes.objects.filter(destinatario=self.request.user.id).all()
    
class MensajeDelte(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Mensajes
    success_url = reverse_lazy('mensaje-list')

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Posteo.objects.filter(destinatario = user_id).exists()
    