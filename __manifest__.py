{
    'name': "Permisos Custom",
    'version': '16.0.1.0.0',
    #'category': 'Website/Website',
    'summary': 'Permission and no edit group',
    'description': 'Esconde Prevision de stock, grupos presupuesto tarifa y plazos de pago. no modificar impuestos en linea. Los proveedores solo se mostraran para admin en venta y grupo especifico para ocultarlos.',
    'author': 'Exemax - Fabian',
    'company': 'Exemax',
    'maintainer': 'Exemax',
    #'images': ['static/description/banner.jpg'],
    'website': 'https://www.exemax.com',
    'depends': ['base', 'sale','stock','sale_stock'],
    'data': [
        'views/product_template_form.xml',
        'views/sale_order_form.xml',
        'views/res_partner.xml',
        'data/groups.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
