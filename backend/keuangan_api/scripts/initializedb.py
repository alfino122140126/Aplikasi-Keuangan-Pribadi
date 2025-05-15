import sys
import transaction

from sqlalchemy import engine_from_config
from keuangan_api.models.meta import Base
from keuangan_api.models import transaksi, utang, pengingat

from pyramid.paster import get_appsettings, setup_logging

def main(argv=sys.argv):
    if len(argv) != 2:
        print("Usage: initialize_keuangan_pribadi_db development.ini")
        sys.exit(1)

    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.create_all(engine)
    print("✅ Database initialized.")