from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def sess_fun(request):
    num = request.session.get("visitors", 0) + 1
    request.session["visitors"] = num
    if num > 4:
        del request.session["visitors"]
    response = render(request, "hello/main.html", {"view_count": num})
    response.set_cookie('dj4e_cookie', 'c04c19c2', max_age=1000)
    return response
