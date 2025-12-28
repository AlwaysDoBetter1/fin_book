from odoo import models, fields

class FinInvoiceWizard(models.TransientModel):
    _name = "fin.invoice.wizard.pavlo"
    _description = "Financial Invoice Wizard"

    name = fields.Char(string="Invoice Month", required=True)

    date = fields.Date(string="Invoice Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))

    def action_confirm(self):
        return True