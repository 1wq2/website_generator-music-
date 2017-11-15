from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse, request
#from django.template import loader
from django.shortcuts import render
from .models import Album

def index(request):

    """html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request)) #(^-^) """

    all_albums =Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album.id)
    except Album.DoesNotExist:
        raise Http404("ALbum doesn't exist")
        return render(request, 'music/index.html', {'album': album})

    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")