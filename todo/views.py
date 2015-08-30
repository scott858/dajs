from django.shortcuts import render, render_to_response, RequestContext


def todo_view(request, **kwargs):
    return render_to_response('todo/todo.html', context_instance=RequestContext(request))
