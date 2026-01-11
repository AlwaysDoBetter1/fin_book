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
        'views/author_pavlo.xml',
        'views/reading_books.xml',
        'views/my_own_book.xml',
        'views/fin_invoices.xml',
        'views/fin_expenses.xml',
        'views/dictionary.xml',
        'views/learning_plans_pavlo.xml',
        'views/todo_tasks_pavlo.xml',
        'views/future_boughts_pavlo.xml',
        'views/expensive_boughts_pavlo.xml',

        'wizards/expense_wizard.xml',
        'wizards/invoice_wizard.xml',

        'data/books_stages.xml',
        'data/invoice_categories.xml',
        'data/author_pavlo.xml',
        'data/expense_categories.xml',
    ],
    'images': ["static/description/icon.png"],
    'demo': [],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js',
            'my_own_financial_book/static/src/js/expense_pie_chart.js',
            'my_own_financial_book/static/src/xml/expense_pie_chart.xml',
        ]
    },

    'license': 'OEEL-1',
}
