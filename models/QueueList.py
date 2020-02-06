from odoo import models, fields, api
from odoo.exceptions import UserError


class QueueList(models.Model):
    _name = 'queue.list'

    name = fields.Char('Name')
    tanggal = fields.Date(string='Tanggal', default=fields.Date.today())
    state = fields.Selection(
        [("open", "Open"), ("lock", "Lock")], string='State', default='open')

    @api.model
    def create(self, values):

        # check tanggal yang sama
        qls = self.env['queue.list'].search(
            [('tanggal', '=', values['tanggal'])])
        if len(qls) > 0:
            raise UserError('Data Queue List dengan tanggal "' +
                            values['tanggal'] + '" telah tersedia.')
        else:
            result = super(QueueList, self).create(values)

            result.write({
                'name': 'QL' + str(result.tanggal.day) + str(result.tanggal.month) + str(result.tanggal.year)
            })

            self.env.cr.execute(
                "update queue_list set state = 'lock' where id != " + str(result.id))

            return result

    def action_lock(self):
        self.write({
            'state': 'lock'
        })

    def action_reset(self):
        self.write({
            'state': 'open'
        })
        self.env.cr.execute(
            "update queue_list set state = 'lock' where id != " + str(self.id))
