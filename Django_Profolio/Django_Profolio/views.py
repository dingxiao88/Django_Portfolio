from django.shortcuts import render
from gallery.models import Gallery
from . import biying


def home(request):


    # g = biying.get_one_photo()
    # url_photo=g.get_one_photo()
	gallerys = Gallery.objects
	# return render(request, 'home.html', {'gallerys': gallerys})

	pic1 = biying.get_one_photo(0)
	pic2 = biying.get_one_photo(1)
	pic3 = biying.get_one_photo(2)

	return render(request, 'index.html',  {'gallerys': gallerys, 'url_photo_1':pic1, 'url_photo_2':pic2, 'url_photo_3':pic3})