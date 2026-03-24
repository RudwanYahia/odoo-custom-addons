from odoo import models, fields

class Customer(models.Model):
    _name = 'custom.customer'

    name = fields.Char()
    email = fields.Char()
