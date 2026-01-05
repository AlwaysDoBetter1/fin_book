# -*- coding: utf-8 -*-
from odoo import models, fields


class ExpenseCategory(models.Model):
    _name = 'expense.category'
    _description = 'Expense Categories'

    name = fields.Char(
        string='Expense Type',
        required=True,
    )