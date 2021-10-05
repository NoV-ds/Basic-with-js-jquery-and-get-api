from django.contrib import admin
from .models import UserProfile, usercommunity

# Register your models here.
admin.site.register(usercommunity)

admin.site.register(UserProfile)