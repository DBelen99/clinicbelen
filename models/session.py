from odoo import models, fields, api


class Session(models.Model):
    _name= "clinicbelen.session"
    _description = "clinicbelen.session"

    id = fields.Integer()
    name = fields.Char(required = True, string="Nombre")
    description = fields.Text(string="Descripción")
    date = fields.Date(string="Fecha")

    # Un tratamiento puede tener varias sesiones y cada sesión tiene un único tratamiento
    treatment = fields.Many2one("clinicbelen.treatment", ondelete = "CASCADE", string="Tratamientos")

    # En cada sesión hay varias técnicas y una técnica aparece en varias sesiones
    techniques = fields.Many2many("clinicbelen.technique", relation = "technique_session", column1="techniques", column2="sessions", string="Técnicas")

    professional = fields.Many2one("clinicbelen.professional", ondelete="CASCADE", string="Profesional", related="treatment.professional",readonly=True)

    # def _get_professional(self):
    #     for session in self:
    #         session.professional = session.treatment.professional