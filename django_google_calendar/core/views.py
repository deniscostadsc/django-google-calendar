import os

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from core.models import CredentialsModel

CLIENT_SECRETS = os.path.join(
    os.path.dirname(__file__), 
    '..',
    'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/plus.me',
    redirect_uri='http://localhost:8000/oauth2callback')


class Index(View):
    def get(self, request):
        storage = Storage(CredentialsModel, 'id', request.user, 'credential')
        credential = storage.get()
        if credential is None or credential.invalid is True:
            FLOW.params['state'] = xsrfutil.generate_token(
                settings.SECRET_KEY,
                request.user)
            authorize_url = FLOW.step1_get_authorize_url()
            return HttpResponseRedirect(authorize_url)
        else:
            http = httplib2.Http()
            http = credential.authorize(http)
            service = build('plus', 'v1', http=http)
            activities = service.activities()
            activitylist = activities.list(
                collection='public',
                userId='me').execute()
            logging.info(activitylist)
            return render(request, 'core/events.html')


class AuthHandler(View):
    def get(self, request):
        if not xsrfutil.validate_token(
                settings.SECRET_KEY,
                request.REQUEST['state'],
                request.user):
            return  HttpResponseBadRequest()
        credential = FLOW.step2_exchange(request.REQUEST)
        storage = Storage(CredentialsModel, 'id', request.user, 'credential')
        storage.put(credential)
        return HttpResponseRedirect("/")