from LETSBOOK.requesthandler import AdminHandler
from LETSBOOK.requesthandler import SchoolHandler
from LETSBOOK.requesthandler import BookHandler
from LETSBOOK.requesthandler import UserHandler

# Code de serveur
# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
_HTTP_ERROR                     = 500
from django.http import HttpResponse

# Type de requetes
_REQUEST_PUT    = 'PUT'
_REQUEST_GET    = 'GET'
_REQUEST_DELETE = 'DELETE'

# Create your views here.
def school(request):

    if request.method == _REQUEST_PUT:
        return AdminHandler.putSchool(request)

    if request.method == _REQUEST_GET:
        return AdminHandler.getSchool(request)

    if request.method == _REQUEST_DELETE:
        return AdminHandler.deleteSchool(request)

    return HttpResponse(status=_HTTP_ERROR)

def course(request):

    if request.method == _REQUEST_GET:
        return SchoolHandler.getCourse(request)

    return HttpResponse(status=_HTTP_ERROR)

def dept(request):

    if request.method == _REQUEST_GET:
        return SchoolHandler.getDepartement(request)

    return HttpResponse(status=_HTTP_ERROR)

def departement(request):

    if request.method == _REQUEST_GET:
        return SchoolHandler.getCourse(request)

    return HttpResponse(status=_HTTP_ERROR)

def book(request):

    if request.method == _REQUEST_PUT:
        return BookHandler.putBook(request)

    if request.method == _REQUEST_GET:
        return BookHandler.getBook(request)

    if request.method == _REQUEST_DELETE:
        return BookHandler.deleteBook(request)

    return HttpResponse(status=_HTTP_ERROR)

def user(request):

    if request.method == _REQUEST_PUT:
        return UserHandler.putUser(request)

    if request.method == _REQUEST_GET:
        return UserHandler.getUser(request)

    if request.method == _REQUEST_DELETE:
        return UserHandler.deleteUser(request)

    return HttpResponse(status=_HTTP_ERROR)