from odoo import models, fields


class MyOwnFinbook(models.Model):
    _name = "fin.book.pavlo"
    _description = "My own Financial Book"

    name = fields.Char("Name", required=True)




