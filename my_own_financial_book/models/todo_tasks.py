from odoo import models, fields

class TodoTasksPavlo(models.Model):
    _name = "todo.tasks.pavlo"
    _description = "#ToDo tasks"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    comment = fields.Text("Comment")
    links = fields.Char("Links")

