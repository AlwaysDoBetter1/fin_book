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
