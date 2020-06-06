from flask import request
from app.controllers.companies import Companies

company = Companies()

def routes(app):
    @app.route('/')
    def hello_word():
        return 'Hello world !'

    @app.route('/employees')
    def employees():
        return 'Empleados'

    @app.route('/employees/1')
    def employees_id():
        return 'El id del empleado es 1'

    @app.route('/companies', methods=['GET'])
    def companies_get():
        return company.companies_all(app)

    @app.route('/companies/<id>', methods=['GET'])
    def companies_id(id):
        return company.companies_get(app, id)

    @app.route('/companies', methods=['POST'])
    def companies_create():
        companies_post = {}
        values = request.values
        companies_post['name'] = values.get('name')
        companies_post['ruc'] = values.get('ruc')
        companies_post['status'] = values.get('status')
        return company.companies_create(app, companies_post)