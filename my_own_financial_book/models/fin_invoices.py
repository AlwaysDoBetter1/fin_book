from odoo import models, fields


class FinInvoice(models.Model):
    _name = "fin.invoice"
    _description = "Financial Invoice"

    name = fields.Char(string="Invoice Number", required=True)

    book_id = fields.Many2one(
        "fin.book.pavlo",
        "Financial Book",
        ondelete="cascade"
    )

    date = fields.Date(string="Invoice Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", digits=(16, 2))
    category = fields.Many2one('invoice.category', string="Category", ondelete="cascade")
