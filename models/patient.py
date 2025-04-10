from odoo import models, fields, api

class Patient(models.Model):
    _name = "clinicbelen.patient"
    _description = "clinicbelen.patient"
    _inherit = "clinicbelen.client"  # Herencia de la clase Client

    medical_history = fields.Text(string="Historia Médica")
    treatments = fields.One2many("clinicbelen.treatment", "patient", string="Tratamientos")

