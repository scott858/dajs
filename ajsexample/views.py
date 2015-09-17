from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def example_app_view(request, **kwargs):
    return render_to_response('ajsexample/angularjs/exampleApp.html',
                              {},
                              RequestContext(request))
