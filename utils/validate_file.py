import os
from django.core.exceptions import ValidationError


def validate_icon(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path & filename
    valid_extensions = ['.png', '.svg']  # populate with the extensions that you allow / want
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please upload SVG or PNG image!')

