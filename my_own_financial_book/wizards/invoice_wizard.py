from odoo import models, fields
from odoo.exceptions import UserError

class FinInvoiceWizard(models.TransientModel):
    _name = "fin.invoice.wizard.pavlo"
    _description = "Financial Invoice Wizard"

    name = fields.Char(string="Invoice Type", required=True)

    date = fields.Date(string="Invoice Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))
    category = fields.Many2one(
        'invoice.category',
        string="Category",
        ondelete="cascade",
        default=lambda self: self.env.ref('my_own_financial_book.invoice_category_salary', raise_if_not_found=False)
    )

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
            "category": self.category.id if self.category else False,
            "book_id": book.id,
        })

        return {"type": "ir.actions.act_window_close"}