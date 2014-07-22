__author__ = 'julien'

from LETSBOOK.models import Course
from LETSBOOK.models import Department
from LETSBOOK.models import Establishment
from django.http import HttpResponse
from django.db.models import Q
import json

_COURSE_DEPT    = "iddept"
_COURSE_SCHOOL  = "idschool"
_DEPT_COURSE    = "idcourse"
_DEPT_SCHOOL    = "iddept"

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_HTTP_SUCCESS                   = 200
_HTTP_ERROR                     = 500
_HTTP_JSON                      = "application/json"

def getCourse(request):

    params  = Q()
    courses = None

    # Tous les cours d'un departement
    if _COURSE_DEPT in request.GET:

        try:
            dept    = Department.objects.get(pk=request.GET[_COURSE_DEPT])
        except Department.DoesNotExist:
            return HttpResponse(status=_HTTP_ERROR, content="Le departement " + request.GET[_COURSE_DEPT] + " n'existe pas")

        results = Course.objects.filter(department=dept)

        courses = {"courses" : []}

        for index in range(0, results.count()):
            courses["courses"].append(getCourseInfo(results[index], False))

        return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(courses), content_type=_HTTP_JSON)


    # Tous les cours
    results = Course.objects.all()

    courses = {"courses" : []}

    for index in range(0, results.count()):
        courses["courses"].append(getCourseInfo(results[index], False))

    return HttpResponse(status=_HTTP_SUCCESS, content=json.dumps(courses), content_type=_HTTP_JSON)

def getCourseInfo(course, jsonFormat):

    cours = { "course"  : {
        "sigle"         : str(course.sigle.encode('utf8', 'replace')),
        "name"          : str(course.name.encode('utf8', 'replace')),
        "description"   : str(course.description.encode('utf8', 'replace')),
        "deptname"      : str(course.department.name.encode('utf8', 'replace')),
        "deptdesc"      : str(course.department.description.encode('utf8', 'replace')),
        "estaname"      : str(course.department.etablishment.name.encode('utf8', 'replace'))
    }}

    if jsonFormat :
        return json.dumps(cours)

    return cours



#def getDepartement(request):

#def getUniversity(request):


