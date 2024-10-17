import json
from odoo import http
from odoo.http import request

class Snippet(http.Controller):
    @http.route('/get_total_students', auth='public', type='http', methods=['GET'])
    def get_total_students(self):
        try:
            # Fetch the students data
            students = request.env['collage.student'].sudo().search_read([], ['name', 'dept', 'gender'])
            return request.make_response(json.dumps(students), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
