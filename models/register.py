from odoo import models, fields, api


class Register(models.Model):
    _name= "clinicbelen.register"
    _description = "clinicbelen.register"

    id = fields.Integer()
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")

    
    # Un cliente puede tener varios registros y un registro solo puede tener un cliente
    client = fields.Many2one("clinicbelen.client", ondelete="CASCADE", string="Cliente")

    # Un registro puede tener varios tratamientos y un tratamiento tiene un solo registro
    treatments = fields.One2many(comodel_name="clinicbelen.treatment", inverse_name = "register", string="Tratamientos")