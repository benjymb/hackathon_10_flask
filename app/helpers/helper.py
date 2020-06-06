from flask import json

def handler_response(app, code_error, output, validate=True, payload=None):
    if payload is None:
        payload = {}

    response_object = {
        'response': {
            'message': output,
            'api_response': payload,
            'request_validate': validate,
            'status_code': code_error
        }
    }

    response = app.response_class(
        response=json.dumps(response_object),
        status=code_error,
        mimetype='application/json'
    )

    return response