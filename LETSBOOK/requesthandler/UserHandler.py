from LETSBOOK.models import Book
from LETSBOOK.models import Account
from LETSBOOK.models import Department
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import json

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_HTTP_SUCCESS                   = 200
_HTTP_ERROR                     = 500
_HTTP_JSON                      = "application/json"

# Description d'un livre
_USER_ID             = "id"         # Clef primaire usager
_USER_DEPT           = "iddept"     # Clef primaire Departement
_USER_FNAME          = "fname"      # Prenom usager
_USER_LNAME          = "lname"      # Nom usager
_USER_EMAIL          = "email"      # email usager
_USER_PHONE          = "phone"      # Telephone usager
_USER_PWD            = "password"   # Mot de passe usager
_USER_FACEBOOK       = "facebook"   # Compte faceBook usager
_USER_GOOGLEPLUS     = "googleplus" # Compte Google Usager
_USER_BOOK           = "idbook"     # Clef primaire d'un livre

# Ajout ou modification d'un compte etudiant
def putUser(request):

    user = None

    # Modification
    if _USER_ID in request.GET:
        user = Account.objects.get(pk=request.GET[_USER_ID])

    # Ajout
    if user is None and _USER_FNAME in request.GET:
        user = Account(firstName=request.GET[_USER_FNAME])
    else:
        user.firstName          = request.GET[_USER_FNAME]

    # Pas de moyen de construction
    if _USER_FNAME not in request.GET and _USER_ID not in request.GET:
        return HttpResponse(status=_HTTP_ERROR)

    if _USER_LNAME in request.GET:
        user.lastName           = request.GET[_USER_LNAME]

    if _USER_DEPT in request.GET:

        try:
            user.department         = Department.objects.get(pk=request.GET[_USER_DEPT])
        except Department.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Departement " + request.GET[_USER_DEPT] + "n'existe pas")

    if _USER_EMAIL in request.GET:
        user.email              = request.GET[_USER_EMAIL]

    if _USER_PHONE in request.GET:
        user.phone              = request.GET[_USER_PHONE]

    if _USER_PWD in request.GET:
        user.password           = request.GET[_USER_PWD]

    if _USER_FACEBOOK in request.GET:
        user.faceBookID         = request.GET[_USER_FACEBOOK]

    if _USER_GOOGLEPLUS in request.GET:
        user.googlePlusID       = request.GET[_USER_GOOGLEPLUS]

    if user.password is None and user.faceBookID is None and user.googlePlusID is None:
        return HttpResponse(status=_HTTP_ERROR, content="Un mot de passe est requis")

    try:
        user.save()
    except Exception as e:
        return HttpResponse(status=_HTTP_ERROR, content=e.message)

    return HttpResponse(status=_HTTP_SUCCESS, content=getUserAccount(user, True))

# Recherche d'un compte usager
def getUser(request):

    params  = Q()

    # Proprietaire d'un livre
    if _USER_BOOK in request.GET:
        try:
            result = Book.objects.get(pk=request.GET[_USER_BOOK])
        except Book.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content= "Le livre " + request.GET[_USER_BOOK ] + " est inconnu")

        return HttpResponse(status=_HTTP_SUCCESS, content=getUserInfo(result.owner, True), content_type=_HTTP_JSON)

    # Identification compte LETSBOOK
    if _USER_EMAIL in request.GET and _USER_PWD in request.GET:
        params = params & Q(email       = str(request.GET[_USER_EMAIL]))
        params = params & Q(password    = str(request.GET[_USER_PWD]))

        try:
            result = Account.objects.get(params)
        except Account.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Le compte n'existe pas")

        return HttpResponse(status=_HTTP_SUCCESS, content=getUserAccount(result, True), content_type=_HTTP_JSON)

    # Identification Facebook
    if _USER_EMAIL in request.GET and _USER_FACEBOOK in request.GET:
        params = params & Q(email       = str(request.GET[_USER_EMAIL]))
        params = params & Q(faceBookID  = str(request.GET[_USER_FACEBOOK]))

        try:
            result = Account.objects.get(params)
        except Account.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Le compte n'existe pas")

        return HttpResponse(status=_HTTP_SUCCESS, content=getUserAccount(result, True), content_type=_HTTP_JSON)

    # Identification Google
    if _USER_EMAIL in request.GET and _USER_GOOGLEPLUS in request.GET:
        params = params & Q(email        = str(request.GET[_USER_EMAIL]))
        params = params & Q(googlePlusID = str(request.GET[_USER_GOOGLEPLUS]))

        try:
            result = Account.objects.get(params)
        except Account.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Le compte n'existe pas")

        return HttpResponse(status=_HTTP_SUCCESS, content=getUserAccount(result, True), content_type=_HTTP_JSON)

    return HttpResponse(status=_HTTP_ERROR, content="Identification/Recherche par ce(s) parametre(s) impossible")

# Suppression d'un compte usager
def deleteUser(request):

    if _USER_ID in request.GET:
        result = Account.objects.get(pk=str(request.GET[_USER_ID]))
        result.delete()
        return HttpResponse(status=_HTTP_SUCCESS)

    return HttpResponse(status=_HTTP_ERROR)

# Json pour l'affichage d'un usager seulement
def getUserInfo(user, jsonFormat):

    if jsonFormat :
        return json.dumps({
            "firstName"     : str(user.firstName.encode('utf8', 'replace')),
            "lastName"      : str(user.lastName.encode('utf8', 'replace')),
            "email"         : str(user.email),
            "phone"         : str(user.phone),
            })

    else:
        return {
            "firstName"     : str(user.firstName.encode('utf8', 'replace')),
            "lastName"      : str(user.lastName.encode('utf8', 'replace')),
            "email"         : str(user.email),
            "phone"         : str(user.phone),
            }

# Json pour une connexion user
def getUserAccount(user, jsonFormat):

    if jsonFormat :
        return json.dumps({
            "idvalue"       : user.pk,
            "firstName"     : str(user.firstName.encode('utf8', 'replace')),
            "lastName"      : str(user.lastName.encode('utf8', 'replace')),
            "email"         : str(user.email),
            "phone"         : str(user.phone),
            })

    else:
        return {
            "idvalue"       : user.pk,
            "firstName"     : str(user.firstName.encode('utf8', 'replace')),
            "lastName"      : str(user.lastName.encode('utf8', 'replace')),
            "email"         : str(user.email),
            "phone"         : str(user.phone),
            }