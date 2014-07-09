#!/usr/bin/env python
# -*- coding: cp1252 -*-

from django.db import models
import json
import base64

# Livre
class Book (models.Model):

    def __str__(self):
        return self.title.encode('utf8', 'replace') + "( " + self.sigle.sigle + " )"

    INTENT_OPTIONS = (
        ('V', 'vente'),
        ('L', 'location'),
        ('P', 'Pret'),
        ('D', 'Don'),
    )

    owner       = models.ForeignKey('Account')
    sigle       = models.ForeignKey('Course')

    title       = models.CharField(verbose_name   = "Titre du livre",
                                   max_length     = 50,
                                   primary_key    = False)

    author      = models.CharField(verbose_name   = "Auteur du livre",
                                   max_length     = 50,
                                   primary_key    = False)

    edition     = models.CharField(verbose_name   = "Edition du livre",
                                   max_length     = 50,
                                   primary_key    = False)

    price       = models.FloatField(verbose_name    = "Prix du livre",
                                    default         = 0.00,
                                    primary_key     = False)

    howIsBook   = models.CharField(verbose_name   = "Etat du livre",
                                   max_length     = 100,
                                   primary_key    = False)

    intent      = models.CharField(verbose_name   = "Intention du vendeur",
                                   max_length     = 1,
                                   choices        = INTENT_OPTIONS,
                                   primary_key    = False)

    description = models.CharField(verbose_name   = "Description du livre",
                                   max_length     = 100,
                                   primary_key    = False)

    ISBN        = models.CharField(verbose_name   = "ISBN (Code a barre) du livre",
                                   max_length     = 30,
                                   primary_key    = False)


    # picture

    # Format JSON
    def getJson(self):

        return json.dumps({
                'pk'            : str(self.pk),
                'title'         : str(self.title.encode('utf8', 'replace')),
                'author'        : str(self.author.encode('utf8', 'replace')),
                'edition'       : str(self.edition.encode('utf8', 'replace')),
                'description'   : str(self.description.encode('utf8', 'replace')),
                'ISBN'          : str(self.ISBN),
                'state'     : str(self.howIsBook.encode('utf8', 'replace')),
                'price'         : float(self.price),
                'intent'        : str(self.intent.encode('utf8', 'replace'))
        })

    # Format String
    def getStr(self):

        return {
                'pk'            : str(self.pk),
                'title'         : str(self.title.encode('utf8', 'replace')),
                'author'        : str(self.author.encode('utf8', 'replace')),
                'edition'       : str(self.edition.encode('utf8', 'replace')),
                'description'   : str(self.description.encode('utf8', 'replace')),
                'ISBN'          : str(self.ISBN),
                'state'     : str(self.howIsBook.encode('utf8', 'replace')),
                'price'         : float(self.price),
                'intent'        : str(self.intent.encode('utf8', 'replace'))
        }

    def getPicture(self):

        return base64.b64decode("")

class Course (models.Model):

    def __str__(self):
        return self.sigle + "( " + self.name.encode('utf8', 'replace') + " )"

    department  = models.ForeignKey('Department')

    name        = models.CharField(verbose_name   = "Nom du cours",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    sigle      = models.CharField(verbose_name   = "Sigle du cours",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du cours",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    def getJson(self):

        return json.dumps({
                'pk'            : str(self.pk),
                "name"          : str(self.name.encode('utf8', 'replace')),
                "sigle"         : str(self.sigle),
                "description"   : str(self.description.encode('utf8', 'replace'))
            })

class Department (models.Model):

    def __str__(self):
        return self.name

    etablishment= models.ForeignKey('Establishment')

    name        = models.CharField(verbose_name   = "Nom du Departement",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du departement",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)
    def getJson(self):

        return json.dump({
                'pk'            : str(self.pk),
                'name'          : str(self.name.encode('utf8', 'replace')),
                'description'   : str(self.description.encode('utf8', 'replace'))
            })

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

    def getJson(self):

        return json.dumps({
            'pk'            : str(self.pk),
            'name'          : str(self.name.encode('utf8', 'replace')),
            'street'        : str(self.street.encode('utf8', 'replace')),
            'city'          : str(self.city.encode('utf8', 'replace')),
            'zipCode'       : str(self.zipCode),
            'type'          : str(self.type.encode('utf8', 'replace')),
            'webSite'       : str(self.webSite)
        })

    def getStr(self):

        return {
            'pk'            : str(self.pk),
            'name'          : str(self.name.encode('utf8', 'replace')),
            'street'        : str(self.street.encode('utf8', 'replace')),
            'city'          : str(self.city.encode('utf8', 'replace')),
            'zipCode'       : str(self.zipCode),
            'type'          : str(self.type.encode('utf8', 'replace')),
            'webSite'       : str(self.webSite)
        }

class Account (models.Model):

    def __str__(self):
        return self.lastName.encode('utf8', 'replace') + ", " + self.firstName.encode('utf8', 'replace') + "( " + self.email + ") "

    department  = models.ForeignKey('Department')

    firstName   = models.CharField(verbose_name   = "Prenom de l'utilisateur",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    lastName    = models.CharField(verbose_name   = "Nom de l'utilisateur",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    email       = models.CharField(verbose_name   = "Email de l'utilisateur",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    phone       = models.CharField(verbose_name   = "Telephone de l'utilisateur",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    password    = models.CharField(verbose_name   = "Mot de passe du compte",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    faceBookID  = models.CharField(verbose_name   = "Identification FaceBook",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    googlePlusID = models.CharField(verbose_name   = "Identification Google Plus",
                                    max_length     = 100,
                                    null           = True,
                                    primary_key    = False,
                                    unique         = True)

    def getJson(self):

        return json.dumps({
            'pk'            : str(self.pk),
            'firstName'     : str(self.firstName.encode('utf8', 'replace')),
            'lastName'      : str(self.lastName.encode('utf8', 'replace')),
            'email'         : str(self.email),
            'phone'         : str(self.phone),
            'password'      : str(self.password.encode('utf8', 'replace')),
            'faceBookID'    : str(self.faceBookID.encode('utf8', 'replace')),
            'googlePlusID'  : str(self.googlePlusID.encode('utf8', 'replace'))
        })
