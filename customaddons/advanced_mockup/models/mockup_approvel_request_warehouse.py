
from odoo import models, fields, api



class ApprovalRequestLine(models.Model):
    _name = 'approval.request.line'
    warehouse = fields.Char(string="Warehouse")
    phone_number = fields.Char(string="Phone number")
    approval_request_id = fields.Many2one('approval.request')
    province = fields.Char(string="Province/City")
    district = fields.Char(string="District")
    detail_address = fields.Char(string="Detail address")

