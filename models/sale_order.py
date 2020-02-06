from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pprint


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rm_no = fields.Char(related='partner_id.rm_no', store=True)
    poli_id = fields.Many2one('res.poli', string='Poliklinik')
    is_appointment_order = fields.Boolean(
        'Is Appointment Order', default=False)

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        # add antrian ke poli
        if self.is_appointment_order:
            self.poli_id.write({
                'jumlah_antrian': self.poli_id.jumlah_antrian+1
            })

        return res

    @api.model
    def create(self, values):

        result = super(SaleOrder, self).create(values)

        return result

    @api.onchange('poli_id')
    def poli_onchange(self):
        # unlkink product from last data
        if len(self.order_line) > 0:
            self.order_line = [(5, False, False)]

        # add product
        order_line_prd = []
        for prod in self.poli_id.product_template_ids:

            prd_desc = prod.description_sale
            if not prod.description_sale:
                prd_desc = prod.name

            order_line_prd.append((0, 0, {
                'product_id': prod.id,
                'product_template_id': prod.id,
                'name': prd_desc,
                'product_uom': 1,
                'product_uom_qty': 1,
                'price_unit': prod.list_price,
            }))

        self.order_line = order_line_prd
