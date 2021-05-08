from odoo import fields, models

class my_model (models.Model):
	_name = "my.model"
	_description = "My Model"
	
	field1 = fields.Char(string="Name", required =True)
	
	
