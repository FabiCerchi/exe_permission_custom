from odoo import models, fields, api
import logging
from lxml import etree


_logger = logging.getLogger("my-logger")

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_only_supplier = fields.Boolean('Es Proveedor', compute="_compute_is_only_supplier", store=True)
    
    @api.depends('category_id')
    def _compute_is_only_supplier(self):
        for e in self:
            if len(e.category_id) > 0:
                e.is_only_supplier = any(category.is_supplier for category in e.category_id)
            else:
                e.is_only_supplier = False
    
    @api.onchange('category_id')
    def _onchange_category_id(self):
        self._compute_is_only_supplier()
        
    def search(self, args, offset=0, limit=None, order=None, count=False):
            group_hide_supplier = self.env.user.has_group('exe_permission_custom.hide_supplier')
            group_admin_ventas = self.env.user.has_group('sales_team.group_sale_manager')
            if group_hide_supplier or not group_admin_ventas:
                args.append(('is_only_supplier', '!=', True))

            # Llama al método search de la superclase
            return super(ResPartner, self).search(args, offset=offset, limit=limit, order=order, count=count)
    
class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    
    is_supplier = fields.Boolean('Es Proveedor', default=False)
    