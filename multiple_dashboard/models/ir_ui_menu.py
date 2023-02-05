# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IrUiMenu(models.AbstractModel):
    _inherit = 'ir.ui.menu'

    def remove_board_menu(self):
        self.ensure_one()
        self.sudo().unlink()
