from django.shortcuts import render
from django.views import generic
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


def book_not_found(req):
    return render(req, 'book_not_found.html')


def profile(req):
    token = Token.objects.get(user=req.user)
    return render(req, 'profile.html', {'token': token, 'user': req.user})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


class IndexView(generic.RedirectView):
    url = '/books/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
