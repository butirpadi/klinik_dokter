from odoo import models, fields, api


class Poli(models.Model):
    _name = 'res.poli'

    name = fields.Char(string='Name')
    color = fields.Integer(string="Color", default=0)
    product_id = fields.Many2one('product.template', string='Product')
    product_template_ids = fields.Many2many(
        comodel_name='product.template',
        relation='poli_product_template_rel',
        column1='poli_id',
        column2='product_id',
        string='Appointment Template'
    )

    @api.model
    def create(self, values):

        # create product of this poli on created
        new_prod = self.env['product.template'].create({
            'name': 'Pendaftaran ' + values['name'],
            'type': 'service',
            'categ_id': self.env['product.category'].search([('is_poli_product_category', '=', True)], limit=1).id,
            'sale_ok' : True,
            'purchase_ok' : False
        })
        values['product_id'] = new_prod.id

        result = super(Poli, self).create(values)

        result.write({
            'product_template_ids': [(4, new_prod.id)]
        })

        return result

    def unlink(self):

        link_product_id = self.product_id.id
        # delete product template
        self.env['product.template'].search(
                [('id', '=', link_product_id)]).unlink()

        result = super(Poli, self).unlink()


        return result
