# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CreateMenuDashboard(models.TransientModel):
    _name = 'create.menu.dashboard'
    _description = 'Create Menu Wizard'

    menu_id = fields.Many2one('ir.ui.menu', string='Parent Menu', required=True, ondelete='cascade')
    name = fields.Char(string='Menu Name', required=True)
    board_group_id = fields.Many2one('board.group', required=True)
    sequence = fields.Integer(default=-1)
    sibling_menu_ids = fields.Many2many('ir.ui.menu', compute='compute_sibling_menu_ids')

    def menu_create(self):
        self.ensure_one()
        self = self.sudo()
        action_id = self.board_group_id.act_window_id.id
        menu_id = self.env['ir.ui.menu'].create({
            'name': self.name,
            'parent_id': self.menu_id.id,
            'action': 'ir.actions.act_window,%d' % (action_id,),
            'sequence': self.sequence
        })
        self.board_group_id.write({'menu_ids': [(4, menu_id.id)]})
        return {'type': 'ir.actions.act_window_close'}

    @api.depends('menu_id')
    def compute_sibling_menu_ids(self):
        for rec in self:
            rec.sibling_menu_ids = [(6, 0, rec.menu_id.child_id.ids)]