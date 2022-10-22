 
#-*- coding: utf-8 -*-
from openerp import models, fields, api
class employee(models.Model):
    _inherit = 'hr.department'
    project_id = fields.Many2one('project.project')
    code = fields.char(help="Campo modificado")
    User_partner_id= fields.Many2one('res.users')
    Is_tech= fields.Boolean()
    Description= fields.Char()
    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()   