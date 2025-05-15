from pyramid.view import view_config
from pyramid.response import Response
from ..models.utang import Utang

@view_config(route_name='get_utang', renderer='json', request_method='GET')
def get_utang(request):
    utang = request.dbsession.query(Utang).all()
    return [u.__dict__ for u in utang]

@view_config(route_name='post_utang', renderer='json', request_method='POST')
def post_utang(request):
    data = request.json_body
    entry = Utang(**data)
    request.dbsession.add(entry)
    return {'status': 'success'}