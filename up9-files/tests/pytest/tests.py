from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_auth_stg_testr_io(unittest.TestCase):

    # authentication-related test
    @json_dataset('data/dataset_9.json')
    @clear_session({'spanId': 9})
    def test_09_get_auth_realms_testr_protocol_openid_connect_auth(self, data_row):
        redirect_uri, state = data_row

        # GET https://auth.stg.testr.io/auth/realms/testr/protocol/openid-connect/auth (endp 9)
        auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
        qstr = '?' + urlencode([('client_id', 'react-client'), ('redirect_uri', redirect_uri), ('response_type', 'code'), ('state', state)])
        resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/auth' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('a#signupLink', expected_value='Sign Up')


@data_driven_tests
class Tests_httpbin_org(unittest.TestCase):

    @clear_session({'spanId': 7})
    def test_07_get_(self):
        # GET http://httpbin.org/ (endp 7)
        httpbin_org = get_http_target('TARGET_HTTPBIN_ORG', authenticate)
        resp = httpbin_org.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.swagger-ui div.wrapper section.block.block-desktop div h2', expected_value='Other Utilities')
        # resp.assert_cssselect('html head title', expected_value='httpbin.org')


@data_driven_tests
class Tests_stg_testr_io(unittest.TestCase):

    @clear_session({'spanId': 8})
    def test_08_get_(self):
        # GET https://stg.testr.io/ (endp 8)
        stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
        resp = stg_testr_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_trdemo_stg_testr_io(unittest.TestCase):

    @clear_session({'spanId': 5})
    def test_05_get_(self):
        # GET https://trdemo.stg.testr.io/ (endp 5)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', authenticate)
        resp = trdemo_stg_testr_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 6})
    def test_06_get_login(self):
        # GET https://trdemo.stg.testr.io/login (endp 6)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', dummy_auth)
        resp = trdemo_stg_testr_io.get('/login')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')


@data_driven_tests
class Tests_www_kayak_com(unittest.TestCase):

    @clear_session({'spanId': 12})
    def test_12_get_(self):
        # GET https://www.kayak.com/ (endp 12)
        www_kayak_com = get_http_target('TARGET_WWW_KAYAK_COM', authenticate)
        resp = www_kayak_com.get('/')
        resp.assert_ok()
        # resp.assert_status_code(302)
