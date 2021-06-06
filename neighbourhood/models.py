from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField()
    neighborhood_location = models.CharField()
    occupants_count = models.IntegerField(default=0)
    admin_foreign_key = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def create_neighbourhood_(self):
        self.save()

    def delete_neighbourhood_(self):
        self.delete()

    def find_neighbourhood(self, neighbourhood_id):
        return self.objects.filter(id = neighbourhood_id).all()

    def update_neighborhood(self):
        self.save()

    def update_occupants(self, new_count):
        self.occupants_count = new_count
        self.save()

class Profile(models.Model):
    names = models.CharField()
    neighborhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', default=None)
    user = models.ForeignKey(User)
    
class Business(models.Model):
    business_name = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    Business_email = models.EmailField()
    
    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    def find_business(self, business_id):
        return self.objects.filter(id = business_id).all()
    
    def update_business(self):
        self.save()
        
class TextPost(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_on = models.DateField(auto_now_add=True)
    text_content = models.TextField()
        
class ImagePost(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_on = models.DateField(auto_now_add=True)
    text_content = models.TextField()
    image = CloudinaryField('image', default=None)
