from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Product(models.Model):
    _inherit = 'product.template'

    poli_id = fields.Many2one(
        comodel_name='res.poli',
        string='Poliklinik'
    )
