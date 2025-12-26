from odoo import models, fields

class FuturePlansPavlo(models.Model):
    _name = "future.plans.pavlo"
    _description = "Model for reading books"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    comment = fields.Text("Comment")
    links = fields.Char("Links")