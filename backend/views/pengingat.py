from pyramid.view import view_config
from pyramid.response import Response
from ..models.pengingat import Pengingat

@view_config(route_name='get_pengingat', renderer='json', request_method='GET')
def get_pengingat(request):
    data = request.dbsession.query(Pengingat).all()
    return [p.__dict__ for p in data]

@view_config(route_name='post_pengingat', renderer='json', request_method='POST')
def post_pengingat(request):
    data = request.json_body
    item = Pengingat(**data)
    request.dbsession.add(item)
    return {'status': 'success'}