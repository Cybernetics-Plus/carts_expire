from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    expire_delay = fields.Float(
        related="website_id.expire_delay", 
        readonly=False
    ) 