# -*- coding: utf-8 -*-
""" Models for the users application.

All apps should use the users.User model for all users
"""
# django
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# managers
from ..managers import UserManager

# models
from . import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    User model with admin-compliant permissions.

    Email is required. Other fields are optional.
    """
    # required fields
    email = models.EmailField(
        _('email address'),
        unique=True,
        db_index=True,
    )
    rut = models.CharField(
        _('rut'),
        db_index=True,
        max_length=20,
    )
    # optional fields
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True, null=True, default="",
    )
    middle_name = models.CharField(
        _('middle name'),
        max_length=100,
        blank=True, null=True, default="",
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        blank=True, null=True, default="",
    )
    mothers_family_name = models.CharField(
        _('mothers family name'),
        max_length=50,
        blank=True, null=True, default="",
    )
    thumbnail = models.CharField(
        _('thumbnail'),
        max_length=1000,
        default="/static/default_user.png",
    )
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'),
    )
    # auto fields
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now,
        help_text=_("The date this user was created in the database"),
    )
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    # public methods
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    # overwritten methods
    def save(self, *args, **kwargs):
        """ store all emails in lowercase """
        self.email = self.email.lower()

        super(User, self).save(*args, **kwargs)
