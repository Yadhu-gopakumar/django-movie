

from django.urls import path

from . import views
app_name="movieApp"
urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('movie/<int:movie_id>/edit/',views.edit,name='edit'),
    path('movie/<int:movie_id>/delete/',views.delete,name='delete'),
    path('add/',views.add_movie,name='add_movie')
]
