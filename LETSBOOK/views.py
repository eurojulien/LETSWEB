from BaseHTTPServer import BaseHTTPRequestHandler
from django.shortcuts import render
from models import Book
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, get_list_or_404
import json

# Description d'un livre
_USER           = "student"     # Identificateur de l'utilisateur possedant le livre
_TITLE          = "title"       # Titre du livre
_AUTHOR         = "author"      # Auteur du livre
_EDITION        = "edition"     # Edition du livre
_SIGLE          = "sigle"       # Sigle du cours dans lequel le livre est demande
_STATE          = "state"       # Etat du livre
_DESCRIPTION    = "desc"        # Description du livre
_PRICE          = "price"       # Prix du livre
_ISBN           = "ISBN"        # Code a barre du livre
_INTENT         = "intent"      # Intention de transaction du vendeur du livre
_PICTURE        = "image"       # Image du livre

# Create your views here.
def findBook(request):

    response = {}

    if _ID in request.GET:
        response[_ID] = str(request.GET[_ID])

    if _TITLE in request.GET:
        response[_TITLE] = str(request.GET[_TITLE])

    if _AUTHOR in request.GET:
        response[_AUTHOR] = str(request.GET[_AUTHOR])

    if _EDITION in request.GET:
        response[_EDITION] = str(request.GET[_EDITION])

    if _SIGLE in request.GET:
        response[_SIGLE] = str(request.GET[_SIGLE])

    if _STATE in request.GET:
        response[_STATE] = str(request.GET[_STATE])

    if _DESCRIPTION in request.GET:
        response[_DESCRIPTION] = str(request.GET[_DESCRIPTION])

    response = json.dumps(response)

    return StreamingHttpResponse(response, content_type='application/response')

def addModififyBook(request):

    studentID       = ""
    studentIntent   = ""
    bookTitle       = ""
    bookAuthor      = ""
    bookEdition     = ""
    bookCourse      = ""
    bookState       = ""
    bookDesc        = ""
    bookISBN        = ""
    bookPrice       = ""
    bookImage       = ""

    if _USER in request.GET:
        studentID = request.GET[_USER]

    if _INTENT in request.GET:
        studentIntent = request.GET[_INTENT]

    if _TITLE in request.GET:
        bookTitle = request.GET[_TITLE]

    if _AUTHOR in request.GET:
        bookAuthor = request.GET[_AUTHOR]

    if _EDITION in request.GET:
        bookEdition = request.GET[_EDITION]

    if _SIGLE in request.GET:
        bookCourse = request.GET[_SIGLE]

    if _STATE in request.GET:
        bookState = request.GET[_STATE]

    if _PRICE in request.GET:
        bookPrice = request.GET[_PRICE]

    if _DESCRIPTION in request.GET:
        bookDesc = request.GET[_DESCRIPTION]

    if _ISBN in request.GET:
        bookISBN = request.GET[_ISBN]

    book = Book(owner=studentID,
                sigle=bookCourse,
                title=bookTitle,
                author=bookAuthor,
                edition=bookEdition,
                price=bookPrice,
                howIsBook=bookState,
                description=bookDesc,
                bookISBN=bookISBN)

    book.save()

    return HttpResponse("SUCCESS")