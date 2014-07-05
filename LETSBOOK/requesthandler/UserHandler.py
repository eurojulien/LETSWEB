from LETSBOOK.models import Book
from LETSBOOK.models import Account
from LETSBOOK.models import Department
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import json

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_ADD_OR_MODIFY_RECORD_SUCCESS   = 201
_ADD_OR_MODIFY_RECORD_FAIL      = 202

# Description d'un livre
_USER_ID             = "id"         # Clef primaire usager
_USER_DEPT           = "dept"       # Clef primaire Departement
_USER_FNAME          = "fname"      # Prenom usager
_USER_LNAME          = "lname"      # Nom usager
_USER_EMAIL          = "email"      # email usager
_USER_PHONE          = "phone"      # Telephone usager
_USER_PWD            = "password"   # Mot de passe usager
_USER_FACEBOOK       = "facebook"   # Compte faceBook usager
_USER_GOOGLEPLUS     = "googleplus" # Compte Google Usager
_USER_BOOK           = "book"       # Clef primaire d'un livre

# Ajout ou modification d'un compte etudiant
def putUser(request):

    user = None

    # Modification
    if _USER_ID in request.GET:
        user = Account.objects.get(pk=request.GET[_USER_ID])

    # Ajout
    if user is None and _USER_FNAME in request.GET:
        user = Account(title=_USER_FNAME)
    else:
        user.firstName          = request.GET[_USER_FNAME]

    # Pas de moyen de construction
    if _USER_FNAME not in request.GET and _USER_ID not in request.GET:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    if _USER_LNAME in request.GET:
        user.lastName           = request.GET[_USER_LNAME]

    if _USER_DEPT in request.GET:
        user.department         = Department.objects.get(pk=request.GET[_USER_DEPT])

    if _USER_PHONE in request.GET:
        user.phone              = request.GET[_USER_PHONE]

    if _USER_PWD in request.GET:
        user.password           = request.GET[_USER_PWD]

    if _USER_FACEBOOK in request.GET:
        user.faceBookID         = request.GET[_USER_FACEBOOK]

    if _USER_GOOGLEPLUS in request.GET:
        user.googlePlusID       = request.GET[_USER_GOOGLEPLUS]

    user.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

# Recherche d'un compte usager
def getUser(request):

    # Recherche avec clef primaire
    if _USER_ID in request.GET:
        results = Account.objects.get(pk=request.GET[_USER_ID])
        return HttpResponse(results.getJson(), content_type='application/response')

    params  = Q()

    # Proprietaire d'un livre
    if _USER_BOOK in request.GET:
        result = Book.objects.get(pk=request.GET[_USER_BOOK]).owner
        return HttpResponse(result.getJson(), content_type='application/response')

    # Identification compte LETSBOOK
    if _USER_EMAIL in request.GET and _USER_PWD in request.GET:
        params = params & Q(email       = str(request.GET[_USER_EMAIL]))
        params = params & Q(password    = str(request.GET[_USER_PWD]))

        result = Account.objects.get(params)
        return HttpResponse(result.getJson())

    # Identification Facebook
    if _USER_EMAIL in request.GET and _USER_FACEBOOK in request.GET:
        params = params & Q(email       = str(request.GET[_USER_EMAIL]))
        params = params & Q(faceBookID  = str(request.GET[_USER_FACEBOOK]))

        result = Account.objects.get(params)
        return HttpResponse(result.getJson())

    # Identification Google
    if _USER_EMAIL in request.GET and _USER_GOOGLEPLUS in request.GET:
        params = params & Q(email        = str(request.GET[_USER_EMAIL]))
        params = params & Q(googlePlusID = str(request.GET[_USER_GOOGLEPLUS]))

        result = Account.objects.get(params)
        return HttpResponse(result.getJson())

    return HttpResponse(status=500, content="Recherche par ce(s) parametre(s) impossible")

# Suppression d'un compte usager
def deleteUser(request):

    if _USER_ID in request.GET:
        result = Account.objects.get(pk=str(request.GET[_USER_ID]))
        result.delete()
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

