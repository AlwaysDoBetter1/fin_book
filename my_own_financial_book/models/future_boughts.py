from odoo import models, fields

class FutureBoughtsPavlo(models.Model):
    _name = "future.boughts.pavlo"
    _description = "Future purchases"

    name = fields.Char("Name", required=True)
    author_id = fields.Many2one(
        "author.pavlo",
        string="Author",
        required=True,
        default=lambda self: self.env["author.pavlo"].search([("name", "=", "Pavlo")], limit=1)
    )
    comment = fields.Text("Comment")
    links = fields.Char("Links")

