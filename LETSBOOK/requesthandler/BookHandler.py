from LETSBOOK.models import Book
from LETSBOOK.models import Account
from LETSBOOK.models import Course
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import json

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_ADD_OR_MODIFY_RECORD_SUCCESS   = 201
_ADD_OR_MODIFY_RECORD_FAIL      = 202

# Description d'un livre
_BOOK_ID             = "id"          # Identificateur de livre
_BOOK_USER           = "owner"       # Identificateur de l'utilisateur possedant le livre
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
_BOOK_KEYWORD        = "keyword"     # KEYWORD (Recherche rapide)

# Ajout ou modification d'un livre
def putBook(request):

    book = None

    # Modification
    if _BOOK_ID in request.GET:
        book = Book.objects.get(pk=request.GET[_BOOK_ID])

    # Ajout
    if book is None and _BOOK_TITLE in request.GET:
        book = Book(title=_BOOK_TITLE)
    else:
        book.title          = request.GET[_BOOK_TITLE]

    # Pas de moyen de construction
    if _BOOK_ID not in request.GET and _BOOK_TITLE not in request.GET:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    if _BOOK_AUTHOR in request.GET:
        book.author         = request.GET[_BOOK_AUTHOR]

    if _BOOK_EDITION in request.GET:
        book.edition        = request.GET[_BOOK_EDITION]

    if _BOOK_SIGLE in request.GET:
        book.sigle          = Course.objects.get(pk=request.GET[_BOOK_SIGLE])

    if _BOOK_STATE in request.GET:
        book.howIsBook      = request.GET[_BOOK_STATE]

    if _BOOK_USER in request.GET:
        book.owner          = Account.objects.get(pk=request.GET[_BOOK_USER])

    if _BOOK_INTENT in request.GET:
        book.intent         = request.GET[_BOOK_INTENT]

    if _BOOK_PRICE in request.GET:
        book.price          = request.GET[_BOOK_PRICE]

    if _BOOK_ISBN in request.GET:
        book.ISBN           = request.GET[_BOOK_ISBN]

    if _BOOK_DESC in request.GET:
        book.description    = request.GET[_BOOK_DESC]

    book.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

# Recherche d'un livre
def getBook(request):

    params  = Q()

    # Recherche avec clef primaire
    if _BOOK_ID in request.GET:
        results = Book.objects.get(pk=request.GET[_BOOK_ID])
        return HttpResponse(results.getJson(), content_type='application/response')

    # Recherche avec keyword (Recherche rapide)
    if _BOOK_KEYWORD in request.GET:
        params = params | Q(title__icontains        =   str(request.GET[_BOOK_KEYWORD]))
        params = params | Q(description__icontains  =   str(request.GET[_BOOK_KEYWORD]))

        response = {}
        results  = Book.objects.filter(params)

        for index in range(0, results.count()):
            response[index] = results[index].getStr()

        return HttpResponse(json.dumps(response), content_type='application/response')

    # Recherche avec critere precis
    if _BOOK_TITLE in request.GET:
        params = params & Q(title__icontains        = str(request.GET[_BOOK_TITLE]))

    if _BOOK_AUTHOR in request.GET:
        params = params & Q(author__icontains       = str(request.GET[_BOOK_AUTHOR]))

    if _BOOK_EDITION in request.GET:
        params = params & Q(edition__icontains      = str(request.GET[_BOOK_EDITION]))

    if _BOOK_DESC in request.GET:
        params = params & Q(description__icontains  = str(request.GET[_BOOK_DESC]))

    if _BOOK_ISBN in request.GET:
        params = params & Q(ISBN__icontains         = str(request.GET[_BOOK_ISBN]))

    if _BOOK_INTENT in request.GET:
        params = params & Q(intent__icontains       = str(request.GET[_BOOK_INTENT]))

    if _BOOK_PRICE in request.GET:
        params = params & Q(price__lte              = str(request.GET[_BOOK_PRICE]))

    if _BOOK_STATE in request.GET:
        params = params & Q(howIsBook__icontains    = str(request.GET[_BOOK_STATE]))

    if _BOOK_USER in request.GET:
        params = params & Q(owner                   = Account.objects.get(pk=str(request.GET[_BOOK_USER])))

    if _BOOK_SIGLE in request.GET:
        params = params & Q(sigle                   = Course.objects.get(pk=str(request.GET[_BOOK_SIGLE])))

    response = {}
    results = Book.objects.filter(params)

    for index in range(0, results.count()):
        response[index] = results[index].getStr()

    return HttpResponse(json.dumps(response), content_type='application/response')

# Suppression d'un livre
def deleteBook(request):

    if _BOOK_ID in request.GET:
        results = Book.objects.get(pk=str(request.GET[_BOOK_ID]))
        results.delete()
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)