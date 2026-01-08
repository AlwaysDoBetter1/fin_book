from odoo import models, fields

class FutureBoughtsPavlo(models.Model):
    _name = "future.boughts.pavlo"
    _description = "Future purchases"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    comment = fields.Text("Comment")
    links = fields.Char("Links")

