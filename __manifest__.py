# -*- coding: utf-8 -*-
{
    'name': "Klinik Dokter",

    'summary': """
        Odoo for klinik Dokter sederhana, Indonesia""",

    'description': """
        Odoo for klinik Dokter sederhana, Indonesia
    """,

    'author': "butirpadi@gmail.com",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'sale_management', 'sales_team'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/default_data.xml',
        'views/PasienView.xml',
        # 'views/QueueLitsView.xml',
        'views/PoliView.xml',
        'views/product_category_view.xml',
        # 'views/klinik_dashboard_view.xml',
        'views/poli_dashboard_view.xml',
        'views/appointment_view.xml',
        'views/klinik_setting_view.xml',
        # 'views/account_move_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
