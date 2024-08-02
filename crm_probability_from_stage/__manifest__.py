# -*- coding: utf-8 -*-
{
    'name': "CRM Probability From Stage",
    'summary': """
        this module assigns probability values to different CRM stages, 
        enabling more accurate sales forecasting and better decision-making throughout the sales process.""",

    'description': """
        This module allows for the manual assignment of probability values to each stage in the CRM pipeline. 
        By defining specific probabilities for various sales stages, the module ensures that the probability field in CRM leads automatically aligns with the stage’s predefined probability. 
        This approach enhances forecasting accuracy and supports sales teams in making informed decisions, ultimately improving overall sales performance and efficiency.
    """,
    'author': "Doodex",
    'website': "https://www.doodex.net/",
    'category': 'Marketing/Sales',
    'version': '16.0.1',
    'depends': ['base','crm'],
    'images': ["static/description/icon.png"],
    'license': 'LGPL-3',
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_views.xml',
        'views/res_config_settings.xml',
    ],
    'application': True,
    'installable': True
}
