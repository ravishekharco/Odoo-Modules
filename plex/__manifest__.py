# -*- coding: utf-8 -*-
{
    'name': "Plex",

    'summary': """Plex""",

    'description': """
        Plex
    """,

    'author': "Ravi Shekhar",
    'website': "shekhar.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
             'views/view.xml',
             'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
   'external_dependencies': {},#{'python' : ['dateutil']}, # pip install python-dateutil
}
