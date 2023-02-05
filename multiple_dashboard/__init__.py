# -*- coding: utf-8 -*-

from . import models
from . import controllers
from . import wizard
from odoo import api, SUPERUSER_ID


def pre_init(cr):
    """ Archive native dashboard menu
    """

    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref('board.menu_board_my_dash').write({'active': False})


def post_init(cr, registry):
    """ Give every user their own main dashboard
    """

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['board.group'].init_board_group()


def uninstall_hook(cr, registry):
    """ Reset native dashboard
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    for board_group in env['board.group'].search([]):
        board_group.menu_ids.sudo().unlink()
        board_group.act_window_id.view_id.sudo().unlink()
        board_group.act_window_id.sudo().unlink()
    env.ref('board.menu_board_my_dash').with_context(active_test=False).write({'active': True})
