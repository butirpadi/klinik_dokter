from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post_mirror(self):
        self.action_post()
    
    def account_invoice_register_payment_mirror(self):
        self.account_invoice_register_payment()
