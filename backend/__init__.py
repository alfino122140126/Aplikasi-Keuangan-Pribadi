from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models.meta import Base
from .routes.routes import includeme

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    config = Configurator(settings=settings)
    config.include('pyramid_tm')
    config.include(includeme)
    
    config.scan('.views')
    
    from .models import transaksi, utang, pengingat
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    
    return config.make_wsgi_app()