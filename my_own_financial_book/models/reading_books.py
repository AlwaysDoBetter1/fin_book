from odoo import models, fields


class Readingbook(models.Model):
    _name = "reading.book.pavlo"
    _description = "Model for reading books"

    name = fields.Char("Name", required=True)



