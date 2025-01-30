from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name='hello'),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_create, name='signup'),
    path("users/", views.get_all_users, name='get_all'),
    path("search/<str:email>/", views.get_by_email, name="search_by_email"),
    path("update/<str:email>/", views.update_by_email, name="update_by_email"),
    path("delete/<str:email>/", views.del_by_email, name="del_by_email"),
]
