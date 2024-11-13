from shop import Shop
from tests.conftest import create_user

def test_happy_path():
    user = create_user(has_address_local=True)
    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = create_user(has_address_local=True, is_major=False, is_verified=True)
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    user = create_user(has_address_local=True, is_major=True, is_verified=False)
    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee():
    user = create_user(has_address_local=False)
    assert Shop.must_pay_foreign_fee(user)
