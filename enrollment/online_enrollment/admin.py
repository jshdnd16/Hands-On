from django.contrib import admin
from .models import TestingDatabase, StudentInformation, Education, Adress, Subject, FamilyBackground

# Register your models here.
admin.site.register(TestingDatabase)
admin.site.register(StudentInformation)
admin.site.register(Education)
admin.site.register(Adress)
admin.site.register(Subject)
admin.site.register(FamilyBackground)