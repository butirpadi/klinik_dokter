from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rm_no = fields.Char('Medical Record Number', default="New")
    is_patient = fields.Boolean(string='Is Patient', default=False)
    tempat_lahir = fields.Char('Tempat Lahir')
    tanggal_lahir = fields.Date('Tanggal Lahir')
    usia = fields.Char('Usia', compute="_compute_usia", store=True,)
    sex = fields.Selection([('m', 'Laki-laki'), ('f', 'Perempuan')], string="Sex")
    blood_type = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
                                   ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], string="Golongan Darah")

    @api.depends('tanggal_lahir')
    def _compute_usia(self):
        for rec in self:
            if rec.tanggal_lahir:
                d1 = rec.tanggal_lahir
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.usia = str(rd.years) + "y" + " " + \
                    str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.usia = "No Date Of Birth!!"

    @api.model
    def create(self, values):

        if 'is_patient' in values:
            values['rm_no'] = self.env['ir.sequence'].next_by_code(
                'pasien.register.sequence') or _('New')

        result = super(ResPartner, self).create(values)

        return result

    def name_get(self):
        # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
        self.browse(self.ids).read(['name', 'rm_no'])
        return [(template.id, '%s%s' % (template.rm_no and '[%s] ' % template.rm_no or '', template.name))
                for template in self]
