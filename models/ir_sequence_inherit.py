from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'ir.sequence'
    _description = 'Sequence Inherit'

    is_active = fields.Boolean()
