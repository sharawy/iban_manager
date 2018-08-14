from django.contrib.auth import get_user_model
from social_core.exceptions import AuthForbidden


def check_user_exists(backend, details, uid, user=None, *args, **kwargs):
    email = details.get('email', '')
    exists = get_user_model().objects.filter(email=email, is_staff=True).exists()

    if not exists:
        raise AuthForbidden(backend)
