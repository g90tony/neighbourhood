from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField()
    neighborhood_location = models.CharField
    occupants_count = models.IntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User)
    
    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    def find_neigborhood(self, neighbourhood_id):
        return self.objects.filter(id = neighbourhood_id).first()

    def update_neighborhood(self):
        self.save()

    def update_occupants(self, new_count):
        self.occupants_count = new_count
        self.save()
