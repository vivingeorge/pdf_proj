from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
from django.contrib.auth.models import User
from .extra_validator import validate_file_extension


def validate_pdf(value):
    if isinstance(value.file, InMemoryUploadedFile) and value.file.content_type != 'application/pdf':
        raise ValidationError('Please upload a valid PDF file')


class Document(models.Model):
    user = models.ForeignKey(User)
    name = models.TextField(blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_pdf])
    imagefile = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.get_full_name()