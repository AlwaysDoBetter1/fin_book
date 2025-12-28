from odoo import models, fields
from odoo.exceptions import UserError

class FinInvoiceWizard(models.TransientModel):
    _name = "fin.invoice.wizard.pavlo"
    _description = "Financial Invoice Wizard"

    name = fields.Char(string="Invoice Month", required=True)

    date = fields.Date(string="Invoice Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))

    def action_confirm(self):
        book_id = self.env.context.get("active_id")
        if not book_id:
            raise UserError("Financial Book not found in context")

        book = self.env["fin.book.pavlo"].browse(book_id)
        if not book.exists():
            raise UserError("Financial Book does not exist")

        self.env["fin.invoice"].create({
            "name": self.name,
            "date": self.date,
            "amount": self.amount,
            "book_id": book.id,
        })

        return {"type": "ir.actions.act_window_close"}