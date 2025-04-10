# -*- coding: utf-8 -*-
# from odoo import http


# class Clinicbelen(http.Controller):
#     @http.route('/clinicbelen/clinicbelen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinicbelen/clinicbelen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinicbelen.listing', {
#             'root': '/clinicbelen/clinicbelen',
#             'objects': http.request.env['clinicbelen.clinicbelen'].search([]),
#         })

#     @http.route('/clinicbelen/clinicbelen/objects/<model("clinicbelen.clinicbelen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinicbelen.object', {
#             'object': obj
#         })

