# from django.db.models import FileField
# from django.forms import forms
# from django.template.defaultfilters import filesizeformat
# from django.utils.translation import ugettext_lazy as _

import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')