# -*- coding: utf-8 -*-
{
    'name': "Plex",
    'summary': """Plex""",
    'description': """
        We love and care about our media. We want to share that love.
        Many of us joined Plex after having already been members of the Plex community, a community very near and dear to our hearts. Some of us are movie buffs. Some are news junkies. Some are passionate about music. Some are budding photographers or videographers. But one thing we all share a love for media! And we love that the constantly evolving landscape of mobile and connected devices gives us the opportunity to improve the way you discover, enjoy, and share all of your media on all of your devices.
    """,
    'application': True,
    'author': "Ravi Shekhar",
    'website': "shekhar.co",
    'category': 'Entertainment',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
             'views/view.xml',
             'security/ir.model.access.csv',
    ],
   'external_dependencies': {},
}
