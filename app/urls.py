from django.urls import path

from .views import SignUp, home, login, verify_email

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:user_id>/<str:token>', verify_email, name='verify'),
]