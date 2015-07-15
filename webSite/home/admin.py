from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ImpactVuln)
admin.site.register(DifficulteExploitVuln)
admin.site.register(Rapport)
admin.site.register(Vulnerabilite)
admin.site.register(MotClef)
admin.site.register(EcheanceReco)
admin.site.register(DifficulteReco)
admin.site.register(Recommandation)
admin.site.register(ActiviteAudit)