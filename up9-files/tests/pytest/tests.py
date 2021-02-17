from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_haiut_dev_spyd_io(unittest.TestCase):

    @clear_session({'spanId': 1})
    def test_1_get_(self):
        # GET https://trdemo.haiut.dev.spyd.io/ (endp 1)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', authenticate)
        resp = trdemo_haiut_dev_spyd_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 2})
    def test_2_get_login(self):
        # GET https://trdemo.haiut.dev.spyd.io/login (endp 2)
        trdemo_haiut_dev_spyd_io = get_http_target('TARGET_TRDEMO_HAIUT_DEV_SPYD_IO', dummy_auth)
        resp = trdemo_haiut_dev_spyd_io.get('/login')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')
