# -*- coding: utf-8 -*-
from odoo import http

class Firstaddons(http.Controller):
    @http.route('/firstaddons/firstaddons/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/firstaddons/firstaddons/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('firstaddons.listing', {
            'root': '/firstaddons/firstaddons',
            'objects': http.request.env['firstaddons.firstaddons'].search([]),
        })

    @http.route('/firstaddons/firstaddons/objects/<model("firstaddons.firstaddons"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('firstaddons.object', {
            'object': obj
        })