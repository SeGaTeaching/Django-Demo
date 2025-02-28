from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    scheme = request.scheme
    method = request.method
    address = request.get_host()
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path
    encoding = request.encoding
    session = request.session
    session['task'] = 'do laundry'
    
    
    response = HttpResponse()
    response.headers['Age'] = 20
    status = response.status_code
    msg = f"""
    <html>
    <body>
        <h1>Request Information</h1>
        <p>Scheme: {scheme}</p>
        <p>Method: {method}</p>
        <p>Address: {address}</p>
        <p>User Agent: {user_agent}</p>
        <p>Path Info: {path_info}</p>
        <p>Encoding: {encoding}</p>
        <p>Response: {response.headers}</p>
        <p>Status: {status}</p>
        <p>Session: {session.items()}</p>
        <p>Headers: {request.headers.items()}</p>     
    </body>
    </html>
    """
    return HttpResponse(msg)

def pathview(request, name, id):
    return HttpResponse(f'Name: {name} UserID: {id}')

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f'Name: {name} :: UserID: {id}')

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == 'POST':
        id = request.POST['user-id']
        name = request.POST['user-name']
        email = request.POST['user-email']
    return HttpResponse(f'Name: {name} UserID: {id} <br> test:{email}')

def math(request, num1, num2):
    multiply = int(num1) * int(num2)
    return HttpResponse(multiply)