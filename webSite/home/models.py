# -*- coding: utf-8 -*-
from django.db import models


def iterativeIsEnfant(activiteMontante, autreActiviteAudit):
    if activiteMontante is None:
        return False
    else:
        if activiteMontante == autreActiviteAudit:
            return True
        else:
            return iterativeIsEnfant(activiteMontante.activiteParente, autreActiviteAudit)


class ActiviteAudit(models.Model):
    # activité parente, peut être nulle si on est à la "racine"
    activiteParente = models.ForeignKey('self', related_name='activiteEnfante', null=True, blank=True) # l'objet courant correspond à l'enfant du parent : activiteEnfante de activiteParente
    # description de l'activité, ex : test d'intrusion
    nom_activite = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nom_activite

    def isEnfant(self, autreActiviteAudit):
        if autreActiviteAudit is None:
            return True
        return iterativeIsEnfant(self, autreActiviteAudit)


class ImpactVuln(models.Model):
    # ex : 4
    niveau = models.IntegerField()
    # ex : Critique
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description


class DifficulteExploitVuln(models.Model):
    # ex : 4
    niveau = models.IntegerField()
    # ex : tres difficile a exploiter, couts eleves etc..
    description_acte_volontaire = models.TextField()
    # ex: tres rarement voire jamais mis en evidence involontairement
    description_acte_involontaire = models.TextField()

    def __unicode__(self):
        return "difficultee = "+str(self.niveau)


class Rapport(models.Model):
    # ex : RAN-01-1995
    nom_rapport = models.CharField(max_length=255)
    # ex : 30/12/2006
    date_rapport = models.DateField()
    # ex : ecrit par Sebastien Herniotte et relu par Thomas Valez
    auditeurs_impliques = models.TextField() # va peut-etre changer si l'on gere les utilisateurs

    def __unicode__(self):
        return self.nom_rapport


class MotClef(models.Model):
    # ex : XSS, Cross-Site-Scriptiong, SQLi...
    nom = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nom


class Vulnerabilite(models.Model):
    # l'impact de la vuln
    impact = models.ForeignKey(ImpactVuln)
    # difficulte d'exploit de la vuln
    difficulte_exploit = models.ForeignKey(DifficulteExploitVuln)
    # un rapport ou la vuln a ete identifiee et expliquee
    rapport_associe = models.OneToOneField(Rapport)
    # tous les mot-clefs associés à cette vuln
    mots_clefs = models.ManyToManyField(MotClef)
    # toutes les activités d'audit, les plus précises possibles, qui sont liées à la vuln
    activites_liees = models.ManyToManyField(ActiviteAudit)
    # explication de la vulnerabilite pour le client (ou qqun qui ne la connait pas)
    description = models.TextField()
    # la vuln est-elle consideree en boite noire ? True/False
    estBoiteNoire = models.BooleanField()

    def __unicode__(self):
        return self.description[:50]+"..."


class EcheanceReco(models.Model):
    # urgence de la reco, ex : 4
    niveau = models.IntegerField()
    # description correspondante au niveau, ex : extremement urgent
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description


class DifficulteReco(models.Model):
    # niveau de difficulte de la mise en place de la recommandation, ex : 1
    niveau = models.IntegerField()
    # description correspondante au niveau, ex : tres facile
    description = models.CharField(max_length=255)
    # cout humain par mois, ex : 1h.m
    cout_homme_mois = models.FloatField()
    # cout depart en euros
    cout_initial_euros = models.FloatField()
    # cout iteratif en euros
    cout_recurrent_euros = models.FloatField()

    def __unicode__(self):
        return self.description


class Recommandation(models.Model):
    # echeance de la recommandation, si elle est urgente
    echeance = models.ForeignKey(EcheanceReco)
    # difficulte de mise en place de la reco
    cout_reco = models.ForeignKey(DifficulteReco)
    # la vunerabilite associee a la recommandation
    vuln = models.ForeignKey(Vulnerabilite)
    # explication detaillee de la recommandation pour le client
    explication = models.TextField()

    def __unicode__(self):
        return self.explication[:50]+"..."

