from odoo import models, fields, api


class MyOwnFinbook(models.Model):
    _name = "fin.book.pavlo"
    _description = "My own Financial Book"

    name = fields.Char("Month", readonly=True)

    date = fields.Date("Date", readonly=True)

    expense_sum =fields.Float("Expense amount", compute="_compute_expense_sum")

    invoice_sum = fields.Float("Invoice amount", compute="_compute_invoice_sum")

    total = fields.Float("Total", compute="_compute_total")

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

    @api.depends('invoice_sum', 'expense_sum')
    def _compute_total(self):
        for rec in self:
            rec.total = (rec.invoice_sum or 0.0) - (rec.expense_sum or 0.0)

    def create_invoice_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Add invoice",
            "res_model": "fin.invoice.wizard.pavlo",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_name": self.name,
                "active_id": self.id,
            },
        }

    def create_expense_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Add expense",
            "res_model": "fin.expense.wizard.pavlo",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_name": self.name,
                "active_id": self.id,
            },
        }





