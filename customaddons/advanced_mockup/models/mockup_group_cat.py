from odoo import models, fields, api

class GroupCat(models.Model):
    _name = "group.cat"

    name = fields.Char(string="Name")



