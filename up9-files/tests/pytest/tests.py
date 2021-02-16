from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_carts_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_22.json')
    @clear_session({'spanId': 22})
    def test_22_delete_carts_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # DELETE http://carts.sock-shop/carts/{customerId} (endp 22)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        resp = carts_sock_shop.delete(f'/carts/{customerId}')
        resp.assert_status_code(202)

    @json_dataset('data/dataset_23.json')
    @clear_session({'spanId': 23})
    def test_23_post_carts_customerId_items(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/items (endp 5)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        resp = carts_sock_shop.get(f'/carts/{customerId}/items', headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)
        itemId = jsonpath('$.[*].itemId', resp)
        unitPrice = jsonpath('$.[*].unitPrice', resp)

        # POST http://carts.sock-shop/carts/{customerId}/items (endp 23)
        with open('data/payload_for_endp_23.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.itemId', itemId)
        apply_into_json(json_payload, '$.unitPrice', unitPrice)
        resp = carts_sock_shop.post(f'/carts/{customerId}/items', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)

    @json_dataset('data/dataset_24.json')
    @clear_session({'spanId': 24})
    def test_24_get_carts_customerId_merge(self, data_row):
        address, card, customer, items, sessionId = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/merge (endp 24)
        carts_sock_shop = get_http_target('TARGET_CARTS_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('sessionId', sessionId)])
        resp = carts_sock_shop.get(f'/carts/{customerId}/merge' + qstr)
        resp.assert_status_code(202)


@data_driven_tests
class Tests_catalogue_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_19.json')
    @clear_session({'spanId': 19})
    def test_19_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 20)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        id_ = jsonpath('$.[*].id', resp)

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 19)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_status_code(200)

    @clear_session({'spanId': 33})
    def test_33_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/catalogue/size (endp 33)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('tags', '')])
        resp = catalogue_sock_shop.get('/catalogue/size' + qstr)
        resp.assert_status_code(200)

    @clear_session({'spanId': 35})
    def test_35_get_tags(self):
        # GET http://catalogue.sock-shop/tags (endp 35)
        catalogue_sock_shop = get_http_target('TARGET_CATALOGUE_SOCK_SHOP', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)


@data_driven_tests
class Tests_front_end_sock_shop(unittest.TestCase):

    @clear_session({'spanId': 7})
    def test_07_get_(self):
        # GET http://front-end.sock-shop/ (endp 7)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm')])
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 8})
    def test_08_get_cart(self):
        # GET http://front-end.sock-shop/cart (endp 8)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 11})
    def test_11_get_basket_html(self):
        # GET http://front-end.sock-shop/basket.html (endp 11)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/basket.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#basket div.box form h1', expected_value='Shopping cart')

    @clear_session({'spanId': 12})
    def test_12_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 12)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.delete('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(202)

    @clear_session({'spanId': 13})
    def test_13_post_cart(self):
        # POST http://front-end.sock-shop/orders (endp 18)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.post('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items.[*].itemId', resp)

        # POST http://front-end.sock-shop/cart (endp 13)
        with open('data/payload_for_endp_13.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)

    @clear_session({'spanId': 15})
    def test_15_get_category_html(self):
        # GET http://front-end.sock-shop/category.html (endp 15)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/category.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.panel.panel-default.sidebar-menu div.panel-heading h3.panel-title', expected_value='Filters ')

    @clear_session({'spanId': 16})
    def test_16_get_detail_html(self):
        # POST http://front-end.sock-shop/orders (endp 18)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.post('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items.[*].itemId', resp)

        # GET http://front-end.sock-shop/detail.html (endp 16)
        qstr = '?' + urlencode([('id', id_)])
        resp = front_end_sock_shop.get('/detail.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    # authentication-related test
    @clear_session({'spanId': 17})
    def test_17_get_login(self):
        # GET http://front-end.sock-shop/login (endp 17)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', dummy_auth)
        resp = front_end_sock_shop.get('/login')
        resp.assert_status_code(200)
        resp.assert_cssselect('p', expected_value='Cookie is set')

    @clear_session({'spanId': 36})
    def test_36_get_address(self):
        # GET http://front-end.sock-shop/address (endp 36)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/address', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')

    @clear_session({'spanId': 38})
    def test_38_get_card(self):
        # GET http://front-end.sock-shop/card (endp 38)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/card', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_42.json')
    @clear_session({'spanId': 42})
    def test_42_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 9)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$.[*].id', resp)

        # GET http://front-end.sock-shop/catalogue/{id} (endp 42)
        resp = front_end_sock_shop.get(f'/catalogue/{id_}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 43})
    def test_43_get_catalogue_size(self):
        # GET http://front-end.sock-shop/catalogue/size (endp 43)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('tags', '')])
        resp = front_end_sock_shop.get('/catalogue/size' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_45.json')
    @clear_session({'spanId': 45})
    def test_45_get_customer_order_html(self, data_row):
        order, = data_row

        # GET http://front-end.sock-shop/customer-order.html (endp 45)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('order', order)])
        resp = front_end_sock_shop.get('/customer-order.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-order div.box h2', expected_value='Order #')

    @clear_session({'spanId': 46})
    def test_46_get_customer_orders_html(self):
        # GET http://front-end.sock-shop/customer-orders.html (endp 46)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/customer-orders.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-orders div.box h1', expected_value='My orders')

    @json_dataset('data/dataset_47.json')
    @clear_session({'spanId': 47})
    def test_47_get_customers_customerId(self, data_row):
        customerId, = data_row

        # GET http://front-end.sock-shop/customers/{customerId} (endp 47)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get(f'/customers/{customerId}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.lastName', expected_value='Name')

    @clear_session({'spanId': 51})
    def test_51_get_orders_href(self):
        # GET http://front-end.sock-shop/orders (endp 49)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')
        href = url_part('/2', jsonpath('$.[*]._links.self.href', resp))

        # GET http://front-end.sock-shop/orders/{href} (endp 51)
        resp = front_end_sock_shop.get(f'/orders/{href}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @clear_session({'spanId': 52})
    def test_52_get_tags(self):
        # GET http://front-end.sock-shop/tags (endp 52)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/tags', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 55})
    def test_55_head_(self):
        # HEAD http://front-end.sock-shop/ (endp 55)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.head('/')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_57.json')
    @clear_session({'spanId': 57})
    def test_57_get_(self, data_row):
        content, = data_row

        # GET http://front-end.sock-shop/ (endp 57)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        qstr = '?' + urlencode([('a', 'fetch'), ('content', content)])
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 60})
    def test_60_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 60)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @clear_session({'spanId': 61})
    def test_61_get_navbar_html(self):
        # GET http://front-end.sock-shop/navbar.html (endp 61)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/navbar.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 62})
    def test_62_get_topbar_html(self):
        # GET http://front-end.sock-shop/topbar.html (endp 62)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/topbar.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success.btn-sm', expected_value='Offer of the day')

    @clear_session({'spanId': 69})
    def test_69_get_(self):
        # GET http://front-end.sock-shop/ (endp 69)
        front_end_sock_shop = get_http_target('TARGET_FRONT_END_SOCK_SHOP', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(206)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')


@data_driven_tests
class Tests_orders_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_54.json')
    @clear_session({'spanId': 54})
    def test_54_get_orders_href(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 31)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.city', expected_value='Glasgow')
        href = url_part('/2', jsonpath('$._embedded.customerOrders.[*]._links.self.href', resp))

        # GET http://orders.sock-shop/orders/{href} (endp 54)
        resp = orders_sock_shop.get(f'/orders/{href}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')


@data_driven_tests
class Tests_payment_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_04_post_paymentAuth(self, data_row):
        address, addresseId, amount, card, cardId, customer, items, longNum, number = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 3)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.lastName', expected_value='Name')
        firstName = jsonpath('$.firstName', resp)

        # GET http://user.sock-shop/addresses/{addresseId} (endp 1)
        resp = user_sock_shop.get(f'/addresses/{addresseId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        country = jsonpath('$.country', resp)
        postcode = jsonpath('$.postcode', resp)
        street = jsonpath('$.street', resp)

        # GET http://user.sock-shop/cards/{cardId} (endp 2)
        resp = user_sock_shop.get(f'/cards/{cardId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        ccv = jsonpath('$.ccv', resp)
        expires = jsonpath('$.expires', resp)

        # POST http://payment.sock-shop/paymentAuth (endp 4)
        payment_sock_shop = get_http_target('TARGET_PAYMENT_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_4.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address.country', country)
        apply_into_json(json_payload, '$.address.number', number)
        apply_into_json(json_payload, '$.address.postcode', postcode)
        apply_into_json(json_payload, '$.address.street', street)
        apply_into_json(json_payload, '$.amount', amount)
        apply_into_json(json_payload, '$.card.ccv', ccv)
        apply_into_json(json_payload, '$.card.expires', expires)
        apply_into_json(json_payload, '$.card.longNum', longNum)
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)


@data_driven_tests
class Tests_shipping_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_6.json')
    @clear_session({'spanId': 6})
    def test_06_post_shipping(self, data_row):
        name, = data_row

        # POST http://shipping.sock-shop/shipping (endp 6)
        shipping_sock_shop = get_http_target('TARGET_SHIPPING_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_6.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', str(uuid.uuid4()))
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)


@data_driven_tests
class Tests_user_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_26.json')
    @clear_session({'spanId': 26})
    def test_26_get_customers_customerId_addresses(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 26)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address.[*].city', expected_value='Glasgow')

    @json_dataset('data/dataset_27.json')
    @clear_session({'spanId': 27})
    def test_27_get_customers_customerId_cards(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 29)
        orders_sock_shop = get_http_target('TARGET_ORDERS_SOCK_SHOP', authenticate)
        with open('data/payload_for_endp_29.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/cards (endp 27)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/cards')
        resp.assert_status_code(200)

    # authentication-related test
    @clear_session({'spanId': 28})
    def test_28_get_login(self):
        # GET http://user.sock-shop/login (endp 28)
        user_sock_shop = get_http_target('TARGET_USER_SOCK_SHOP', dummy_auth)
        resp = user_sock_shop.get('/login')
        resp.assert_status_code(200)
