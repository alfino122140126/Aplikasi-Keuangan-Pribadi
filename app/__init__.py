from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base

def main(global_config, **settings):
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    config.include("pyramid_jinja2")  # Jika perlu templating
    config.include("pyramid_tm")

    config.add_route("get_transactions", "/api/transactions")
    config.scan()

    return config.make_wsgi_app()
