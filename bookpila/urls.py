"""bookpila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('books/', include('books.urls', namespace='books')),
    path('api/', include('books.api_urls', namespace='api')),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='api-auth')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile),
    path('logout', views.logout_view),
    path('api/login', views.api_login, name="api_login"),
    path('', views.IndexView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'views.book_not_found'
