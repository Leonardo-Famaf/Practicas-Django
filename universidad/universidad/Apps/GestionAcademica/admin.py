# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from universidad.Apps.GestionAcademica.models import *

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)
