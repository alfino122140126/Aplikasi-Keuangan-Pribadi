from pyramid.view import view_config
from pyramid.response import Response
from ..models import DBSession, Transaction
import json

@view_config(route_name='get_transactions', renderer='json')
def get_transactions(request):
    result = DBSession.query(Transaction).all()
    data = [
        {
            "id": t.id,
            "amount": t.amount,
            "category": t.category,
            "description": t.description,
            "date": t.date.isoformat()
        }
        for t in result
    ]
    return data
