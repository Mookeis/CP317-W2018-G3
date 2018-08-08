from django.shortcuts import render, get_object_or_404,redirect
from subby.models.favourite import Favourite
from subby.models.sublet import Sublet
from subby.models.image import SubletImage
from subby.decorators.loginrequiredmessage import message_login_required


	
@message_login_required
def FavouriteLister(request, user_id):
	fav_list = Favourite.objects.filter(user=request.user)
	
	image_dict = {}
	image_list = []
	for fav in fav_list:
		images = SubletImage.objects.filter(sublet=fav.sublet)
		image_dict = images[0]
		image_list.append(images[0])
	fav_dict = {
		'fav_list':fav_list,
		'image_dict':image_dict,
		'image_list':image_list,
	}
	return render(request, 'favourite/favourite_list.html', fav_dict)
    



@message_login_required
def favourite_bar_lister(request):
    fav_list = Favourite.objects.filter(user=request.user)

    image_list = []
    for fav in fav_list:
        images = SubletImage.objects.filter(sublet=fav.sublet)
        image_list.append(images[0])

    data = { 'fav_list': fav_list,
             'image_list': image_list,
             }

    return render(request, 'favourite/favourite_nav.html', data)


def fav_unfav_sublet(request):

    current_user = request.user
    next = request.POST.get('next', '/')
    # Check if sublet exists
    try:
        sublet = get_object_or_404(Sublet, id=request.POST['subletid'])
    except(KeyError, Sublet.DoesNotExist):
        return redirect(next, id=sublet.get_sublet_id())
    else:
        if(Favourite.objects.filter(user=current_user, sublet=sublet).count() > 0): #Remove favourite
            Favourite.objects.remove_favourite(sublet, current_user)
        else: #Add favourite
            Favourite.objects.create_favourite(sublet, current_user)
        return redirect(next, id=sublet.get_sublet_id())



