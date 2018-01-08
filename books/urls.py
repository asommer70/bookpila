from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:pk>', views.show, name='show'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/remove_tag', views.remove_tag, name='remove_tag'),
    path('<int:pk>/current_loc', views.current_loc, name='current_loc'),
    path('tags/<int:pk>', views.tag, name='tags'),
    path('search/<str:term>', views.search, name='search'),
]
