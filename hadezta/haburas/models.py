from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.safestring import mark_safe
import string
import os

# Create your models here.

DIGIT_CHARS = set(string.digits)

def numberthing_validate(value, length):
    if (set(value) - DIGIT_CHARS):
        raise ValidationError(
            _('%(value)s is not a number: it contains non-digit characters'),
            params={'value': value},
        )
    if (len(value) != length):
        raise ValidationError(
            _('Incorrect entry %(value)s: it is not exactly %(length)s digits long'), params={'value': value, 'length':length}
        )

def phonenumber_validate(value):
    numberthing_validate(value, 8)

CHOICES_SEXO = (
    ('m', _('Male')),
    ('f', _('Famale'))
)

CHOICES_CURSUS = (
    (1, 'English Basic'),
    (2, 'Pre-Intermediario'),
    (3, 'Microsoft Word'),
    (4, 'Microsoft Excel'),
    (5, 'Microsoft Power-Point'),
    (6, 'Microsoft Access'),
    (7, 'Microsoft Publisher'),
    (8, 'Linguage Portugues-I'),
    (9, 'Linguage Portugues-II'),
)

class RegistuKursu(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    place = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=8, null=True, blank=True, validators=[phonenumber_validate], unique=True)
    sexo = models.CharField(max_length=1, choices=CHOICES_SEXO)
    cursu = models.IntegerField(choices=CHOICES_CURSUS)
    photo = models.ImageField(null=True, blank=True)

    def url(self):
        return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.photo)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="70" height="70" />'.format(self.url()) )
    image_tag.short_description = 'Image'
