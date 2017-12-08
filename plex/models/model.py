from odoo import models, fields, api, tools, modules, _
from odoo.exceptions import UserError, ValidationError
import keen
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)


class Plex(models.Model):
    _description = 'Plex Activities'
    _name = 'plex_activities'
    _order = 'create_date desc'

    name = fields.Text(string='Name', compute='_compute_name', store=True)
    event = fields.Text(string='Event')
    title = fields.Text(string='Title')
    type = fields.Text(string='Type')
    content_rating = fields.Text(string='Content Rating')
    summary = fields.Text(string='Summary')
    rating_key = fields.Text(string='Rating Key')
    player_title = fields.Text(string='Player')
    player_uuid = fields.Text(string='Player UUID')
    server_uuid = fields.Text(string='Server UUID')
    content_url = fields.Html(string='Content URL', compute='_compute_content_url', store=True)
    _rec_name= "name"
    
    @api.multi
    @api.depends('server_uuid', 'rating_key')
    def _compute_content_url(self):
        for eachRecord in self:
            eachRecord.content_url = "<a href='https://app.plex.tv/desktop#!/server/" + eachRecord.server_uuid + "/details?key=%2Flibrary%2Fmetadata%2F" + eachRecord.rating_key + "' target='_blank'>Open in Plex</a>"

    @api.multi
    @api.depends('event', 'title')
    def _compute_name(self):
        for eachRecord in self:
            eachRecord.name = eachRecord.event + " (" + eachRecord.title + ")"
