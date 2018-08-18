
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
from .models import Tweet
from .forms import AddTweetForm


class BaseView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, "all_tweets.html", {'tweets':tweets})

    def post(self, request):

        form = AddTweetForm(request.POST)


        if form.is_valid():
            try:
                user = request.user
                tweet = Tweet.objects.create(user=user, content=form.cleaned_data['content'])

                tweets = Tweet.objects.all()
                return render(request, "all_tweets.html", {'tweets':tweets})
            except Exception as e:
                return HttpResponse(e)
        return HttpResponse('form not valid')



class AddTweetView(View):
    def get(self, request):
        #user=request.user
        form = AddTweetForm()
        return render(request, "add_tweet.html", {'form': form})

    def post(self, request):

        return render(request, "add_tweet.html", {'form': form})


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