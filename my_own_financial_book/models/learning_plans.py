from odoo import models, fields

class LearningPlansPavlo(models.Model):
    _name = "learning.plans.pavlo"
    _description = "Plans of learning"

    name = fields.Char("Name", required=True)
    author_id = fields.Many2one(
        "author.pavlo",
        string="Author",
        required=True,
        default=lambda self: self.env["author.pavlo"].search([("name", "=", "Pavlo")], limit=1)
    )
    comment = fields.Text("Comment")
    links = fields.Char("Links")

