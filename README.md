# Spike sobre a API do Google Calendar

## Passsos para conseguir criar uma aplicação que use a API do Calendar

1. Crie uma aplicação no [Console Google Developer](
    https://console.developers.google.com/
    "Console Google Developer")

2. Preencha o arquivo com o secrets da aplicação.

    {
      "web": {
        "client_id": [ CLIENT_ID ],
        "client_secret": [ CLIENT_SECRET ],
        "redirect_uris": [],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token"
      }
    }

## Items importantes

- [Modelo que salva a credencial do usuário](
    https://github.com/deniscostadsc/django-google-calendar/blob/master/django_google_calendar/core/models.py#L7 
    "Modelo de credencial")
- [View que usa a API do Calendar](
    https://github.com/deniscostadsc/django-google-calendar/blob/master/django_google_calendar/core/views.py#L29
    "View de index")
- [View que autentica](
    https://github.com/deniscostadsc/django-google-calendar/blob/master/django_google_calendar/core/views.py#L56
    "View de autenticação")
