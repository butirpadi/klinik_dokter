from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_poli_product_category = fields.Boolean('Category for Poliklinik Product Service', default=False)

    