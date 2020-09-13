# standard library

# django
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

# rest framework
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

# models
from .models import (
    Notification,
    User
)

# serializers
from .serializers import NotificationSerializer

# utils
from .token_auth import account_activation_token
from .utils import getUser

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


@api_view(['POST'])
def authenticate_password(request, format=None):
    email = request.data.get('email')
    password = request.data.get('password')
    empty_respose = {
        "token": "",
        "first_name": "",
        "last_name": "",
        "email": "",
        "thumbnail": "",
    }
    try:
        user = User.objects.get(email=email, is_active=True)
        if check_password(password, user.password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "thumbnail": user.thumbnail,
            })
        else:
            return Response(empty_respose)
    except Exception:
        return Response(empty_respose)


@api_view(['POST'])
def register(request, format=None):
    email = request.data.get('email').strip()
    first_name = request.data.get('first_name').strip()
    last_name = request.data.get('last_name').strip()
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')

    if not password1 or not password2 or not email or \
            not first_name or not last_name:
        return Response({
            "message": "Faltan campos obligatorios!"
        }, status=403)

    if password1 != password2:
        return Response({
            "message": "Las contraseñas no coinciden"
        }, status=403)

    if User.objects.filter(email=email).exists():
        return Response({
            "message": "Ya existe un correo asociado a esta cuenta"
        }, status=403)

    try:
        validate_password(password1)
    except Exception:
        return Response({"message": "Contraseña poco segura!"}, status=403)

    try:
        # create user
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password1),
            is_active=False,
        )
        # send activation email
        current_site = get_current_site(request)
        mail_subject = 'Activata tu cuenta de Comunidad Redpie.'
        message = render_to_string('registration_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            mail_subject, message, to=[user.email]
        )
        email.send()
        return Response({
            "message": (
                'Te hemos enviado un correo para que confirmes tu cuenta.'
            )
        })
    except Exception:
        return Response({
            "message": "Tu cuenta ya existe, debes activarla"
        }, status=403)


@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        return redirect('index')
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
    return redirect('index')


@api_view(['POST'])
def get_my_notifications(request, format=None):
    user = getUser(request)

    notifications = Notification.objects.filter(
        user=user, is_active=True).order_by('-created_at')

    serializer = NotificationSerializer(notifications, many=True)
    return Response({"notifications": serializer.data})
