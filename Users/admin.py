from django.contrib import admin
from Users.models import *
# Register your models here.
admin.site.register(UserInformation)
admin.site.register(UserContact)
admin.site.register(UserBackground)
admin.site.register(UserEducation)
admin.site.register(UserLanguage)
admin.site.register(UserGuide)
admin.site.register(UserIdentity)