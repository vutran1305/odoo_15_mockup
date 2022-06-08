
from odoo import models, fields, api

class ProductTemplateihr(models.Model):
    _inherit = 'product.template'
    group_cat = fields.Many2one("group.cat", string="Group cat")
    sub_cat_1 = fields.Many2one("sub.cat.1", string="Sub cat 1")
    sub_cat_2 = fields.Many2one("sub.cat.2", string="Sub cat 2")
    cat = fields.Many2one("model.cat", string="Cat")
    spec_1 = fields.Char(string="SPEC-1")
    spec_2 = fields.Char(string="SPEC-2")
    spec_3 = fields.Char(string="SPEC-3")
    spec_4 = fields.Char(string="SPEC-4")
    spec_5 = fields.Char(string="SPEC-5")
    spec_6 = fields.Char(string="SPEC-6")
    spec_7 = fields.Char(string="SPEC-7")
    spec_8 = fields.Char(string="SPEC-8")

