#!/usr/bin/env python
# -*- coding: cp1252 -*-

from django.db import models
import json
import base64

# Catalogue de description de livres
class BookDescription (models.Model):

    def __str__(self):
        return  self.title.encode('utf8', 'replace') + "( " + self.editionNo + " )"

    title       = models.CharField(verbose_name             = "Titre",
                                   max_length               = 100)

    author      = models.CharField(verbose_name             = "Auteur(s)",
                                   max_length               = 100)

    editionNo   = models.PositiveSmallIntegerField(verbose_name     = "Numero d'edition")

    editor      = models.CharField(verbose_name     = "Editeur(s)",
                                   max_length               = 100)

    pubYear     = models.PositiveSmallIntegerField(verbose_name     = "Annee de publication")

    oriLan      = models.CharField(verbose_name             = "Langue originale",
                                   max_length               = 50)

    traLan      = models.CharField(verbose_name             = "Langue traduite",
                                   max_length               = 50)

    nbPages     = models.PositiveSmallIntegerField(verbose_name     = "Nombre de pages")

    ISBN        = models.CharField(verbose_name             = "ISBN",
                                   max_length               = 50)

    survey      = models.CharField(verbose_name             = "Resume/Description",
                                   max_length               = 1000)