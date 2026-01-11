from odoo import models, fields, api

class ExpensiveBoughtsPavlo(models.Model):
    _name = "expensive.boughts.pavlo"
    _description = "Expensive purchases"

    name = fields.Char("Name", required=True)
    author_id = fields.Many2one(
        "author.pavlo",
        string="Author",
        required=True,
        default=lambda self: self.env["author.pavlo"].search([("name", "=", "Pavlo")], limit=1)
    )
    price = fields.Float("Price", digits=(16, 2))
    paid = fields.Float("Paid", digits=(16, 2))
    remaining = fields.Float(
        "Remaining",
        digits=(16, 2),
        compute="_compute_remaining",
        store=True,
        help="Remaining amount to pay (Price - Paid)"
    )
    is_active = fields.Boolean("Active", default=False)
    months_planned = fields.Integer(string="Planned Months", required=True, default=12)
    comment = fields.Text("Comment")
    links = fields.Char("Links")

    @api.depends("price", "paid")
    def _compute_remaining(self):
        for record in self:
            record.remaining = (record.price or 0.0) - (record.paid or 0.0)
