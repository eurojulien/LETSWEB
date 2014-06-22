from django.db import models
import json

# Livre
class Book (models.Model):

    title       = models.CharField(verbose_name   = "titre livre",
                                   name           = "titre",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    author      = models.CharField(verbose_name   = "auteur livre",
                                   name           = "auteur",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    edition     = models.CharField(verbose_name   = "edition livre",
                                   name           = "edition",
                                   max_length     = 50,
                                   null           = False,
                                   primary_key    = False)

    description = models.CharField(verbose_name   = "Description du livre",
                                   name           = "description",
                                   max_length     = 100,
                                   null           = True,
                                   primary_key    = False)

    ISBN        = models.CharField(verbose_name   = "ISBN livre",
                                   name           = "isbn",
                                   max_length     = 20,
                                   null           = True,
                                   primary_key    = False)

    price        = models.FloatField(verbose_name   = "Prix du livre",
                                    name           = "prix",
                                    default        = 0.00,
                                    null           = False,
                                    primary_key    = False)

    howIsBook   = models.CharField(verbose_name   = "Etat du livre",
                                   name           = "etat",
                                   max_length     = 100,
                                   null           = False,
                                   primary_key    = False)


    # codebarre
    # etablissementID
    # sigle
    # ownerID
    # picture
    # 

    # Format JSON
    def getJSON(self):

        return json.dumps({
                'titre'         : str(self.titre),
                'auteur'        : str(self.auteur),
                'edition'       : str(self.edition),
                'description'   : str(self.description),
                'ISBN'          : str(self.ISBN),
                'etatLivre'     : str(self.etatLivre),
                'prix'          : float(self.prix),

        })
# Create your models here.
