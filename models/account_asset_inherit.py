from odoo import fields, models, api


class AccountAsset(models.Model):
    _inherit = 'account.asset'
    _description = 'Account Asset inherit'

    sequence_name = fields.Char(string='Asset Sequence', default='New')

    @api.onchange('model_id')
    def _onchange_model_id(self):
        self.name = self.model_id.sequence_name
        res = super(AccountAsset, self)._onchange_model_id()
        return res

    @api.model
    def create(self, vals):
        vals['sequence_name'] = self.env['ir.sequence'].next_by_code('asset.seq') or 'New'
        result = super(AccountAsset, self).create(vals)
        return result

