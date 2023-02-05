# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Board(models.AbstractModel):
    _inherit = 'board.board'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        user_dashboard = self.env.context.get('user_dashboard')
        if user_dashboard:
            self = self.with_env(self.env(user=user_dashboard))
        res = super(Board, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        return res
