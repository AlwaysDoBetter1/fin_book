{
    'name': 'Financial book',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 200,
    'summary': 'My own financial book',
    'description': """My own financial book""",
    'depends': ['base', 'web'],
    'author': "Pavlo",
    'data': [
        'security/ir.model.access.csv',

        'views/actions.xml',
        'views/menuitems.xml',
    ],
    'images': ["static/description/icon.png"],
    'demo': [],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
        ]
    },

    'license': 'OEEL-1',
}
