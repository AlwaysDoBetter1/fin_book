from odoo import models, fields

class TodoTasksPavlo(models.Model):
    _name = "todo.tasks.pavlo"
    _description = "#ToDo tasks"

    name = fields.Char("Name", required=True)
    author_id = fields.Many2one(
        "author.pavlo",
        string="Author",
        required=True,
        default=lambda self: self.env["author.pavlo"].search([("name", "=", "Pavlo")], limit=1)
    )
    status = fields.Selection(
        selection=[
            ('pending', 'Pending'),
            ('done', 'Done'),
        ],
        string="Status",
        default='pending',
        required=True,
    )
    comment = fields.Text("Comment")
    links = fields.Char("Links")

