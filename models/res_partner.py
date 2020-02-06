from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rm_no = fields.Char('Medical Record Number', default="New")
    is_patient = fields.Boolean(string='Is Patient', default=False)

    @api.model
    def create(self, values):

        if 'is_patient' in values :
            values['rm_no'] = self.env['ir.sequence'].next_by_code(
                'pasien.register.sequence') or _('New')        

        result = super(ResPartner, self).create(values)

        return result

    def name_get(self):
        # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
        self.browse(self.ids).read(['name', 'rm_no'])
        return [(template.id, '%s%s' % (template.rm_no and '[%s] ' % template.rm_no or '', template.name))
                for template in self]
