# -*- coding: utf-8 -*-
from odoo import models, fields


class InvoiceCategory(models.Model):
    _name = 'invoice.category'
    _description = 'Invoice Categories'

    name = fields.Char(
        string='Invoice Type',
        required=True,
    )