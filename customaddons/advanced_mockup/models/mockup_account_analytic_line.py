from odoo import models, fields, api



class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    drawing = fields.Char(string="Drawing")
    start_date = fields.Datetime(string="Start date",default=fields.Datetime.now())
    end_date = fields.Datetime(string="End date",default=fields.Datetime.now())
    activities = fields.Char(string="Activities", default="Draw")
    quantity = fields.Float(string="Quantity",default=0)


