from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AppointmentOrder(models.Model):
    _name = 'appointment.order'

    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Pasien', domain=[('is_patient','=',True)])
    appointment_date = fields.Datetime(string="Tanggal")
    

    