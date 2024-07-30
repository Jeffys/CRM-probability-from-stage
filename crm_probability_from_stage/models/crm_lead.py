from odoo import _, api, fields, models



class CrmLead(models.Model):
    _inherit = 'crm.lead'


    probability = fields.Float('Probability', group_operator="avg", readonly=False, store=True, related='stage_id.probability')
    revenue_probability = fields.Float('Probability Revenue', default=0.0, store=True, compute="_compute_revenue_probability")


    @api.depends('stage_id', 'probability', 'expected_revenue', 'partner_id')
    def _compute_revenue_probability(self):
        for rec in self:
            rec.revenue_probability = (rec.probability/100)*rec.expected_revenue
    