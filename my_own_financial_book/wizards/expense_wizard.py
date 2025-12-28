from odoo import models, fields

class FinExpenseWizard(models.TransientModel):
    _name = "fin.expense.wizard.pavlo"
    _description = "Financial Expense Wizard"

    name = fields.Char(string="Expense Month", required=True)

    date = fields.Date(string="Expense Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))

    def action_confirm(self):
        return True