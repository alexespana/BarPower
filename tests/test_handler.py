import pytest
from bar_power.clientType import ClientType
from bar_power.handler import Handler
from tests.test_visits import HOUR, PRODUCT, CLIENT_TYPE, HOUR_WITH_FORMAT

@pytest.fixture
def handler():
    handler = Handler()
    return handler

def test_visit_creation(handler):
    visit = handler.create_visit(HOUR, CLIENT_TYPE)
    assert visit.time == HOUR
    assert visit.client_type == CLIENT_TYPE

def test_order_creation(handler):
    order = handler.create_order(HOUR, PRODUCT)
    assert order.time == HOUR 
    assert order.product == PRODUCT

def test_visits_creation(handler):
    visits = handler.create_visits()
    assert len(visits.v_orders) == 0

def test_add_visit(handler):
    handler.create_visits()
    handler.add_visit(CLIENT_TYPE, HOUR)
    assert len(handler.visits.v_visits) == 1

def test_product_consumed(handler):
    handler.create_visits()
    handler.add_product_consumed(PRODUCT, HOUR)
    assert len(handler.visits.v_orders) == 1

def test_update_data_when_added_visit(handler):
    handler.create_visits()
    handler.add_visit(CLIENT_TYPE, HOUR)
    assert handler.visits.data[HOUR_WITH_FORMAT]['clients_type'][CLIENT_TYPE] == 1   

def test_update_data_when_added_product(handler):
    handler.create_visits()
    handler.add_product_consumed(PRODUCT, HOUR)
    assert handler.visits.data[HOUR_WITH_FORMAT]['products_consumed'][PRODUCT] == 1
