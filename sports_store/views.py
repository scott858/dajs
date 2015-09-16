from django.shortcuts import render, render_to_response, RequestContext


def sports_store_view(request, **kwargs):
    return render_to_response('sports_store/sports_store.html', RequestContext(request))
