from pyramid.view import view_config
from pyramid.response import Response
from ..models.transaksi import Transaksi

@view_config(route_name='get_transaksi', renderer='json', request_method='GET')
def get_transaksi(request):
    transaksi = request.dbsession.query(Transaksi).all()
    return [t.__dict__ for t in transaksi]

@view_config(route_name='post_transaksi', renderer='json', request_method='POST')
def post_transaksi(request):
    data = request.json_body
    trx = Transaksi(**data)
    request.dbsession.add(trx)
    return {'status': 'success'}