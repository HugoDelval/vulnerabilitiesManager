# -*- coding: utf-8 -*-
from django.db import models


def recursiveIsEnfant(activiteMontante, autreActiviteAudit):
    if activiteMontante is None:
        return False
    else:
        if activiteMontante == autreActiviteAudit:
            return True
        else:
            return recursiveIsEnfant(activiteMontante.activiteParente, autreActiviteAudit)


class ActiviteAudit(models.Model):
    # activité parente, peut être nulle si on est à la "racine"
    activiteParente = models.ForeignKey('self', related_name='activiteEnfante', null=True, blank=True) # l'objet courant correspond à l'enfant du parent : activiteEnfante de activiteParente
    # description de l'activité, ex : test d'intrusion
    nom_activite = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nom_activite

    def isEnfant(self, autreActiviteAudit):
        """
        :param autreActiviteAudit: l'activite d'audit dont laquelle on veut savoir si l'on est enfant
        :return:True si self est un enfant de autreActiviteAudit
        """
        if autreActiviteAudit is None:
            return True
        return recursiveIsEnfant(self, autreActiviteAudit)


class ImpactVuln(models.Model):
    # ex : 4
    niveau = models.IntegerField()
    # ex : Critique
    description = models.CharField(max_length=255)
    # ex : dizaine ou centaine d’euros annuels... blablablaba
    description_detaillee = models.TextField()

    def __unicode__(self):
        return self.description


class DifficulteExploitVuln(models.Model):
    # ex : 4
    niveau = models.IntegerField()
    # ex : difficile
    description_niveau = models.CharField(max_length=255)
    # ex : tres difficile a exploiter, couts eleves etc..
    description_acte_volontaire = models.TextField()
    # ex: tres rarement voire jamais mis en evidence involontairement
    description_acte_involontaire = models.TextField()

    def __unicode__(self):
        return self.description_niveau


class MotClef(models.Model):
    # ex : XSS, Cross-Site-Scriptiong, SQLi...
    nom = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.nom


class Rapport(models.Model):
    # ex : RAN-01-1995
    nom_rapport = models.CharField(max_length=255)
    # ex : 30/12/2006
    date_rapport = models.DateField()
    # ex : ecrit par Sebastien Herniotte et relu par Thomas Valez
    auditeurs_impliques = models.TextField() # va peut-etre changer si l'on gere les utilisateurs

    class Meta:
        ordering = ['nom_rapport']

    def __unicode__(self):
        return self.nom_rapport


class Vulnerabilite(models.Model):
    # l'impact de la vuln
    impact = models.ForeignKey(ImpactVuln)
    # difficulte d'exploit de la vuln
    difficulte_exploit = models.ForeignKey(DifficulteExploitVuln)
    # les rapports où on a trouvé la vuln
    rapports_ou_on_a_trouve_la_vuln = models.ManyToManyField(Rapport, blank=True)
    # tous les mot-clefs associés à cette vuln
    mots_clefs = models.ManyToManyField(MotClef)
    # toutes les activités d'audit, les plus précises possibles, qui sont liées à la vuln
    activites_liees = models.ManyToManyField(ActiviteAudit)
    # explication de la vulnerabilite pour le client (ou qqun qui ne la connait pas)
    description = models.TextField()
    # definition de la vulnerabilite pour le client 
    definition = models.TextField()
    # la vuln est-elle consideree en boite noire ? True/False
    estBoiteNoire = models.BooleanField()

    def __unicode__(self):
        return self.description[:70]+"..."


class EcheanceReco(models.Model):
    # urgence de la reco, ex : 4
    niveau = models.IntegerField()
    # description correspondante au niveau, ex : extremement urgent
    description = models.CharField(max_length=255)
    # ex : à faire dans vraiment pas longtemps, voire dans.. blabla
    description_detaillee = models.TextField()

    def __unicode__(self):
        return self.description


class DifficulteReco(models.Model):
    # niveau de difficulte de la mise en place de la recommandation, ex : 1
    niveau = models.IntegerField()
    # description correspondante au niveau, ex : tres facile
    description = models.CharField(max_length=255)
    # cout humain par mois, ex : 1h.m
    cout_homme_mois = models.FloatField(default=0)
    # cout depart en euros
    cout_initial_euros = models.FloatField(default=0)
    # cout iteratif en euros
    cout_recurrent_euros = models.FloatField(default=0)
    # ex : cette recommandation nécessite blablabliblu
    description_detaillee = models.TextField()

    def __unicode__(self):
        return self.description


# class ThemeReco(models.Model):
#     # ex : réseau, architecture, gestion des sauvegardes..
#     nom = models.CharField(max_length=255, unique=True)

#     def __unicode__(self):
#         return self.nom


class Recommandation(models.Model):
    # echeance de la recommandation, si elle est urgente
    echeance = models.ForeignKey(EcheanceReco)
    # difficulte de mise en place de la reco
    cout_reco = models.ForeignKey(DifficulteReco)
    # les rapports où on a trouvé la vuln
    rapports_ou_on_a_trouve_la_reco = models.ManyToManyField(Rapport, blank=True)
    # thèmes de la reco
    themes = models.ManyToManyField(MotClef, blank=True)
    # la vunerabilite associee a la recommandation
    vuln = models.ForeignKey(Vulnerabilite, blank=True, null=True)
    # explication detaillee de la recommandation pour le client
    explication = models.TextField()

    def __unicode__(self):
        return self.explication[:70]+"..."

