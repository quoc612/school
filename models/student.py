from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'
    _inherit = 'mail.thread'
    name = fields.Char(string="Name", required=True, track_visibility='always')
    age = fields.Integer(string="Age", track_visibility='onchange')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    student_dob = fields.Date(string="Date of Birth")
    nationality = fields.Many2one('res.country', string='Nationality')
