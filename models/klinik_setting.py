from odoo import api, fields, models


class KlinikSetting(models.Model):
    _name = 'klinik.setting'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    value = fields.Char('Value')

    