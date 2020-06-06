from app.models.companies import CompaniesModel
from app.helpers.helper import handler_response
from flask import json

class Companies:
    def __init__(self):
        self.name = ''
        self.ruc = ''
        self.status = ''

    def companies_all(self, app):
        try:
            result = CompaniesModel.get()
            companies_json = []
            for i in result:
                companies = {
                    'id': i.id,
                    'name': i.name,
                    'ruc': i.ruc,
                    'status': i.status
                }
                companies_json.append(companies)
            return handler_response(app, 200, 'Data compañias', True, companies_json)
        except Exception as e:
            return handler_response(app, 501, str(e))

    def companies_get(self, app, company_id):
        try:
            result = CompaniesModel.where('id', company_id).first()
            if result:
                companies = {
                    'id': result.id,
                    'name': result.name,
                    'ruc': result.ruc,
                    'status': result.status
                }
                return handler_response(app, 200, f'Dato compañia {company_id}', True, companies)
            else:
                return handler_response(app, 404, f'La compania no fue encontrada')
        except Exception as e:
            return handler_response(app, 501, str(e))

    def companies_create(self, app, data):
        try:
            respuesta = CompaniesModel.insert({
                #'id': 2,
                'name': data.get('name'),
                'ruc': data.get('ruc'),
                'status': data.get('status')
            })
            return handler_response(app, 201, f'''Se creo la compañia {data.get('name')}''')
        except Exception as e:
            return handler_response(app, 501, str(e))