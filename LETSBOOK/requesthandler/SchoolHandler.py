__author__ = 'julien'

from LETSBOOK.models import Course
from LETSBOOK.models import Department
from LETSBOOK.models import Establishment
from django.http import HttpResponse
from django.db.models import Q
import json

_SCHOOL         = "idschool"

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_HTTP_SUCCESS                   = 200
_HTTP_ERROR                     = 500
_HTTP_JSON                      = "application/json"

def getUniversity(request):

    # Nom universite
    if _SCHOOL in request.GET:

        try:
            school = Establishment.objects.get(pk=str(request.GET[_SCHOOL]))
        except Establishment.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="L'ecole est inconnue")

        response    = getSchoolInfo(school, False)

        depts       = Department.objects.filter(etablishment=school)

        for dept in range(0, depts.count()):
            response["depts"].append(getDeptInfo(depts[dept], False))

            courses = Course.objects.filter(department=depts[dept])

            for course in range(0, courses.count()):
                response["depts"][dept]["courses"].append(getCourseInfo(courses[course], False))


        return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(response), content_type=_HTTP_JSON)

    return HttpResponse(status=_HTTP_ERROR)

def getSchoolInfo(school, jsonFormat):

    school = {
                  "idvalue" : str(school.pk),
                  "name"    : str(school.name.encode('utf8', 'replace')),
                  "street"  : str(school.street.encode('utf8', 'replace')),
                  "city"    : str(school.city.encode('utf8', 'replace')),
                  "zipcode" : str(school.zipCode.encode('utf8', 'replace')),
                  "type"    : str(school.type.encode('utf8', 'replace')),
                  "website" : str(school.webSite.encode('utf8', 'replace')),
                  "depts"   : [],
            }

    if jsonFormat:
        return json.dumps(school)

    return school

def getDeptInfo(dept, jsonFormat):

    depts = {
                "idvalue"       : str(dept.pk),
                "name"          : str(dept.name.encode('utf8', 'replace')),
                "description"   : str(dept.description.encode('utf8', 'replace')),
                "courses"       : [],
            }

    if jsonFormat :
        return json.dumps(depts)

    return depts

def getCourseInfo(course, jsonFormat):

    cours = {
                "idvalue"       : str(course.pk),
                "sigle"         : str(course.sigle.encode('utf8', 'replace')),
                "name"          : str(course.name.encode('utf8', 'replace')),
                "description"   : str(course.description.encode('utf8', 'replace')),
           }

    if jsonFormat :
        return json.dumps(cours)

    return cours