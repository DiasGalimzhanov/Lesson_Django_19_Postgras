from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def senf_verification_email(self, user):
        token = default_token_generator.make_token(user)
        link = f"http://localhost:8000/{user.id}/{token}"
        body = f"Activate your account: {link}"
        send_mail(
            subject="Account activation",
            message=body,
            from_email='dias199770@gmail.com',
            recipient_list=[user.email],
            fail_silently=False
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        self.senf_verification_email(self.object)
        return super().form_valid(form)
    
def verify_email(request,user_id, token):
    user = User.objects.get(id=user_id)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(request, 'login.html')