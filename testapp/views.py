from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_example(request, arg):
    response = {'mensaje' : arg}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})

def gallery(request):
    return render(request, 'testapp/gallery.html')

def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)