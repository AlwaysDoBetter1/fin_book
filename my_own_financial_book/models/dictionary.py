from odoo import models, fields


class EnglishDictionary(models.Model):
    _name = "english.dictionary"
    _description = "English Dictionary"

    name = fields.Char(string="Word", required=True)

    transcription = fields.Char(string="Transcription")

    translation = fields.Char(string="Translation")




