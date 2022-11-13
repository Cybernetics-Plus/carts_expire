from datetime import timedelta
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    expire_date = fields.Datetime(compute="_compute_expire_date")

    @api.depends("write_date", "website_id.expire_delay")
    def _compute_expire_date(self):
        for rec in self:
            if rec.state in ["draft", "sent"] and rec.website_id.expire_delay > 0:
                from_date = rec.write_date or fields.Datetime.now()
                expire_delta = timedelta(hours=rec.website_id.expire_delay)
                rec.expire_date = from_date + expire_delta
            elif rec.expire_date:
                rec.expire_date = False
