from LETSBOOK.requesthandler import SchoolHandler
from LETSBOOK.requesthandler import BookHandler
from LETSBOOK.requesthandler import UserHandler

# Type de requetes
_REQUEST_PUT    = 'PUT'
_REQUEST_GET    = 'GET'
_REQUEST_DELETE = 'DELETE'

# Create your views here.
def school(request):

    if request.method == _REQUEST_PUT:
        return SchoolHandler.putSchool(request)

    if request.method == _REQUEST_GET:
        return SchoolHandler.getSchool(request)

    if request.method == _REQUEST_DELETE:
        return SchoolHandler.deleteSchool(request)

def book(request):

    if request.method == _REQUEST_PUT:
        return BookHandler.putBook(request)

    if request.method == _REQUEST_GET:
        return BookHandler.getBook(request)

    if request.method == _REQUEST_DELETE:
        return BookHandler.deleteBook(request)

def user(request):

    if request.method == _REQUEST_PUT:
        return UserHandler.putUser(request)

    if request.method == _REQUEST_GET:
        return UserHandler.getUser(request)

    if request.method == _REQUEST_DELETE:
        return UserHandler.deleteUser(request)
