from django.urls import path
from apps.users.views import login, registration

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]
