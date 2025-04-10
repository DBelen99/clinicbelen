from odoo import models, fields, api


class Treatment(models.Model):
    _name= "clinicbelen.treatment"
    _description = "clinicbelen.treatment"

    id = fields.Integer()
    name = fields.Char(required = True, string="Nombre", compute = "_get_name")
    description = fields.Text(string="Descripción")
    initdate = fields.Datetime(string="Fecha de Inicio")
    enddate = fields.Datetime(string="Fecha de Fin")

    # Un registro puede tener varios tratamientos y un tratamiento tiene un solo registro
    register = fields.Many2one("clinicbelen.register", ondelete = "CASCADE", string="Registro")

    # Un tratamiento puede tener varias sesiones y cada sesión tiene un único tratamiento
    sessions = fields.One2many(comodel_name="clinicbelen.session", inverse_name = "treatment", string="Sesiones")

    # Un profesional puede desarrollar varios tratamientos y un tratamiento está a cargo de un único profesional
    professional = fields.Many2one("clinicbelen.professional", ondelete = "CASCADE", string="Profesional")

    # Un paciente puede tener varios tratamientos y un tratamiento está asociado a un único paciente
    patient = fields.Many2one("clinicbelen.patient", ondelete="CASCADE", string="Paciente")

    @api.depends("register.name", "register.client.name") 
    def _get_name(self): 
        for treatment in self: 
            if treatment.register.client and treatment.register:
                treatment.name=f"{treatment.register.client.name} - {treatment.register.name}"
            else:
                treatment.name="Tratamiento sin nombre"