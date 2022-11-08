from secrets import choice
from ssl import create_default_context
from django.db import models

import uuid


class RegistrationInfo(models.Model):
    STATUS_CHOICE = (
        ("R", "Recieved"),
        ("DDLG", "DDLG"),
        ("P", "Ready for Print"),
        ("D", "Ready for Delivery"),
        ("Dd", "Delivered"),
    )
    TYPE_CHOICE = (
        ("B", "Bengali"),
        ("E", "English"),
        ("BE", "Both"),
    )
    application_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    ward = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    application_online_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    # operator

    def __str__(self):
        return self.name
