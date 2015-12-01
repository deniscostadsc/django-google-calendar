from django.contrib import admin

from core.models import FlowModel, CredentialsModel

admin.register([
    FlowModel,
    CredentialsModel
])
