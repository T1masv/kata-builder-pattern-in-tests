from shop import Shop
from tests.testhelpers import create_user


def test_happy_path(fsf_address):
    user = create_user(address=fsf_address)
    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user = create_user(address=fsf_address, age=16, verified=True)
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified(fsf_address):
    user = create_user(address=fsf_address, age=25, verified=False)
    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(paris_address):
    user = create_user(address=paris_address)
    assert Shop.must_pay_foreign_fee(user)
