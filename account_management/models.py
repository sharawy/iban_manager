from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.generic.models import IBANField
from model_utils import Choices


class CustomUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):  # to use email instead of username
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class BaseUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        }, default=''
    )  # no need to be required

    # required fields
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)

    # using email for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()


class Admin(BaseUser):
    class Meta:
        verbose_name = _('admin')
        verbose_name_plural = _('admins')
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = True
        return super().save(*args, **kwargs)


class User(BaseUser):
    created_by = models.ForeignKey(Admin, related_name='creator', on_delete=models.CASCADE)


class BankAccount(models.Model):
    STATUSES = Choices(
        (1, 'active', _('Active')), (2, 'suspended', _('Suspended')), )
    iban = IBANField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    status = models.IntegerField(choices=STATUSES, default=STATUSES.active)
