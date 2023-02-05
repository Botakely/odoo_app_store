# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BoardGroup(models.Model):
    _name = 'board.group'

    name = fields.Char(required=True)
    act_window_id = fields.Many2one('ir.actions.act_window')
    user_ids = fields.Many2many('res.users', string='Share with', domain="[('id', '!=', owner_id)]")
    owner_id = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.uid, readonly=True)
    is_main_dashboard = fields.Boolean()
    is_my_main_dashboard = fields.Boolean(compute='compute_is_my_main_dashboard')
    menu_ids = fields.Many2many('ir.ui.menu')

    @api.model
    def fetch_user_dashboard(self):
        return self.search_read([('owner_id', '=', self.env.user.id)], ['id', 'name', 'is_main_dashboard'])

    @api.model
    def init_board_group(self):
        self.env['res.users'].search([('board_group_ids', '=', False)]).create_board_group()

    @api.model
    def _create_act_window(self, uid=None):
        board_view_id = self.env.ref('board.board_my_dash_view').copy()
        return self.env.ref('board.open_board_my_dash_action').copy({
            'name': _('Dashboard'),
            'view_id': board_view_id.id,
            'context': {'user_dashboard': uid or self.env.uid}
        })

    @api.model
    def create(self, values):
        if not self.env.context.get('is_main_dashboard'):
            values['act_window_id'] = self.sudo()._create_act_window().id
        return super(BoardGroup, self).create(values)

    def unlink(self):
        for rec in self:
            if rec.is_my_main_dashboard:
                raise UserError('You can\'t delete a main dashboard')
            rec.menu_ids.sudo().unlink()
            rec.act_window_id.view_id.sudo().unlink()
            rec.act_window_id.sudo().unlink()
        return super(BoardGroup, self).unlink()

    def open_board_group(self):
        self.ensure_one()
        action = self.act_window_id.read()[0]
        if self.act_window_id == self.env.ref('board.open_board_my_dash_action'):
            action['context'] = {'user_dashboard': self.owner_id.id}
        return action

    @api.depends('is_main_dashboard', 'owner_id')
    def compute_is_my_main_dashboard(self):
        for rec in self:
            rec.is_my_main_dashboard = rec.is_main_dashboard and rec.owner_id == self.env.user

    @api.model
    def _get_main_dashboard(self):
        return self.search([('owner_id', '=', self.env.user.id), ('is_main_dashboard', '=', True)], limit=1)

    def set_as_main_dashboard(self):
        self.ensure_one()
        if self.owner_id == self.env.user:
            self._get_main_dashboard().write({'is_main_dashboard': False})
            self.write({'is_main_dashboard': True})
        else:
            raise UserError('You can only set your own dashboard as your main dashboard')

    @api.model
    def action_open_main_dashboard(self):
        main_dashboard = self._get_main_dashboard()
        return main_dashboard.act_window_id.read()[0]

    def create_menu(self):
        self.ensure_one()
        return {
            'name': _('Create menu'),
            'view_mode': 'form',
            'res_model': 'create.menu.dashboard',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_board_group_id': self.id},
        }
