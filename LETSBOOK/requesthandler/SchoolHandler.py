from LETSBOOK.models import Establishment
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_ADD_OR_MODIFY_RECORD_SUCCESS   = 201
_ADD_OR_MODIFY_RECORD_FAIL      = 202

# Description d'un etablissement scolaire
_SCHOOL_ID      = "id"
_SCHOOL_NAME    = "name"
_SCHOOL_STREET  = "street"
_SCHOOL_CITY    = "city"
_SCHOOL_ZIP     = "zipcode"
_SCHOOL_TYPE    = "type"
_SCHOOL_WEB     = "website"

# Ajout ou modification d'un etablissement scolaire
def putSchool(request):

    school = Establishment()

    if _SCHOOL_NAME in request.GET:

        try:
            school = Establishment.objects.get(name=request.GET[_SCHOOL_NAME])

        except ObjectDoesNotExist:
            school = Establishment(name=request.GET[_SCHOOL_NAME])

    else:
        return HttpResponse(status=_ADD_OR_MODIFY_RECORD_FAIL)

    if _SCHOOL_STREET in request.GET:
        school.street   = request.GET[_SCHOOL_STREET]

    if _SCHOOL_CITY in request.GET:
        school.city     = request.GET[_SCHOOL_CITY]

    if _SCHOOL_ZIP in request.GET:
        school.zipCode  = request.GET[_SCHOOL_ZIP]

    if _SCHOOL_TYPE in request.GET:
        school.type     = request.GET[_SCHOOL_TYPE]

    if _SCHOOL_WEB in request.GET:
        school.webSite  = request.GET[_SCHOOL_WEB]

    school.save()

    return HttpResponse(status=_ADD_OR_MODIFY_RECORD_SUCCESS)

# Recherche d'un etablissement scolaire
def getSchool(request):

    schools = 0

    if _SCHOOL_ID in request.GET:
        schools = Establishment.objects.get(pk=request.GET[_SCHOOL_ID])
        return HttpResponse(schools.getJson(), content_type='application/response')

    params = {}

    if _SCHOOL_NAME in request.GET:
        params['name_contains']     = str(request.GET[_SCHOOL_NAME])

    if _SCHOOL_STREET in request.GET:
        params['street_contains']   = str(request.GET[_SCHOOL_STREET])

    if _SCHOOL_TYPE in request.GET:
        params['type_contains']     = str(request.GET[_SCHOOL_TYPE])

    if _SCHOOL_CITY in request.GET:
        params['city_contains']     = str(request.GET[_SCHOOL_CITY])

    if _SCHOOL_ZIP in request.GET:
        params['zipCode_contains']  = str(request.GET[_SCHOOL_ZIP])

    if _SCHOOL_WEB in request.GET:
        params['webSite_contains']  = str(request.GET[_SCHOOL_WEB])

    results   = Establishment.objects.filter(params)

    return HttpResponse("Banane", content_type='application/response')

