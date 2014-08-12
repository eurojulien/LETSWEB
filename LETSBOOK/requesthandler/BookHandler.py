from LETSBOOK.models import Book
from LETSBOOK.models import Account
from LETSBOOK.models import Course
from django.http import HttpResponse
from django.db.models import Q
from collections import OrderedDict
from UserHandler import getUser
import json

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_HTTP_SUCCESS                   = 200
_HTTP_ERROR                     = 500
_HTTP_JSON                      = "application/json"
_BOOK_JSON                      = "books"

# Description d'un livre
_BOOK_ID             = "id"          # Identificateur de livre
_BOOK_TITLE          = "title"       # Titre du livre
_BOOK_USER           = "idowner"     # Proprietaire du livre (Clef primaire)
_BOOK_AUTHOR         = "author"      # Auteur du livre
_BOOK_EDITION        = "edition"     # Edition du livre
_BOOK_SIGLE          = "idsigle"     # Sigle du cours dans lequel le livre est demande
_BOOK_STATE          = "state"       # Etat du livre
_BOOK_DESC           = "desc"        # Description du livre
_BOOK_PRICE          = "price"       # Prix du livre
_BOOK_ISBN           = "ISBN"        # Code a barre du livre
_BOOK_INTENT         = "intent"      # Intention de transaction du vendeur du livre
_BOOK_PICTURE        = "image"       # Image du livre
_BOOK_KEYWORD        = "keyword"     # KEYWORD (Recherche rapide)

_USER_EMAIL          = "email"      # email usager

# Ajout ou modification d'un livre
# Reception des parametres en JSON
def putBook(request):

    if request.body == None:
        return HttpResponse(status=_HTTP_ERROR, content="Pas d'information a traiter")

    book = None
    jsonBook = json.loads(request.body)

    # Modification
    if _BOOK_ID in jsonBook:

        try:
            book = Book.objects.get(pk=jsonBook.get(_BOOK_ID))
        except Book.DoesNotExist:
            return HttpResponse(content="Le livre " + jsonBook[_BOOK_ID] + " n'existe pas", status=_HTTP_ERROR)

    # Ajout
    # Verification des elements servant a la creation d'un livre
    else :
        if _BOOK_TITLE      not in jsonBook or \
           _BOOK_AUTHOR     not in jsonBook or \
           _BOOK_EDITION    not in jsonBook or \
           _BOOK_SIGLE      not in jsonBook or \
           _BOOK_STATE      not in jsonBook or \
           _BOOK_USER       not in jsonBook or \
           _BOOK_INTENT     not in jsonBook or \
           _BOOK_PRICE      not in jsonBook :

            return HttpResponse(status=_HTTP_ERROR, content="Parametre(s) manquant(s)")

        else:
            book    = Book(title=jsonBook.get(_BOOK_TITLE))

    if _BOOK_TITLE in jsonBook:
        book.title          = jsonBook.get(_BOOK_TITLE)

    if _BOOK_AUTHOR in jsonBook:
        book.author         = jsonBook.get(_BOOK_AUTHOR)

    if _BOOK_EDITION in jsonBook:
        book.edition        = jsonBook.get(_BOOK_EDITION)

    if _BOOK_SIGLE in jsonBook:
        book.sigle          = Course.objects.get(pk=jsonBook.get(_BOOK_SIGLE))

    if _BOOK_STATE in jsonBook:
        book.howIsBook      = jsonBook.get(_BOOK_STATE)

    if _BOOK_USER in jsonBook:
        book.owner          = Account.objects.get(pk=jsonBook.get(_BOOK_USER))

    if _BOOK_INTENT in jsonBook:
        book.intent         = jsonBook.get(_BOOK_INTENT)

    if _BOOK_PRICE in jsonBook:
        book.price          = jsonBook.get(_BOOK_PRICE)

    if _BOOK_ISBN in jsonBook:
        book.ISBN           = jsonBook.get(_BOOK_ISBN)

    if _BOOK_DESC in jsonBook:
        book.description    = jsonBook.get(_BOOK_DESC)

    try:
        book.save()
    except Exception as e:
        return HttpResponse(content=e.message, status=_HTTP_ERROR)

    return HttpResponse(status=_HTTP_SUCCESS, content=getBookData(book, True),content_type=_HTTP_JSON)

# Recherche d'un livre
def getBook(request):

    # Parametres de recherche
    params  = Q()

    # Recherche avec keyword (Recherche rapide)
    if _BOOK_KEYWORD in request.GET:
        params = params | Q(title__icontains        =   str(request.GET[_BOOK_KEYWORD]))
        params = params | Q(description__icontains  =   str(request.GET[_BOOK_KEYWORD]))

        response = {"books" : []}
        results = Book.objects.filter(params)

        for index in range(0, results.count()):
            response[_BOOK_JSON].append(getBookInfo(results[index], False))

        return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(response), content_type=_HTTP_JSON)

    response = {'books' : []}

    # Recherche d'une liste de livre d'un usager
    if _USER_EMAIL in request.GET and _BOOK_USER in request.GET:

        try:
            account = Account.objects.get(pk=str(request.GET[_BOOK_USER]),
                                          email=str(request.GET[_USER_EMAIL]))
        except Account.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Le compte n'existe pas")

        results = Book.objects.filter(owner=account)

        for index in range(0, results.count()):
            response["books"].append(getBookData(results[index], False))

        return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(response), content_type=_HTTP_JSON)

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

    if _BOOK_SIGLE in request.GET:
        params = params & Q(sigle                   = Course.objects.get(pk=str(request.GET[_BOOK_SIGLE])))

    if len(params) == 0:
        return HttpResponse(status=_HTTP_ERROR, content="Aucun parametre precise")

    try :
        results = Book.objects.filter(params)
    except Exception as e:
        return HttpResponse(status=_HTTP_ERROR, content=e.message)

    for index in range(0, results.count()):
        response["books"].append(getBookInfo(results[index], False))

    return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(response), content_type=_HTTP_JSON)

# Suppression d'un livre
def deleteBook(request):

    if _BOOK_ID in request.GET:

        try:
            results = Book.objects.get(pk=str(request.GET[_BOOK_ID]))
        except Book.DoesNotExist :
            return HttpResponse(content="Le livre " + request.GET[_BOOK_ID] + " n'existe pas", content_type=_HTTP_ERROR)

        results.delete()

        return HttpResponse(status=_HTTP_SUCCESS)

    return HttpResponse(status=_HTTP_ERROR)

# Json pour l'affichage d'un livre seulement
def getBookInfo(book, jsonFormat):

    book = OrderedDict({
                        "title"         : str(book.title.encode('utf8', 'replace')),
                        "author"        : str(book.author.encode('utf8', 'replace')),
                        "edition"       : str(book.edition.encode('utf8', 'replace')),
                        "description"   : str(book.description.encode('utf8', 'replace')),
                        "ISBN"          : str(book.ISBN),
                        "state"         : str(book.howIsBook.encode('utf8', 'replace')),
                        "price"         : book.price,
                        "intent"        : str(book.intent.encode('utf8', 'replace')),
                        "sigle"         : str(book.sigle.sigle.encode('utf8', 'replace')),
                        "course"        : str(book.sigle.name.encode('utf8', 'replace')),
                        "firstname"     : str(book.owner.firstName.encode('utf8', 'replace')),
                        "lastname"      : str(book.owner.lastName.encode('utf8', 'replace')),
                        "email"         : str(book.owner.email),
                        "phone"         : str(book.owner.phone),
                    })

    if jsonFormat :
        return json.dumps(book,sort_keys=False)

    return book

# Json pour modification/suppression d'un livre
def getBookData(book, jsonFormat):

    book = OrderedDict({
                        "idvalue"       : str(book.pk),
                        "title"         : str(book.title.encode('utf8', 'replace')),
                        "author"        : str(book.author.encode('utf8', 'replace')),
                        "edition"       : str(book.edition.encode('utf8', 'replace')),
                        "description"   : str(book.description.encode('utf8', 'replace')),
                        "ISBN"          : str(book.ISBN),
                        "state"         : str(book.howIsBook.encode('utf8', 'replace')),
                        "price"         : book.price,
                        "intent"        : str(book.intent.encode('utf8', 'replace')),
                        "sigle"         : str(book.sigle.sigle.encode('utf8', 'replace')),
                        "course"        : str(book.sigle.name.encode('utf8', 'replace')),
                })

    if jsonFormat :
        return json.dumps(book)

    return book