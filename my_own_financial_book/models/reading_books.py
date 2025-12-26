from odoo import models, fields

class Readingbook(models.Model):
    _name = "reading.book.pavlo"
    _description = "Model for reading books"

    name = fields.Char("Name", required=True)
    author = fields.Char("Author", required=True)
    comment = fields.Text("Comment")
    links = fields.Char("Links")

    books_stages = fields.Many2one(
        'books.stage',
        string="Books Stage",
        default=lambda self: self.env.ref(
            'my_own_financial_book.stage_1', raise_if_not_found=False
        ),
        group_expand="_group_expand_candidate_stage",
    )

    def _group_expand_candidate_stage(self, stages, domain):
        return self.env["books.stage"].search([], order="sequence asc")



