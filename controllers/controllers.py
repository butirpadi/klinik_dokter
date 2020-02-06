# -*- coding: utf-8 -*-
from odoo import http

# class KlinikDokter(http.Controller):
#     @http.route('/klinik_dokter/klinik_dokter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/klinik_dokter/klinik_dokter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('klinik_dokter.listing', {
#             'root': '/klinik_dokter/klinik_dokter',
#             'objects': http.request.env['klinik_dokter.klinik_dokter'].search([]),
#         })

#     @http.route('/klinik_dokter/klinik_dokter/objects/<model("klinik_dokter.klinik_dokter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('klinik_dokter.object', {
#             'object': obj
#         })