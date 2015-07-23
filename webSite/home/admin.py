# coding: utf-8
from django.contrib import admin

# Register your models here.
from .models import *


class RecommandationInline(admin.StackedInline):
    model = Recommandation
    extra = 1
    classes = ('collapse open',)
    inline_classes = ('collapse open',)
#
#
# class RapportInline(admin.StackedInline):
#     model = Rapport


# on permet à l'admin d'ajouter dynamiquement des recommandations et des rapports lorsqu'il créé sa vuln
class VulnerabiliteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Echelle de sévérité', {'fields': ['impact', 'difficulte_exploit', 'estBoiteNoire']}),
        ('Pour retrouver la vuln facilement..', {'fields': ['rapports_ou_on_a_trouve_la_vuln', 'mots_clefs', 'activites_liees']}),
        ('Une bonne description de la vuln pour le client', {'fields': ['description']})
    ]
    inlines = [RecommandationInline]
    list_display = ('__unicode__', 'impact', 'difficulte_exploit', 'estBoiteNoire')


admin.site.register(Vulnerabilite, VulnerabiliteAdmin)


# customisation du formulaire de création d'une recommandation, pas très intéressant
class RecommandationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Echelle d\'urgence', {'fields': ['echeance', 'cout_reco']}),
        ('La vuln associée (optionnel)', {'fields': ['vuln',]}),
        ('Une bonne explication de la recommandation pour le client', {'fields': ['explication']})
    ]
    list_display = ('__unicode__', 'echeance', 'cout_reco')


admin.site.register(Recommandation, RecommandationAdmin)

############################################################
# Le reste du fichier ne sert qu'à cacher des models de l'index de l'interface admin
# = pas interessant pour un futur lecteur
############################################################


# class ImpactVulnAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(ImpactVuln, ImpactVulnAdmin)
#
#
# class DifficulteExploitVulnAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(DifficulteExploitVuln, DifficulteExploitVulnAdmin)
#
#
# class RapportAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(Rapport, RapportAdmin)
#
#
# class MotClefAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(MotClef, MotClefAdmin)
#
#
# class EcheanceRecoAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(EcheanceReco, EcheanceRecoAdmin)
#
#
# class DifficulteRecoAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(DifficulteReco, DifficulteRecoAdmin)
#
#
# class ActiviteAuditAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Return empty perms dict thus hiding the model from admin index
#         """
#         return {}
#
# admin.site.register(ActiviteAudit, ActiviteAuditAdmin)

admin.site.register(ActiviteAudit)
admin.site.register(DifficulteReco)
admin.site.register(EcheanceReco)
admin.site.register(ImpactVuln)
admin.site.register(DifficulteExploitVuln)
admin.site.register(Rapport)
admin.site.register(MotClef)
