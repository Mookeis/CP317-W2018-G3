from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from subby.models.image import SubletImage
# Create your views here.

def index(req):
	"""
	---------------------
	creating particular index.
	Use:render=index(request)
	---------------------
	Parameters:
		request - request object
	Return:
		render - render object
	---------------------
	"""
    images = SubletImage.objects.all()
    return render(req, 'application/base.html', {'images' : images})
