from odoo import models, fields, api

class ModelCat(models.Model):
    _name = 'model.cat'
    name = fields.Char(string="Name")
    group_cat_id = fields.Many2one("group.cat", string="Group cat")
