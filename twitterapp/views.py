
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, CreateView

#from .models import
#from .forms import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.views import View


class BaseView(View):
    def get(self, request):
        base = []
        return render(request, "base.html", {'base':base})

    def post(self, request):
        return HttpResponse('post')


class Login(View):
    def get(self, request):
        return HttpResponse
    def post(self, request):
        return HttpResponse

class Logout(View):
    def get(self, request):
        return HttpResponse
    def post(self, request):
        return HttpResponse