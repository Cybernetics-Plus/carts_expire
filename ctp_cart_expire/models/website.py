from datetime import timedelta
from odoo import _, api, fields, models
from odoo.osv import expression

class Website(models.Model):
    _inherit = "website"

    expire_delay = fields.Float(
        string="Expire Delay",
        default=0.0,
        help="Time to Auto Cancel Website Orders.\n"
        "0 is Disable.",
    )

    def _get_domain(self):
        self.ensure_one()
        expire_date = fields.Datetime.now() - timedelta(hours=self.expire_delay)
        return [
            ("website_id", "=", self.id),
            ("state", "in", ["draft", "sent"]),
            ("write_date", "<=", expire_date),
        ]

    @api.model
    def _cron_cart_expire(self):
        websites = self.search([("expire_delay", ">", 0)])
        if not websites:
            return True
        
        expire_domains = [
            website._get_domain() for website in websites
        ]
        carts_to_expire = self.env["sale.order"].search(
            expression.OR(expire_domains)
        )
        
        for cart in carts_to_expire:
            cart.message_post(body=_("Auto Cancel Cart Expired"))
        carts_to_expire.action_cancel()
