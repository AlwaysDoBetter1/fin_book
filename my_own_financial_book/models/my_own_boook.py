from odoo import models, fields, api


class MyOwnFinbook(models.Model):
    _name = "fin.book.pavlo"
    _description = "My own Financial Book"

    name = fields.Char("Month", readonly=True)

    date = fields.Date("Date", readonly=True)

    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id,
    )

    expense_sum =fields.Monetary("Expense amount", currency_field="currency_id", compute="_compute_expense_sum")

    invoice_sum = fields.Monetary("Invoice amount", currency_field="currency_id", compute="_compute_invoice_sum")

    fin_invoices = fields.One2many("fin.invoice", "book_id", string="Invoices")

    fin_expenses = fields.One2many('fin.expense', 'book_id', string="Expenses")

    @api.depends('fin_expenses.amount')
    def _compute_expense_sum(self):
        for rec in self:
            rec.expense_sum = sum(rec.fin_expenses.mapped('amount'))

    @api.depends('fin_invoices.amount')
    def _compute_invoice_sum(self):
        for rec in self:
            rec.invoice_sum = sum(rec.fin_invoices.mapped('amount'))

    def create_invoice_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Add invoice",
            "res_model": "fin.expense.wizard.pavlo",
            "view_mode": "form",
            "target": "new",
            # "context": ctx,
        }

    def create_expense_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Add expense",
            "res_model": "fin.expense.wizard.pavlo",
            "view_mode": "form",
            "target": "new",
            # "context": ctx,
        }





