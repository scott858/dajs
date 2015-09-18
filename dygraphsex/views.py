from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def example_app_view(request, **kwargs):
    return render_to_response('dygraphsex/angularjs/exampleApp.html',
                              {},
                              RequestContext(request))


def plot_view(request, **kwargs):
    return render_to_response('dygraphsex/angularjs/plot.html')
