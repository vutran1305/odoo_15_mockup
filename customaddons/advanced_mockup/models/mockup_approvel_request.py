


from odoo import models, fields, api



class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    full_name = fields.Char(string="Name")
    phone_number = fields.Char(string="Phone Number")
    province = fields.Char(string="Province/City")
    district = fields.Char(string="District")
    detail_address = fields.Char(string="Detail address")
    email = fields.Char(string="Email")
    image_1 = fields.Binary("Image 1")
    image_2 = fields.Binary("Image 2")
    image_3 = fields.Binary("Image 3")
    approvel_request_line = fields.One2many('approval.request.line', 'approval_request_id', string='approvel_request_line')







