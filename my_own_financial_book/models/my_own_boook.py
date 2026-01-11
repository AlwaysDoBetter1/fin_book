from odoo import models, fields, api


class MyOwnFinbook(models.Model):
    _name = "fin.book.pavlo"
    _description = "My own Financial Book"

    name = fields.Char("Month")

    date = fields.Date("Date", readonly=True)

    expense_sum =fields.Float("Expense amount", compute="_compute_expense_sum")

    invoice_sum = fields.Float("Invoice amount", compute="_compute_invoice_sum")

    total = fields.Float("Total", compute="_compute_total")

    manual_amount = fields.Float("Manual Amount", digits=(16, 2), default=0.0)

    total_with_manual = fields.Float("Total with Manual", compute="_compute_total_with_manual")

    fin_invoices = fields.One2many("fin.invoice", "book_id", string="Invoices")

    fin_expenses = fields.One2many('fin.expense', 'book_id', string="Expenses")

    expensive_goals_remaining = fields.Float("Expensive Goals Remaining", compute="_compute_expensive_goals_remaining")

    month_should_paid = fields.Float("Monthly Planned Payment", digits=(16, 2), compute="_compute_month_should_paid")

    this_month_paid = fields.Float("This Month Paid (Expensive Goals)", digits=(16, 2), compute="_compute_this_month_paid")

    debt = fields.Float("Debt (Paid - Planned)", digits=(16, 2), compute="_compute_debt")

    expense_chart = fields.Char("Expense Chart", compute="_compute_expense_chart")

    comment = fields.Text("Comment")

    @api.depends('fin_expenses.amount')
    def _compute_expense_sum(self):
        for rec in self:
            rec.expense_sum = -sum(rec.fin_expenses.mapped('amount'))

    @api.depends('fin_invoices.amount')
    def _compute_invoice_sum(self):
        for rec in self:
            rec.invoice_sum = sum(rec.fin_invoices.mapped('amount'))

    @api.depends('invoice_sum', 'expense_sum')
    def _compute_total(self):
        for rec in self:
            rec.total = (rec.invoice_sum or 0.0) + (rec.expense_sum or 0.0)

    @api.depends('total', 'manual_amount')
    def _compute_total_with_manual(self):
        for rec in self:
            rec.total_with_manual = (rec.total or 0.0) + (rec.manual_amount or 0.0)

    @api.depends_context('uid')
    def _compute_expensive_goals_remaining(self):
        ExpensiveBoughts = self.env['expensive.boughts.pavlo']
        for rec in self:
            active_goals = ExpensiveBoughts.search([('is_active', '=', True)])
            rec.expensive_goals_remaining = sum(active_goals.mapped('remaining'))

    @api.depends_context('uid')
    def _compute_month_should_paid(self):
        ExpensiveBoughts = self.env['expensive.boughts.pavlo']
        for rec in self:
            active_goals = ExpensiveBoughts.search([('is_active', '=', True)])
            total_monthly = 0.0
            for goal in active_goals:
                months = goal.months_planned or 1
                total_monthly += (goal.price or 0.0) / months
            rec.month_should_paid = round(total_monthly, 2)

    @api.depends('fin_expenses.amount', 'fin_expenses.category')
    def _compute_this_month_paid(self):
        for rec in self:
            cat = self.env.ref('my_own_financial_book.expense_category_expensive_goals', raise_if_not_found=False)
            if not cat:
                rec.this_month_paid = 0.0
                continue
            expenses = rec.fin_expenses.filtered(lambda e: e.category and e.category.id == cat.id)
            rec.this_month_paid = round(sum(expenses.mapped('amount')), 2)

    @api.depends('this_month_paid', 'month_should_paid')
    def _compute_debt(self):
        for rec in self:
            # base debt for the current record
            base_debt = (rec.this_month_paid or 0.0) - (rec.month_should_paid or 0.0)
            # sum base debts of all previous records by create_date
            prev_recs = self.search([('create_date', '<', rec.create_date)]) if rec.create_date else self.browse()
            prev_base_total = 0.0
            for prev in prev_recs:
                prev_base_total += (prev.this_month_paid or 0.0) - (prev.month_should_paid or 0.0)
            rec.debt = round(base_debt + prev_base_total, 2)

    def create_invoice_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Add invoice",
            "res_model": "fin.invoice.wizard.pavlo",
            "view_mode": "form",
            "target": "new",
            "context": {
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
                "active_id": self.id,
            },
        }

    @api.depends('fin_expenses')
    def _compute_expense_chart(self):
        # Dummy compute to trigger widget rendering
        for rec in self:
            rec.expense_chart = "chart"
