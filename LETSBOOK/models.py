#!/usr/bin/env python
# -*- coding: cp1252 -*-

from django.db import models
import json
import base64

# Livre
class Book (models.Model):

    def __str__(self):
        return self.title.encode('utf8', 'replace') + "( " + self.sigle.sigle + " )"

    owner       = models.ForeignKey('Account',
                                    verbose_name  = 'Proprietaire du livre',
                                    )

    sigle       = models.ForeignKey('Course',
                                    verbose_name = 'Requis pour ce cours',
                                    )

    title       = models.CharField(verbose_name   = "Titre du livre",
                                   max_length     = 100, #50
                                   primary_key    = False)

    author      = models.CharField(verbose_name   = "Auteur(s) du livre",
                                   max_length     = 100, # 50
                                   primary_key    = False)

    edition     = models.CharField(verbose_name   = "Edition du livre",
                                   max_length     = 50,
                                   primary_key    = False)

    price       = models.FloatField(verbose_name    = "Prix du livre",
                                    default         = 0.00,
                                    primary_key     = False)

    howIsBook   = models.CharField(verbose_name   = "Etat du livre",
                                   max_length     = 50, # 100
                                   primary_key    = False)

    intent      = models.CharField(verbose_name   = "Intention du vendeur",
                                   max_length     = 50, # 30
                                   primary_key    = False)

    description = models.CharField(verbose_name   = "Description du livre",
                                   max_length     = 1000, # 100
                                   blank          = True,
                                   default        = "",
                                   primary_key    = False)

    ISBN        = models.CharField(verbose_name   = "ISBN (Code a barre) du livre",
                                   max_length     = 30,
                                   blank          = True,
                                   default        = "",
                                   primary_key    = False)

    # Suggestion de champs de livre
    # langue du livre       ***
    # maison d'edition      *

class Course (models.Model):

    def __str__(self):
        return self.sigle + "( " + self.name.encode('utf8', 'replace') + " )"

    department  = models.ForeignKey('Department',
                                    verbose_name  = 'Departement du cours',)

    name        = models.CharField(verbose_name   = "Nom du cours",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    sigle      = models.CharField(verbose_name   = "Sigle du cours",
                                   max_length     = 50, # 100
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du cours",
                                   max_length     = 1000, # 100
                                   blank          = True, # false
                                   default        = "",
                                   null           = False,
                                   primary_key    = False)

class Department (models.Model):

    def __str__(self):
        return self.name

    establishment = models.ForeignKey('Establishment',
                                      verbose_name = "Etablissement scolaire",
                                      )

    name        = models.CharField(verbose_name   = "Nom du Departement",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du departement",
                                   max_length     = 100,
                                   blank          = True, # false
                                   default        = "",
                                   null           = False,
                                   primary_key    = False)

# Etablissement scolaire
class Establishment (models.Model):

    def __str__(self):
        return self.name + "( " + self.street + ") "

    name        = models.CharField(verbose_name   = "Nom de l'etablissement scolaire",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    street      = models.CharField(verbose_name   = "Numero et nom de la rue (Ex : 1100, Rue Notre-Dame)",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    city        = models.CharField(verbose_name   = "Nom de la ville de l'etablissement",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    zipCode     = models.CharField(verbose_name   = "Code postal de l'etablissement scolaire",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    type        = models.CharField(verbose_name   = "Type de l'etablissement scolaire",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    webSite     = models.CharField(verbose_name   = "Site Web de l'etablissement scolaire",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

class Account (models.Model):

    def __str__(self):
        return self.lastName.encode('utf8', 'replace') + ", " + self.firstName.encode('utf8', 'replace') + "( " + self.email + ") "

    establishment = models.ForeignKey('Establishment',                      # Departement
                                      verbose_name  = "Etablissement scolaire",
                                      blank         = True,
                                      default       = None,
                                      )

    firstName   = models.CharField(verbose_name   = "Prenom de l'utilisateur",
                                   max_length     = 100,
                                   primary_key    = False)

    lastName    = models.CharField(verbose_name   = "Nom de l'utilisateur",
                                   max_length     = 100,
                                   primary_key    = False)

    email       = models.CharField(verbose_name   = "Email de l'utilisateur",
                                   max_length     = 100,
                                   null           = False,
                                   unique         = True,
                                  )

    phone       = models.CharField(verbose_name   = "Telephone de l'utilisateur",
                                   max_length     = 100,
                                   blank          = True,
                                   primary_key    = False)

    password    = models.CharField(verbose_name   = "Mot de passe du compte",
                                   max_length     = 100,
                                   null           = False,
                                   blank          = True,
                                   default        = "",
                                   primary_key    = False)

    faceBookID  = models.CharField(verbose_name   = "Identification FaceBook",
                                   max_length     = 100,
                                   null           = False,
                                   blank          = True,
                                   default        = "",
                                   primary_key    = False)

    googlePlusID = models.CharField(verbose_name   = "Identification Google Plus",
                                    max_length     = 100,
                                    null           = False,
                                    blank          = True,
                                    default        = "",
                                    primary_key    = False)
