from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from core.forms import RegisterForm, UpdateProfileForm, CarCreateForm
from core.models import Car, User


class RegistrationForm(View):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, 'registration/signup.html', {'form': form})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = "car_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_create'] = CarCreateForm()
        return data

    def get_queryset(self):
        return self.model.objects.order_by('-id')


class CarCreateView(CreateView):
    fields = ['title', 'brand', 'year', 'mileage', 'gas', 'image']
    model = Car

    def form_valid(self, form):
        car = form.save()
        return render(self.request, 'car.html', {'car': car})


class CarView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Car

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        car = get_object_or_404(Car, pk=self.get_object().pk)
        data['users_list'] = car.user_set.all()
        return data


class OrderCarView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        car = get_object_or_404(Car, pk=pk)
        user.cars.add(car)
        return render(request, 'order_user.html', {'user': user})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        form = UpdateProfileForm(initial=model_to_dict(user, fields=['about_me', 'favorite_author']))
        return render(request, 'update_profile.html', {'user': user, 'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/profile/')


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User


class IndexRedirectView(View):
    def get(self, request):
        return redirect('/login/')


class CarListPageView(ListView):
    model = Car
    template_name = 'page.html'
    context_object_name = "car_list"
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.order_by('-id')