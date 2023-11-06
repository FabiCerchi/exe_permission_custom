from odoo import models, fields, api
import logging

_logger = logging.getLogger("my-logger")

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    readonly_no_sale_admin = fields.Boolean('Readonly Group', compute="_compute_readonly_fields_groups")

    @api.depends('name')
    def _compute_readonly_fields_groups(self):
        for rec in self:
            rec.readonly_no_sale_admin = not self.env.user.has_group('sales_team.group_sale_manager')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    readonly_no_sale_admin = fields.Boolean('Readonly Group', default=False, compute='_compute_readonly_fields_groups')
    
    @api.depends('product_template_id')
    def _compute_readonly_fields_groups(self):
        for rec in self:
            rec.readonly_no_sale_admin = not self.env.user.has_group('sales_team.group_sale_manager')