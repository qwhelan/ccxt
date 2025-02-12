import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-


from ccxt.test.base import test_shared_methods  # noqa E402
from ccxt.test.base import test_order  # noqa E402


def test_fetch_open_orders(exchange, symbol):
    method = 'fetchOpenOrders'
    orders = exchange.fetch_open_orders(symbol)
    assert isinstance(orders, list), exchange.id + ' ' + method + ' must return an array, returned ' + exchange.json(orders)
    now = exchange.milliseconds()
    for i in range(0, len(orders)):
        order = orders[i]
        test_order(exchange, method, order, symbol, now)
        assert order['status'] == 'open', exchange.id + ' ' + method + ' ' + symbol + ' returned an order with status ' + order['status'] + ' (expected \"open\")'
    test_shared_methods.assert_timestamp_order(exchange, method, symbol, orders)
