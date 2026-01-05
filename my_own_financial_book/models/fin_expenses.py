from odoo import models, fields


class FinExpense(models.Model):
    _name = "fin.expense"
    _description = "Financial Expense"

    name = fields.Char(string="Expense Description", required=True)

    book_id = fields.Many2one(
        "fin.book.pavlo",
        string="Financial Book",
        ondelete="cascade",
    )

    date = fields.Date(string="Expense Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))
    category = fields.Many2one('expense.category', string="Category", ondelete="cascade")
