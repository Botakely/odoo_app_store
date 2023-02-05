# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    board_group_ids = fields.One2many('board.group', 'owner_id', string='Board group')

    def create_board_group(self):
        for rec in self:
            BoadGroup = self.env['board.group']
            BoadGroup.with_context(is_main_dashboard=True).create({
                'name': 'My dashboard',
                'owner_id': rec.id,
                'is_main_dashboard': True,
                'act_window_id': BoadGroup._create_act_window(rec.id).id
            })

    @api.model
    def create(self, values):
        res = super(ResUsers, self).create(values)
        if not res.share:
            res.sudo().create_board_group()
        return res