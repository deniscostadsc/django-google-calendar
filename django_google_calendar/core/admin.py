from django.contrib import admin

from .models import FlowModel, CredentialsModel

admin.register([
    FlowModel,
    CredentialsModel
])
