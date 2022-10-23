from odoo import fields, models, api


class AccountAsset(models.Model):
    _inherit = 'account.asset'
    _description = 'Account Asset inherit'

    sequence_id = fields.Many2one('ir.sequence', string='Sequence', domain=[('is_active', '=', True)])
    code = fields.Char(string='Code')

    @api.onchange('sequence_id')
    def _active_model(self):
        self.sequence_id.is_active = True

    @api.onchange('model_id')
    def _sequence_for_asset(self):
        self.code = self.env['ir.sequence'].next_by_code(self.sequence_id.code)
