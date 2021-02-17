from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_haiut_dev_spyd_io(unittest.TestCase):

    @clear_session({'spanId': 1})
    def test_01_get_(self):
        # GET https://trdemo.haiut.dev.spyd.io/ (endp 1)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 2})
    def test_02_get_cart(self):
        # GET https://trdemo.haiut.dev.spyd.io/cart (endp 2)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h2', expected_value='Cart for alex.haiut@testr.io')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_03_get_cart_add(self, data_row):
        product_id, = data_row

        # GET https://trdemo.haiut.dev.spyd.io/cart/add (endp 3)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        qstr = '?' + urlencode([('product_id', product_id)])
        resp = trdemo_haiut_dev_spyd_io.get('/cart/add' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_04_get_cart_remove_flight_id(self, data_row):
        flight_id, = data_row

        # GET https://trdemo.haiut.dev.spyd.io/cart/remove/{flight_id} (endp 4)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get(f'/cart/remove/{flight_id}')
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_05_get_flight(self, data_row):
        flight_id, = data_row

        # GET https://trdemo.haiut.dev.spyd.io/flight (endp 5)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        qstr = '?' + urlencode([('flight_id', flight_id)])
        resp = trdemo_haiut_dev_spyd_io.get('/flight' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h2', expected_value='Details for flight LY-007')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 6})
    def test_06_get_login(self):
        # GET https://trdemo.haiut.dev.spyd.io/login (endp 6)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', dummy_auth)
        resp = trdemo_haiut_dev_spyd_io.get('/login')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 7})
    def test_07_get_logout(self):
        # GET https://trdemo.haiut.dev.spyd.io/logout (endp 7)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', dummy_auth)
        resp = trdemo_haiut_dev_spyd_io.get('/logout')
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_8.json')
    @clear_session({'spanId': 8})
    def test_08_get_search(self, data_row):
        startDate, = data_row

        # GET https://trdemo.haiut.dev.spyd.io/search (endp 8)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        qstr = '?' + urlencode([('destination', '*'), ('endDate', ''), ('source', '*'), ('startDate', startDate)])
        resp = trdemo_haiut_dev_spyd_io.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#flightsearch-form form.form-search h1.h3.font-weight-normal', expected_value=' Search Flights')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 9})
    def test_09_get_(self):
        # GET http://trdemo.haiut.dev.spyd.io/ (endp 9)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(307)

    @clear_session({'spanId': 10})
    def test_10_get_cart(self):
        # GET http://trdemo.haiut.dev.spyd.io/cart (endp 10)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(307)
