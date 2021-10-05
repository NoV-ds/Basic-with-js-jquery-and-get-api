from django.db import models

# Create your models here.
class UserProfile(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
    

class usercommunity(models.Model):
    fullname = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    community = models.CharField(max_length=50)

    def __str__(self):
        return self.community
    