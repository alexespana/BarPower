import pytest   # Biblioteca de aserciones
import bar_power.Visits

@pytest.fixture
def visits():
    visits = bar_power.Visits.Visits()
    return visits

def test_has_new_entry_when_added_visit(visits):
    visits.add_visit('joven', 10)
    hour = bar_power.Visits.Visits.get_hour_from_time(10)
    assert visits.data[hour]['clients_type']['joven'] == 1

def test_has_new_entry_when_added_product(visits):
    visits.add_product_consumed('paella', 14)
    hour = bar_power.Visits.Visits.get_hour_from_time(14)
    assert visits.data[hour]['products_consumed']['paella'] == 1

def test_new_value_object_in_v_visits(visits):
    visits.add_visit('anciano', 19)
    assert len(visits.v_visits) == 1

def test_new_value_object_in_v_orders(visits):
    visits.add_product_consumed('Carne en salsa', 15)
    assert len(visits.v_orders) == 1
    