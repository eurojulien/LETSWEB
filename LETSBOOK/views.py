from BaseHTTPServer import BaseHTTPRequestHandler
from django.shortcuts import render
from models import *
from django.http import HttpResponse, StreamingHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django import http
from django.shortcuts import render, get_list_or_404

import json
from LETSBOOK.requesthandler import SchoolHandler
from LETSBOOK.requesthandler import BookHandler

# Description d'un livre
_BOOK_USER           = "student"     # Identificateur de l'utilisateur possedant le livre
_BOOK_TITLE          = "title"       # Titre du livre
_BOOK_AUTHOR         = "author"      # Auteur du livre
_BOOK_EDITION        = "edition"     # Edition du livre
_BOOK_SIGLE          = "sigle"       # Sigle du cours dans lequel le livre est demande
_BOOK_STATE          = "state"       # Etat du livre
_BOOK_DESC           = "desc"        # Description du livre
_BOOK_PRICE          = "price"       # Prix du livre
_BOOK_ISBN           = "ISBN"        # Code a barre du livre
_BOOK_INTENT         = "intent"      # Intention de transaction du vendeur du livre
_BOOK_PICTURE        = "image"       # Image du livre

# Description d'un departement scolaire
_DEPT_NAME          = "name"
_DEPT_DESC          = "desc"
_DEPT_SCHOOL_NAME   = "schoolName"

# Description d'un cours scolaire
_COURSE_SIGLE         = "sigle"
_COURSE_NAME          = "name"
_COURSE_DESC          = "desc"


# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_ADD_OR_MODIFY_RECORD_SUCCESS   = 201
_ADD_OR_MODIFY_RECORD_FAIL      = 202

_REQUEST_PUT    = 'PUT'
_REQUEST_GET    = 'GET'
_REQUEST_DELETE = 'DELETE'

# Create your views here.
def school(request):

    if request.method == _REQUEST_PUT:
        return SchoolHandler.putSchool(request)

    if request.method == _REQUEST_GET:
        return SchoolHandler.getSchool(request)

def addModifyDepartment(request):

    dept    = 0

    if _DEPT_NAME in request.GET:
        dept = Department.objects.get_or_create(name=_DEPT_NAME)
    else:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    if _DEPT_DESC in request.GET:
        dept.description    = request.GET[_DEPT_DESC]

    dept.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

def addModifyCourse(request):

    course = 0

    if _COURSE_SIGLE in request.GET:
        course = Course.objects.get_or_create(sigle=request.GET[_COURSE_SIGLE])
    else:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    if _COURSE_NAME in request.GET:
        course.name = request.GET[_COURSE_NAME]

    if _COURSE_DESC in request.GET:
        course.description = request.GET[_COURSE_DESC]

    course.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

def book(request):

    if request.method == _REQUEST_PUT:
        return BookHandler.putBook(request)

    if request.method == _REQUEST_GET:
        return BookHandler.getBook(request)

    if request.method == _REQUEST_DELETE:
        return BookHandler.deleteBook(request)
