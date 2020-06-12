from app.models.user import User
from app.helpers.helper import handler_response, decode_token, jwt_secret
from bcrypt import hashpw, gensalt
from jwt import encode

class UserController:

    @staticmethod
    def create(request,app):
        try:
            password = hashpw(request.get('password').encode('utf-8'),gensalt())
            user = User.create(
                name = request.get('name'), 
                username = request.get('username'), 
                password = password.decode('utf-8'), 
                rol = request.get('rol')
            )
            return handler_response(app,201,f'Se creo el usuario {user.username}')
        except Exception as e:
            return handler_response(app,400,str(e))

    @staticmethod
    def read(raw_token, app):
        token_info = decode_token(raw_token)
        if token_info[0]:
            current_user = User(**token_info[1])
            try:
                if current_user.obtener_rol() == 'Administrador':
                    user = User.all()
                    return handler_response(app,200,user.serialize())
                else:
                    return handler_response(app,403, "El usuario no es un administrador")
            except Exception as e:
                return handler_response(app,400,str(e))
        return handler_response(app, 403, "Envie un token valido.")

    @staticmethod
    def update(request,app):
        try:
            user = User.find(request.get('id'))
            user.name = request.get('name')
            user.username = request.get('username')
            user.save()
            return handler_response(app,201,f'Se actualizo el usuario {user.username}')
        except Exception as e:
            return handler_response(app,400,str(e))

    @staticmethod
    def login(request,app):
        try:
            user = User.where('username','=',request.get('username')).first()
            if user and user.password_valid(request.get('password')):
                token = encode(user.serialize(), jwt_secret(), algorithm='HS256')
                response = {
                    'token': token,
                    'user': user.serialize()
                }
                return handler_response(app, 200, 'Logeado con exito', response)
            message = f'el usuario : {user.username} y/o la contraseña es incorrecta'
            return handler_response(app, 401, message)
        except Exception as error:
            return handler_response(app, 500, str(error))

        
        