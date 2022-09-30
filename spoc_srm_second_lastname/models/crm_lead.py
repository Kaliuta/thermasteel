
from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_lastname2 = fields.Char("Second last name")
