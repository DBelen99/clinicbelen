from odoo import models, fields, api


class Client(models.Model):
    _name= "clinicbelen.client"
    _description = "clinicbelen.client"

    id = fields.Integer()
    name = fields.Char(required = True, )
    surname = fields.Char(required = True, string="Apellidos")
    birthdate = fields.Date(string="Fecha de Nacimiento")
    phone = fields.Integer(string="Nº de Teléfono")
    email = fields.Text(string="Correo Electrónico")
    direction = fields.Text(string="Dirección")

    # Un cliente puede tener varios registros y un registro solo puede tener un cliente
    registers = fields.One2many(string="Registros", comodel_name="clinicbelen.register", inverse_name = "client", readonly=True)
