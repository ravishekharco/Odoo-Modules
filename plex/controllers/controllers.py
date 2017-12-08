from odoo.http import request
from odoo import http
import logging
from inspect import currentframe, getframeinfo
from odoo.exceptions import MissingError, UserError, ValidationError
from werkzeug._internal import _log
_logger = logging.getLogger(__name__)
import simplejson
import json
from datetime import datetime
 
class PlexController(http.Controller):
    
    @http.route('/plex/webhook',methods=['GET','POST'],type="http",auth='public',csrf=False)
    def plexWebhookHttpd(self,**kwargs):
#         _logger.debug('plex/webhook' + str(kwargs))
#         _logger.debug('plex/webhook type' + str(type(kwargs)))
#         _logger.debug('plex/webhook payload' + str(kwargs['payload']))
#         _logger.debug('plex/webhook payload type' + str(type(kwargs['payload'])))
#         _logger.debug('plex/webhook payload event' + str(kwargs['payload']['event']))
#         json_acceptable_string = str(kwargs['payload']).replace("'", "\"")
        if 'payload' in kwargs.keys():
            data = json.loads(kwargs['payload'])
            vals = {}
            if 'event' in data.keys():
                vals['event'] = data['event']
            if 'Metadata' in data.keys():
                if 'title' in data['Metadata'].keys():
                    vals['title'] = data['Metadata']['title']
                if 'type' in data['Metadata'].keys():
                    vals['type'] = data['Metadata']['type']
                if 'contentRating' in data['Metadata'].keys():
                    vals['content_rating'] = data['Metadata']['contentRating']
                if 'summary' in data['Metadata'].keys():
                    vals['summary'] = data['Metadata']['summary']
                if 'ratingKey' in data['Metadata'].keys():
                    vals['rating_key'] = data['Metadata']['ratingKey']
            if 'Server' in data.keys():
                if 'uuid' in data['Server'].keys():
                    vals['server_uuid'] = data['Server']['uuid']
            if 'Player' in data.keys():
                if 'uuid' in data['Player'].keys():
                    vals['player_uuid'] = data['Player']['uuid']
                if 'title' in data['Player'].keys():
                    vals['player_title'] = data['Player']['title']
            createPlexActivityResponse = request.env['plex_activities'].sudo().create(vals)
            _logger.debug('plex/webhook data event' + str(data['event']))
            _logger.debug('plex/webhook createPlexActivityResponse' + str(createPlexActivityResponse))
        return simplejson.dumps({'code':'200'})
