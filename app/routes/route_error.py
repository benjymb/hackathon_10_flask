def error_handler(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return 'Pagina no encontrada', 404