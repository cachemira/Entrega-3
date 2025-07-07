from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Libro

register_models = [Familiar, Curso, Estudiante, Libro]

admin.site.register(register_models)