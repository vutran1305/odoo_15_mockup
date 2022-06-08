from odoo import models, fields, api

class SubCat1(models.Model):
    _name = "sub.cat.1"
    name = fields.Char(string="Name")

