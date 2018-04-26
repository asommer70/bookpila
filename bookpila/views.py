from django.shortcuts import render
from django.views import generic
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


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


@csrf_exempt
def api_login(request):
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                return JsonResponse({
                    'message': "Thank you for logging in.",
                    'id': user.id,
                    'username': user.username,
                    'token': user.auth_token.key
        		})
            else:
                return JsonResponse({
		            'message': 'Bad username or password.',
                    'id': None,
                    'username': None,
                    'token': None
                })
