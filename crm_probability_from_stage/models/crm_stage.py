# -*- coding: utf-8 -*-

from odoo import _, api, fields, models



class CrmStage(models.Model):
    _inherit = 'crm.stage'


    probability = fields.Float('Probability', default=0.0)