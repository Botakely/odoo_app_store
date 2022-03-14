# -*- coding: utf-8 -*-
{
    'name': "Screenshot current view",

    'summary': """
        Take a screenshot of your current view""",

    'description': """
        This module allows you to take a screenshot of your current view 
    """,

    'author': "Apanda",
    'category': 'Sale',
    'version': '1.0',
    'license': 'OPL-1',

    'depends': ['base'],

    # always loaded
    'data': [
        'views/assets_backend.xml',
    ],
    'qweb': [
        'static/src/xml/template.xml'
    ],
    'images': ['static/description/cover.gif'],
}