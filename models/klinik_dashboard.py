from odoo import models, fields, api, _
from odoo.exceptions import UserError


class KlinikDashboard(models.Model):
    _name = 'klinik.dashboard'

    name = fields.Char(
        string='Name',
    )
    poli_id = fields.Many2one(
        comodel_name='res.poli',
        string='Poliklinik'
    )
    registered = fields.Integer(
        string='Terdaftar',
    )
    next_sequence = fields.Integer(
        string='Next Sequence',
    )
    color = fields.Integer(
        string='Color',
    )

    def reset_seq(self):
        self.write({
            'registered': 0,
            'next_sequence': 1
        })

    def get_next_sequence(self):
        next_seq = self.next_sequence
        self.write({
            'next_sequence': next_seq+1
        })
        return next_seq
