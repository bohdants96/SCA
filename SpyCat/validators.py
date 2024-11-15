from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import requests


def validate_int(value):
    if value < 0:
        raise ValidationError(
            _("%(value)s must have a positive value"),
            params={"value": value},
        )


def validate_breed(value):
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(f"{url}")
    cats_data = response.json()
    correct = False
    for cat in cats_data:
        if cat['name'] == value:
            correct = True
            break
    if not correct:
        raise ValidationError(
            _("%(value)s is not a breed"),
            params={"value": value},
        )