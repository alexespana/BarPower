import pytest   # Biblioteca de aserciones
from bar_power.Visits import *
from bar_power.ClientType import *

HOUR = 19
PRODUCT = 'paella'
CLIENT_TYPE = ClientType.joven
HOUR_WITH_FORMAT = Visits.get_hour_from_time(HOUR)  # 19:00

@pytest.fixture
def visits():
    visits = Visits()
    return visits

def test_empty_visits_when_creation(visits):
    assert len(visits.v_visits) == 0

def test_empty_orders_when_creation(visits):
    assert len(visits.v_orders) == 0

def test_update_data_when_added_visit(visits):
    visits.add_visit(CLIENT_TYPE, HOUR)
    assert visits.data[HOUR_WITH_FORMAT]['clients_type'][CLIENT_TYPE] == 1

def test_update_data_when_added_product(visits):
    visits.add_product_consumed(PRODUCT, HOUR)
    assert visits.data[HOUR_WITH_FORMAT]['products_consumed'][PRODUCT] == 1

def test_new_visit_added(visits):
    visits.add_visit(CLIENT_TYPE, HOUR)
    assert len(visits.v_visits) == 1

def test_new_order_added(visits):
    visits.add_product_consumed(PRODUCT, HOUR)
    assert len(visits.v_orders) == 1
