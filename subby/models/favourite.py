from django.db import models
from django.conf import settings
from subby.models.sublet import Sublet
from subby.managers.favouritesmanager import FavouriteManager

class Favourite(models.Model):


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    sublet = models.ForeignKey(Sublet, on_delete=models.CASCADE, null=True)

    objects = FavouriteManager()

def __str__(self):
    return self.sublet.get_sublet_title

# Getters
def get_created_at(self):
     return self.created_at

def get_updated_at(self):
    return self.updated_at


# Setters
def set_created_at(self, created_at):
    self.created_at = created_at
    return


def set_updated_at(self):
    self.updated_at = pytz.utc.localize(datetime.datetime.now())
    return