# project/__init__.py
import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap


# instantiate the extensions
toolbar = DebugToolbarExtension()
bootstrap = Bootstrap()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder='./templates',
        static_folder='./static'
    )

    # set config
    app_settings = os.getenv(
        'APP_SETTINGS', 'project.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # set up extensions
    toolbar.init_app(app)
    bootstrap.init_app(app)

    # register blueprints
    from project.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    # error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template('errors/401.html'), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app