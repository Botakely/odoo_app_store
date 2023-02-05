# -*- coding: utf-8 -*-

import json
from odoo.addons.board.controllers.main import Board
from odoo.http import Controller, route, request
from lxml import etree as ElementTree

class BoardInherit(Board):

    @route('/board/add_to_dashboard', type='json', auth='user')
    def add_to_dashboard(self, action_id, context_to_save, domain, view_mode, name=''):
        board_group_id = context_to_save.get('board_group_id')
        if board_group_id:
            board_group = request.env['board.group'].browse(context_to_save['board_group_id'])
            action = board_group.act_window_id
            if action and action['res_model'] == 'board.board' and action['views'][0][1] == 'form' and action_id:
                view_id = action['views'][0][0]
                board = request.env['board.board'].fields_view_get(view_id, 'form')
                if board and 'arch' in board:
                    xml = ElementTree.fromstring(board['arch'])
                    column = xml.find('./board/column')
                    if column is not None:
                        new_action = ElementTree.Element('action', {
                            'name': str(action_id),
                            'string': name,
                            'view_mode': view_mode,
                            'context': str(context_to_save),
                            'domain': str(domain)
                        })
                        column.insert(0, new_action)
                        arch = ElementTree.tostring(xml, encoding='unicode')
                        request.env['ir.ui.view.custom'].create({
                            'user_id': request.session.uid,
                            'ref_id': view_id,
                            'arch': arch
                        })
                        return True
            return False
        return super(BoardInherit, self).add_to_dashboard(action_id, context_to_save, domain, view_mode, name)