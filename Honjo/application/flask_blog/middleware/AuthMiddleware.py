from flask import session,redirect,url_for
from werkzeug.exceptions import Unauthorized
class AuthMiddleware:
    def __init__(self,app):
        self.app=app
    def __call__(self,environ,start_response):
        print('middleware called')
        # middlewareでsessionはダメらしい
        if not session.get('logged_in'):
            raise Unauthorized()
        return self.app(environ,start_response)
    
