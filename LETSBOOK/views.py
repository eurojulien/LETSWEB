from django.shortcuts import render
from models import Livre
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_list_or_404
import json

_ID             = "id"
_TITRE          = "titre"
_AUTEUR         = "auteur"
_EDITION        = "edition"
_SIGLE          = "sigle"
_ETAT           = "etat"
_DESCRIPTION    = "description"

# Create your views here.
def findBook(request):

    response = {}

    if _ID in request.GET:
        response[_ID] = str(request.GET[_ID])

    if _TITRE in request.GET:
        response[_TITRE] = str(request.GET[_TITRE])

    if _AUTEUR in request.GET:
        response[_AUTEUR] = str(request.GET[_AUTEUR])

    if _EDITION in request.GET:
        response[_EDITION] = str(request.GET[_EDITION])

    if _SIGLE in request.GET:
        response[_SIGLE] = str(request.GET[_SIGLE])

    if _ETAT in request.GET:
        response[_ETAT] = str(request.GET[_ETAT])

    if _DESCRIPTION in request.GET:
        response[_DESCRIPTION] = str(request.GET[_DESCRIPTION])

    response = json.dumps(response)

    return StreamingHttpResponse(response, content_type='application/response')