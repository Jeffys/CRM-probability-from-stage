# -*- coding: utf-8 -*-

from odoo import _, api, fields, models



class CrmStage(models.Model):
    _inherit = 'crm.stage'


    probability = fields.Float('Probability', default=0.0)
    show_probability = fields.Boolean(compute='_compute_show_probability', string='Show probability')
    
    def _compute_show_probability(self):
        for stage in self:
            stage.show_probability = self.env['ir.config_parameter'].sudo().get_param('crm.manual.compute.probability', False)