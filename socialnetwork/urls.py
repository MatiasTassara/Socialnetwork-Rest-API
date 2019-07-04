from django.urls import path, re_path
from .views import UserView, OneUserView, PostView, OnePostView, MyLoginView, SearchView
app_name = "socialnetwork"

urlpatterns = [
    path('users/', UserView.as_view()),
    re_path(r'users/(?P<user_id>\d+)/$', OneUserView.as_view()),
    path('posts/', PostView.as_view()),
    re_path(r'posts/(?P<user_id>\d+)/$', OnePostView .as_view()),
    path('login/', MyLoginView.as_view()),
    path('search/', SearchView.as_view()),

]