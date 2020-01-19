# -*- coding: utf-8 -*-
{
    'name': "First/Last Pager",

    'summary': """
        This module helps you to browse first or last page of list in form by one click""",

    'description': """
        This module helps you to browse first or last page of list in form by one click
    """,

    'license': 'AGPL-3',
    'author': "Apanda",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/webclient_templates.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        "static/src/xml/base.xml",
    ],
}