import json
from django.shortcuts import render, render_to_response, RequestContext, redirect, HttpResponse
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request, **kwargs):
    if request.method == 'POST':
        post_data = request.POST

        username = post_data.get('username')
        password = post_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("User logged in.")
            else:
                return HttpResponseForbidden("User no longer active.")
        else:
            return Http404("User not found.")
    elif request.method == "GET":
        return render_to_response('sportsstoreadmin/angularjs/views/adminLogin.html')


def admin_view(request, **kwargs):
    return render_to_response('sportsstoreadmin/admin.html', context_instance=RequestContext(request))


def main_view(request, **kwargs):
    return render_to_response('sportsstoreadmin/angularjs/views/adminMain.html', context_instance=RequestContext(request))


def products_view(request, **kwargs):
    return render_to_response('sportsstoreadmin/angularjs/views/adminProducts.html', context_instance=RequestContext(request))


def orders_view(request, **kwargs):
    return render_to_response('sportsstoreadmin/angularjs/views/adminOrders.html', context_instance=RequestContext(request))

