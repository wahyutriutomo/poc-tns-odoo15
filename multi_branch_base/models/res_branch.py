import logging
from odoo import models, fields


_logger = logging.getLogger(__name__)


class Branch(models.Model):
    """res branch"""
    _name = "res.branch"
    _description = 'Company Branches'
    _order = 'name'

    code = fields.Char(string='Code', required=True, store=True)
    name = fields.Char(string='Branch', required=True, store=True)
    company_id = fields.Many2one('res.company', required=True, string='Company')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(
        'res.country.state',
        string="Fed. State", domain="[('country_id', '=?', country_id)]"
    )
    country_id = fields.Many2one('res.country',  string="Country")
    email = fields.Char(store=True, )
    phone = fields.Char(store=True)
    website = fields.Char(readonly=False)

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The Branch code must be unique !'),
        ('name_uniq', 'unique (name)', 'The Branch name must be unique !'),
    ]
