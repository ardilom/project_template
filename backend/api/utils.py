# standard library
from datetime import datetime
from math import log
import pytz
import random
import re
import string

# django
from django import forms

# django rest
from rest_framework.authtoken.models import Token

# external
from localflavor.cl.forms import CLRutField


def random_string(length=6, chars=None, include_spaces=True):
    if chars is None:
        chars = string.ascii_uppercase + string.digits

    if include_spaces:
        chars += ' '

    return ''.join(random.choice(chars) for x in range(length))


# RUT
def clean_rut(rut, with_hyphen=False):
    rut = rut.replace(' ', '').replace('.', '')
    if not with_hyphen:
        rut = rut.replace('-', '')
    return rut


def format_rut(rut):
    if not rut:
        return ''
    if len(rut) < 2:
        return ''

    rut = clean_rut(rut)
    rut = rut[:9]

    verifier = rut[-1]
    code = rut[0:-1][::-1]
    points = (len(code) - 1) // 3
    if points:
        code = re.sub("(.{3})", "\\1.", code, points, re.DOTALL)
    code = code[::-1]

    return '%s-%s' % (code, verifier)


def get_rut_verifier_digit(rut):
    """
    Returns the verifier digit for a given rut without one
    """
    # strip chars
    rut = clean_rut(rut)
    rut = rut[:8]

    if not rut:
        return ''

    # calculate verifier digit
    value = 11 - sum(
        [int(a) * int(b) for a, b in zip(
            str(rut).zfill(8), '32765432'
        )]
    ) % 11
    return {10: 'K', 11: '0'}.get(value, str(value))


class RUTForm(forms.Form):
    rut = CLRutField(
        label='Rut', max_length=75,
    )


def is_valid_rut(rut):
    return RUTForm({'rut': rut}).is_valid()


# token
def getAuth(request):
    raw_token = request.META.get('HTTP_AUTHORIZATION')
    if raw_token and raw_token.startswith('Token '):
        return raw_token[6:]
    else:
        return ''


def getUser(request):
    auth = getAuth(request)
    token = Token.objects.filter(key=auth).first()

    user = None
    if token:
        user = token.user

    return user


def epoch_seconds(date):
    td = date - datetime(1970, 1, 1, tzinfo=pytz.utc)
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


def hot(s, date):
    order = log(max(abs(int(s)), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)


def nonefy(element):
    if not element:
        return None
    return element
