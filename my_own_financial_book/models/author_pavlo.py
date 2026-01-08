from odoo import models, fields


class AuthorPavlo(models.Model):
    _name = "author.pavlo"
    _description = "Author"

    name = fields.Char("Name", required=True)
    bio = fields.Text("Biography")

