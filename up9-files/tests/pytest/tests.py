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

    @clear_session({'spanId': 35})
    def test_35_get_(self):
        # GET https://trdemo.stg.testr.io/ (endp 35)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', authenticate)
        resp = trdemo_stg_testr_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @json_dataset('data/dataset_37.json')
    @clear_session({'spanId': 37})
    def test_37_post_login(self, data_row):
        user, = data_row

        # POST https://trdemo.stg.testr.io/login (endp 37)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', dummy_auth)
        resp = trdemo_stg_testr_io.post('/login', data=[('user', user)])
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_38.json')
    @clear_session({'spanId': 38})
    def test_38_get_search(self, data_row):
        startDate, = data_row

        # GET https://trdemo.stg.testr.io/search (endp 38)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', authenticate)
        qstr = '?' + urlencode([('destination', '*'), ('endDate', ''), ('source', '*'), ('startDate', startDate)])
        resp = trdemo_stg_testr_io.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#flightsearch-form form.form-search h1.h3.font-weight-normal', expected_value=' Search Flights')
        # resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')


@data_driven_tests
class Tests_www_il_kayak_com(unittest.TestCase):

    @clear_session({'spanId': 14})
    def test_14_get_(self):
        # GET https://www.il.kayak.com/ (endp 14)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        qstr = '?' + urlencode([('ispredir', 'true')])
        resp = www_il_kayak_com.get('/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#ptn1 h1.SeoLinksHeader__subtitle', expected_value='Search Flights, Hotels & Rental Cars')
        # resp.assert_cssselect('html head title', expected_value='Search Flights, Hotels & Rental Cars | KAYAK')

    @json_dataset('data/dataset_15.json')
    @clear_session({'spanId': 15})
    def test_15_post_s_horizon_common_ccpa_CCPAConsent(self, data_row):
        r9version, scriptsMetadata, stylesMetadata = data_row

        # POST https://www.il.kayak.com/s/horizon/common/ccpa/CCPAConsent (endp 15)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/s/horizon/common/ccpa/CCPAConsent', data=[('r9version', r9version), ('scriptsMetadata', scriptsMetadata), ('stylesMetadata', stylesMetadata)], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_16.json')
    @clear_session({'spanId': 16})
    def test_16_post_s_horizon_common_core_AjaxMany(self, data_row):
        components__, formtoken, parameters__ = data_row

        # POST https://www.il.kayak.com/s/horizon/common/core/AjaxMany (endp 16)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/s/horizon/common/core/AjaxMany', data=[('components[]', components__), ('formtoken', formtoken), ('parameters[]', parameters__)], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 17})
    def test_17_post_s_horizon_compareTo_config(self):
        # POST https://www.il.kayak.com/s/horizon/compareTo/config (endp 17)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/s/horizon/compareTo/config', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.content.workaround.name', expected_value='SwapperNoSpinner')

    @clear_session({'spanId': 18})
    def test_18_get_s_horizon_react_component_CurrencyPickerStateProviderAction(self):
        # GET https://www.il.kayak.com/s/horizon/react/component/CurrencyPickerStateProviderAction (endp 18)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.get('/s/horizon/react/component/CurrencyPickerStateProviderAction', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.current.displayName', expected_value='Israeli New Shekels')

    @clear_session({'spanId': 19})
    def test_19_get_s_horizon_react_component_FooterSiteMapLinksProviderAction(self):
        # GET https://www.il.kayak.com/s/horizon/react/component/FooterSiteMapLinksProviderAction (endp 19)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.get('/s/horizon/react/component/FooterSiteMapLinksProviderAction', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 20})
    def test_20_get_s_horizon_react_component_PrivacyMenuStateProviderAction(self):
        # GET https://www.il.kayak.com/s/horizon/react/component/PrivacyMenuStateProviderAction (endp 20)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.get('/s/horizon/react/component/PrivacyMenuStateProviderAction', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_21.json')
    @clear_session({'spanId': 21})
    def test_21_post_s_run_kmkid_set(self, data_row):
        kmkid, = data_row

        # POST https://www.il.kayak.com/s/run/kmkid/set (endp 21)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/s/run/kmkid/set', data=[('kmkid', kmkid)], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_22.json')
    @clear_session({'spanId': 22})
    def test_22_post_s_vestigo_v1_measure(self, data_row):
        clientRequestTime, domain, eventName, eventObject, eventType, height, npmPackageVersion, queryString, subPageType, timestamp, viewId, width = data_row

        # POST https://www.il.kayak.com/s/vestigo/v1/measure (endp 22)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        with open('data/payload_for_endp_22.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.events.[*].context.client.npmPackageVersion', npmPackageVersion)
        apply_into_json(json_payload, '$.events.[*].context.client.windowSize.height', height)
        apply_into_json(json_payload, '$.events.[*].context.client.windowSize.width', width)
        apply_into_json(json_payload, '$.events.[*].context.domain', domain)
        apply_into_json(json_payload, '$.events.[*].context.location.queryString', queryString)
        apply_into_json(json_payload, '$.events.[*].context.viewCode.subPageType', subPageType)
        apply_into_json(json_payload, '$.events.[*].context.viewId', viewId)
        apply_into_json(json_payload, '$.events.[*].eventName', eventName)
        apply_into_json(json_payload, '$.events.[*].eventType', eventType)
        apply_into_json(json_payload, '$.events.[*].payload.eventObject', eventObject)
        apply_into_json(json_payload, '$.events.[*].timestamp', timestamp)
        apply_into_json(json_payload, '$.headers.clientRequestTime', clientRequestTime)
        resp = www_il_kayak_com.post('/s/vestigo/v1/measure', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)

    @clear_session({'spanId': 23})
    def test_23_get_ugtm_(self):
        # GET https://www.il.kayak.com/ugtm/ (endp 23)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        qstr = '?' + urlencode([('ispredir', 'true')])
        resp = www_il_kayak_com.get('/ugtm/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 24})
    def test_24_post_vs_main_frontdoor_EmailSubscriptionPanel_show(self):
        # POST https://www.il.kayak.com/vs/main/frontdoor/EmailSubscriptionPanel/show (endp 24)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/vs/main/frontdoor/EmailSubscriptionPanel/show', data=[('action', 'vs')], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_25.json')
    @clear_session({'spanId': 25})
    def test_25_post_vs_main_frontdoor_IsNi_covidExplore_shown(self, data_row):
        IsNi, = data_row

        # POST https://www.il.kayak.com/vs/main/frontdoor/{IsNi}/covidExplore/shown (endp 25)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post(f'/vs/main/frontdoor/{IsNi}/covidExplore/shown', data=[('action', 'vs')], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)

    @clear_session({'spanId': 26})
    def test_26_post_vs_main_frontdoor_saving_loaded_drawer(self):
        # POST https://www.il.kayak.com/vs/main/frontdoor/saving/loaded/drawer (endp 26)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/vs/main/frontdoor/saving/loaded/drawer', data=[('action', 'vs'), ('searchid', 'undefined')])
        resp.assert_ok()
        # resp.assert_status_code(204)

    @clear_session({'spanId': 27})
    def test_27_post_vs_page_main_frontdoor(self):
        # POST https://www.il.kayak.com/vs/page/main/frontdoor (endp 27)
        www_il_kayak_com = get_http_target('TARGET_WWW_IL_KAYAK_COM', authenticate)
        resp = www_il_kayak_com.post('/vs/page/main/frontdoor', data=[('action', 'vs')], headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_ok()
        # resp.assert_status_code(204)


@data_driven_tests
class Tests_www_kayak_com(unittest.TestCase):

    @clear_session({'spanId': 12})
    def test_12_get_(self):
        # GET https://www.kayak.com/ (endp 12)
        www_kayak_com = get_http_target('TARGET_WWW_KAYAK_COM', authenticate)
        resp = www_kayak_com.get('/')
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_13.json')
    @clear_session({'spanId': 13})
    def test_13_post_s_run_kmkid_sync(self, data_row):
        suggestedKmkid, = data_row

        # POST https://www.kayak.com/s/run/kmkid/sync (endp 13)
        www_kayak_com = get_http_target('TARGET_WWW_KAYAK_COM', authenticate)
        resp = www_kayak_com.post('/s/run/kmkid/sync', data=[('suggestedKmkid', suggestedKmkid)])
        resp.assert_ok()
        # resp.assert_status_code(200)
