from django.contrib import admin
from .models import Inscription,Member,Activity

admin.site.register([Member,Inscription,Activity])
