from django.shortcuts import render
from django.http import HttpResponseNotFound
# Create your views here.
def catch_all(request, path):
  
    return HttpResponseNotFound(render(request, '404.html').content)


def custom_404(request, exception):
    
    context = {'requested_path': request.path}
    return render(request, "404.html", context=context, status=404)