# -*- coding: utf-8 -*-
{
    'name': "Dashboard per user",

    'summary': """
        This module helps you to see other's user dashboard""",

    'description': """
        Long description of module's purpose
    """,

    'license': 'OPL-1',

    'author': "Samuel RAMAROSELY",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/board_users.xml',
        'security/ir.model.access.csv',
        'views/board_users_view.xml',
        'views/assets_backend.xml',
    ],
    'qweb': ['static/src/xml/board.xml'],
    'images': ['static/description/cover.gif'],
    'price': 17.00,
    'currency': 'EUR',
}