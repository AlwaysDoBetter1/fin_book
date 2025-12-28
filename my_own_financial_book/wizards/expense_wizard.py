from odoo import models, fields
from odoo.exceptions import UserError

class FinExpenseWizard(models.TransientModel):
    _name = "fin.expense.wizard.pavlo"
    _description = "Financial Expense Wizard"

    name = fields.Char(string="Expense Month", required=True)

    date = fields.Date(string="Expense Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))

    def action_confirm(self):
        self.ensure_one()

        book_id = self.env.context.get("active_id")
        if not book_id:
            raise UserError("Financial Book not found in context")

        book = self.env["fin.book.pavlo"].browse(book_id)
        if not book.exists():
            raise UserError("Financial Book does not exist")

        self.env["fin.expense"].create({
            "name": self.name,
            "date": self.date,
            "amount": self.amount,
            "book_id": book.id,
        })

        return {"type": "ir.actions.act_window_close"}