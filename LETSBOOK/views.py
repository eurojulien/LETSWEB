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

def addModififyBook(request):

    studentID       = ""
    bookCourse      = ""

    # Si l'usager n'est pas specifie, alors le service retourne une erreur
    if _BOOK_USER in request.GET:
        studentID = Account.objetcs.get_object_or_404(id=studentID)
    else:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    # Si le sigle n'est pas specifie, alors le service retourne une erreur
    if _BOOK_SIGLE in request.GET:
        bookCourse = request.GET[_BOOK_SIGLE]
    else:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    # Recherche ou creation du livre avec les donnees de base
    book = Book.objects.get_or_create(owner=studentID, sigle=bookCourse)

    if _BOOK_INTENT in request.GET:
        book.intent = request.GET[_BOOK_INTENT]

    if _BOOK_TITLE in request.GET:
        book.title = request.GET[_BOOK_TITLE]

    if _BOOK_AUTHOR in request.GET:
        book.author = request.GET[_BOOK_AUTHOR]

    if _BOOK_EDITION in request.GET:
        book.edition = request.GET[_BOOK_EDITION]

    if _BOOK_STATE in request.GET:
        book.howIsBook = request.GET[_BOOK_STATE]

    if _BOOK_PRICE in request.GET:
        book.price = request.GET[_BOOK_PRICE]

    if _BOOK_DESC in request.GET:
        book.description = request.GET[_BOOK_DESC]

    if _BOOK_ISBN in request.GET:
        book.ISBN = request.GET[_BOOK_ISBN]

    # Sauvegarde du livre
    book.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

def findBook(request):

    response = {}

    if _BOOK_TITLE in request.GET:
        response[_BOOK_TITLE] = str(request.GET[_BOOK_TITLE])

    if _BOOK_AUTHOR in request.GET:
        response[_BOOK_AUTHOR] = str(request.GET[_BOOK_AUTHOR])

    if _BOOK_EDITION in request.GET:
        response[_BOOK_EDITION] = str(request.GET[_BOOK_EDITION])

    if _BOOK_SIGLE in request.GET:
        response[_BOOK_SIGLE] = str(request.GET[_BOOK_SIGLE])

    if _BOOK_STATE in request.GET:
        response[_BOOK_STATE] = str(request.GET[_BOOK_STATE])

    if _BOOK_DESC in request.GET:
        response[_BOOK_DESC] = str(request.GET[_BOOK_DESC])

    response = json.dumps(response)

    return StreamingHttpResponse(response, content_type='application/response')