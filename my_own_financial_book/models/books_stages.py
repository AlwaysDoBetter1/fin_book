# -*- coding: utf-8 -*-
from odoo import models, fields


class BooksStage(models.Model):
    _name = 'books.stage'
    _description = 'Books Stage'
    _order = 'sequence, id'

    name = fields.Char(
        string='Stage Name',
        required=True,
        translate=True,
    )

    sequence = fields.Integer(
        default=10,
        help='Stage order',
    )

    fold = fields.Boolean(
        string='Folded in Kanban',
        default=False,
    )

    active = fields.Boolean(
        default=True,
    )

    color = fields.Integer()

    description = fields.Text()

