from odoo import models, fields

class LearningPlansPavlo(models.Model):
    _name = "learning.plans.pavlo"
    _description = "Plans of learning"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    comment = fields.Text("Comment")
    links = fields.Char("Links")

