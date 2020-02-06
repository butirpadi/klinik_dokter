from odoo import models, fields, api


class ProductQueueListRel(models.Model):
    _name = 'product.queue.list.rel'

    product_id = fields.Many2one('product.template', string='Product')
    queue_list_id = fields.Many2one('queue.list', string='Queue List')
    next_sequence = fields.Integer('Next Sequence', default=1)

    def get_next_seq(self):

        next_seq = self.next_sequence + 1
        self.write({
            'next_sequence': next_seq
        })
        
        return next_seq
