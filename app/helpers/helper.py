from flask import json
import os
from flask import json, request, jsonify
from dotenv import load_dotenv
from pathlib import Path
from functools import wraps
from jwt import decode
from app.models.user import User

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

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

def jwt_secret():
    return os.getenv('JWT_SECRET')

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('_token')
        if not token:
            return jsonify({
                'response': {
                    'system_message': 'Token no encontrado',
                    'api_response': {},
                    'status_code': 401
                }
            })

        try:
            decode(token, jwt_secret())
        except Exception as e:
            return jsonify({
                'response': {
                    'system_message': 'Token incorrecto',
                    'api_response': {
                        'error': f'{str(e)}'
                    },
                    'status_code': 401
                }
            })

        return f(*ars, **kwargs)

    return decorator

def decode_token(token):
    try:
        decoded_token = decode(token, jwt_secret())
        return (True, decoded_token)
    except Exception as e:
        return (False, e)

def allowed_roles(*decorator_args):
    def inner_function(function):
        @wraps(function)
        def decorator(*args, **kwargs):
            token = request.headers.get('_token')
            decoded_token = decode(token, jwt_secret())
            current_user = User(**decoded_token)
            if current_user.rol in decorator_args:
                return function(*args, **kwargs)
            else:
                return jsonify({
                    'response': {
                        'system_message': 'El usuario no tiene permisos',
                        'api_response': {
                            'error': 'El usuario no tiene permisos'
                        },
                        'status_code': 403
                    }
                })
        return decorator
    return inner_function

def jwt_secret():
    return os.getenv('JWT_SECRET')
