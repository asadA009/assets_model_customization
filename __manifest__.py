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
    'depends': ['account_asset', 'stock_account', 'product', 'sale_margin'],

    # always loaded
    'data': [
        'security/security_groups.xml',
        'views/account_asset_inherit.xml',
        'views/product_view_inherit.xml',
        'views/sale_order_view_inherit.xml',
        'report/barcode_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'auto_install': False,
}
