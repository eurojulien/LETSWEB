from django.db import models
import json
import base64

# Livre
class Book (models.Model):

    owner       = models.ForeignKey('Account')
    sigle       = models.ForeignKey('Department')

    title       = models.CharField(verbose_name   = "Titre du livre",
                                   name           = "Titre",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    author      = models.CharField(verbose_name   = "Auteur du livre",
                                   name           = "Auteur",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    edition     = models.CharField(verbose_name   = "Edition du livre",
                                   name           = "edition",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    description = models.CharField(verbose_name   = "Description du livre",
                                   name           = "description",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False)

    ISBN        = models.CharField(verbose_name   = "ISBN (Code a barre) du livre",
                                   name           = "ISBN",
                                   max_length     = 30,
                                   null           = True,
                                   primary_key    = False)

    price       = models.FloatField(verbose_name    = "Prix du livre",
                                    name            = "Prix",
                                    default         = 0.00,
                                    null            = False,
                                    primary_key     = False)

    howIsBook   = models.CharField(verbose_name   = "Etat du livre",
                                   name           = "Etat",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    intent      = models.CharField(verbose_name   = "Intention du vendeur",
                                   name           = "Intention",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)
    # picture

    # Format JSON
    def getJSON(self):

        return json.dumps({
                'title'         : str(self.titre),
                'author'        : str(self.author),
                'edition'       : str(self.edition),
                'description'   : str(self.description),
                'ISBN'          : str(self.ISBN),
                'howIsBook'     : str(self.howIsBook),
                'price'         : float(self.price),
                'intent'        : str(self.intetn)
        })

    def getPicture(self):

        return base64.b64decode("")

class Course (models.Model):

    department  = models.ForeignKey('Department')

    name        = models.CharField(verbose_name   = "Nom du cours",
                                   name           = "Nom",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    sigle      = models.CharField(verbose_name   = "Sigle du cours",
                                   name           = "Sigle",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du cours",
                                   name           = "Description",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    def getJson(self):

        return json.dumps({
                "name"          : self.name,
                "sigle"         : self.sigle,
                "description"   : self.description
            })

class Department (models.Model):

    etablishment= models.ForeignKey('Establishment')

    name        = models.CharField(verbose_name   = "Nom du Departement",
                                   name           = "Nom",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    description = models.CharField(verbose_name   = "Description du departement",
                                   name           = "Description",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)
    def getJson(self):

        return json.dump({
                'name'          : str(self.name),
                'description'   : str(self.description)
            })

# Etablissement scolaire
class Establishment (models.Model):

    name        = models.CharField(verbose_name   = "Nom de l'etablissement scolaire",
                                   name           = "Nom",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    street      = models.CharField(verbose_name   = "Numero et nom de la rue (Ex : 1100, Rue Notre-Dame)",
                                   name           = "Rue",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    city        = models.CharField(verbose_name   = "Nom de la ville de l'etablissement",
                                   name           = "Ville",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    zipCode     = models.CharField(verbose_name   = "Code postal de l'etablissement scolaire",
                                   name           = "Code Postal",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    type        = models.CharField(verbose_name   = "Type de l'etablissement scolaire",
                                   name           = "Type",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    webSite     = models.CharField(verbose_name   = "Site Web de l'etablissement scolaire",
                                   name           = "Site Web",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    def getJson(self):

        return json.dump({
            'name'          : str(self.name),
            'street'        : str(self.street),
            'city'          : str(self.city),
            'zipCode'       : str(self.zipCode),
            'type'          : str(self.type),
            'webSite'       : str(self.webSite)
        })

class Account (models.Model):

    department  = models.ForeignKey('Department')

    firstName   = models.CharField(verbose_name   = "Prenom de l'utilisateur",
                                   name           = "Prenom",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    lastName    = models.CharField(verbose_name   = "Nom de l'utilisateur",
                                   name           = "Nom",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)

    email       = models.CharField(verbose_name   = "Email de l'utilisateur",
                                   name           = "Adresse Email",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False,
                                   unique         = True)

    phone       = models.CharField(verbose_name   = "Telephone de l'utilisateur",
                                   name           = "Telephone",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    password    = models.CharField(verbose_name   = "Mot de passe du compte",
                                   name           = "Mot de passe",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    faceBookID  = models.CharField(verbose_name   = "Identification FaceBook",
                                   name           = "FaceBook",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False,
                                   unique         = True)

    googlePlusID = models.CharField(verbose_name   = "Identification Google Plus",
                                    name           = "Google Plus",
                                    max_length     = 100,
                                    null           = True,
                                    primary_key    = False,
                                    unique         = True)

    def getJson(self):

        return json.dump({
            'firstName'     : str(self.firstName),
            'lastName'      : str(self.lastName),
            'email'         : str(self.email),
            'phone'         : str(self.phone),
            'password'      : str(self.password),
            'faceBookID'    : str(self.faceBookID),
            'googlePlusID'  : str(self.googlePlusID)
        })
