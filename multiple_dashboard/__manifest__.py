# -*- coding: utf-8 -*-
{
    'name': "Multiple shareable dashboard",

    'summary': """
        This module allows you to have shareable multiple dashboards.""",

    'description': """
        This module allows you to have multiple dashboards that you can share with other users. You can also create a 
        menu to see a specific dashboard and put it wherever you want.
    """,

    'author': "Apanda",
    'category': 'dashboard',
    'version': '0.1',

    'license': 'AGPL-3',
    'support': "ryantsoa@gmail.com",

    'depends': ['board'],
    'qweb': ['static/src/xml/board.xml'],

    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'security/res_groups.xml',
        'views/board_group_views.xml',
        'views/board_templates.xml',
        'wizard/create_menu_dashboard_views.xml',
    ],

    'pre_init_hook': 'pre_init',
    'post_init_hook': 'post_init',
    'uninstall_hook': 'uninstall_hook',
}
