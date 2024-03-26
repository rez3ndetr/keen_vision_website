from django.contrib import admin

# Register your models here.


from .models import bid, Registration

admin.site.register(bid)

admin.site.register(Registration)

# admin.site.register(User)