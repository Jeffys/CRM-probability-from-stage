from datetime import timedelta
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    crm_manual_compute_probability = fields.Boolean(string="Probability from stage", config_parameter="crm.manual.compute.probability")


    