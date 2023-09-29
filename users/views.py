import random
import uuid
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Генерация нового ключа
        verification_key = str(uuid.uuid4())
        # Сохранение ключа в поле "verification_key" у пользователя
        self.object.verification_key = verification_key
        # Отправка письма с ключом
        subject = 'Подтверждение регистрации'
        message = f'Привет, {self.object.username}! Вот твой ключ для верификации: {verification_key}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [self.object.email])
        self.object.is_verified = False
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verify', args=(self.object.verification_key,))


class VerifyView(View):
    def get(self, request, verification_key):
        user = get_object_or_404(User, verification_key=verification_key)
        if user.verification_key == verification_key:
            user.is_active = True
            user.verification_key = None
            user.save()
            return HttpResponse('Пользователь успешно верифицирован!')
        else:
            return HttpResponse('Неправильный ключ верификации. Попробуйте еще раз.')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:list'))
