from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    hide_forecast_group = fields.Boolean('hide_forecast_group', default=True, compute='_compute_hide_forecast_group')
    
    def _compute_hide_forecast_group(self):
        for rec in self:
            rec.hide_forecast_group = self.env.user.has_group('exe_permission_custom.hide_forecast_group')