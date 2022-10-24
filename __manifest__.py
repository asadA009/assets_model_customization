# -*- coding: utf-8 -*-
{
    'name': "Assets Model Customization",

    'summary': '',

    'description': """
        
    """,

    'author': "Asad Ali || PlusTech Team",
    'website': "http://www.mycompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_asset'],

    # always loaded
    'data': [
        'views/account_asset_inherit.xml',
        'report/barcode_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'auto_install': False,
}
