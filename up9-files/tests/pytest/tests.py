from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests__5142311_fls_doubleclick_net(unittest.TestCase):

    @clear_session({'spanId': 32})
    def test_32_get_activityi(self):
        # GET https://5142311.fls.doubleclick.net/activityi (endp 32)
        _5142311_fls_doubleclick_net = get_http_target('TARGET__5142311_FLS_DOUBLECLICK_NET', authenticate)
        resp = _5142311_fls_doubleclick_net.get('/activityi')
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_adservice_google_com(unittest.TestCase):

    @clear_session({'spanId': 4})
    def test_04_get_adsid_google_ui(self):
        # GET https://adservice.google.com/adsid/google/ui (endp 4)
        adservice_google_com = get_http_target('TARGET_ADSERVICE_GOOGLE_COM', authenticate)
        resp = adservice_google_com.get('/adsid/google/ui')
        resp.assert_ok()
        # resp.assert_status_code(204)


@data_driven_tests
class Tests_api_iam_intercom_io(unittest.TestCase):

    @json_dataset('data/dataset_11.json')
    @clear_session({'spanId': 11})
    def test_11_post_messenger_web_ping(self, data_row):
        Idempotency_Key, app_id, g, page_title, referer, s, v = data_row

        # POST https://api-iam.intercom.io/messenger/web/ping (endp 11)
        api_iam_intercom_io = get_http_target('TARGET_API_IAM_INTERCOM_IO', authenticate)
        resp = api_iam_intercom_io.post('/messenger/web/ping', data=[('Idempotency-Key', Idempotency_Key), ('app_id', app_id), ('g', g), ('internal', '{}'), ('page_title', page_title), ('platform', 'web'), ('r', ''), ('referer', referer), ('s', s), ('sampling', 'false'), ('source', 'apiBoot'), ('user_active_company_id', 'undefined'), ('user_data', '{}'), ('v', v)])
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.app.active_admins.[*].name', expected_value='Refael')


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
class Tests_bat_bing_com(unittest.TestCase):

    @json_dataset('data/dataset_29.json')
    @clear_session({'spanId': 29})
    def test_29_get_action_0(self, data_row):
        ti, = data_row

        # GET https://bat.bing.com/action/0 (endp 29)
        bat_bing_com = get_http_target('TARGET_BAT_BING_COM', authenticate)
        qstr = '?' + urlencode([('Ver', '2'), ('ti', ti)])
        resp = bat_bing_com.get('/action/0' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(204)


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
class Tests_ib_adnxs_com(unittest.TestCase):

    @clear_session({'spanId': 30})
    def test_30_get_bounce(self):
        # GET https://ib.adnxs.com/bounce (endp 30)
        ib_adnxs_com = get_http_target('TARGET_IB_ADNXS_COM', authenticate)
        qstr = '?' + urlencode([('/getuid?https://www.kayak.com/s/kayakpixel/lgbl/impevent?adnxs_uid=%24UID', '')])
        resp = ib_adnxs_com.get('/bounce' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(302)

    @json_dataset('data/dataset_31.json')
    @clear_session({'spanId': 31})
    def test_31_get_getuid(self, data_row):
        https___www_kayak_com_s_kayakpixel_lgbl_impevent_adnxs_uid, = data_row

        # GET https://ib.adnxs.com/getuid (endp 31)
        ib_adnxs_com = get_http_target('TARGET_IB_ADNXS_COM', authenticate)
        qstr = '?' + urlencode([('https://www.kayak.com/s/kayakpixel/lgbl/impevent?adnxs_uid', https___www_kayak_com_s_kayakpixel_lgbl_impevent_adnxs_uid)])
        resp = ib_adnxs_com.get('/getuid' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(307)


@data_driven_tests
class Tests_ogs_google_com(unittest.TestCase):

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_03_get_widget_app_so(self, data_row):
        origin, = data_row

        # GET https://ogs.google.com/widget/app/so (endp 3)
        ogs_google_com = get_http_target('TARGET_OGS_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('cn', 'app'), ('hl', 'iw'), ('origin', origin), ('pid', '1'), ('spid', '1')])
        resp = ogs_google_com.get('/widget/app/so' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_stats_g_doubleclick_net(unittest.TestCase):

    @json_dataset('data/dataset_33.json')
    @clear_session({'spanId': 33})
    def test_33_post_j_collect(self, data_row):
        _gid, _r, _u, _v, cid, gjid, jid, tid, z = data_row

        # POST https://stats.g.doubleclick.net/j/collect (endp 33)
        stats_g_doubleclick_net = get_http_target('TARGET_STATS_G_DOUBLECLICK_NET', authenticate)
        qstr = '?' + urlencode([('_gid', _gid), ('_r', _r), ('_u', _u), ('_v', _v), ('aip', '1'), ('cid', cid), ('gjid', gjid), ('jid', jid), ('t', 'dc'), ('tid', tid), ('v', '1'), ('z', z)])
        resp = stats_g_doubleclick_net.post('/j/collect' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


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
class Tests_trcc_api_service_tradmin(unittest.TestCase):

    @json_dataset('data/dataset_40.json')
    @clear_session({'spanId': 40})
    def test_40_post_agents_agentId_verifyTargets(self, data_row):
        agentId, targetKey, value = data_row

        # POST http://trcc-api-service.tradmin/agents/{agentId}/verifyTargets (endp 40)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        with open('data/payload_for_endp_40.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.targetMapping.[*].targetKey', targetKey)
        apply_into_json(json_payload, '$.targetMapping.[*].value', value)
        resp = trcc_api_service_tradmin.post(f'/agents/{agentId}/verifyTargets', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.status', expected_value='COMPLETED')

    @json_dataset('data/dataset_41.json')
    @clear_session({'spanId': 41})
    def test_41_get_models_roee_param_all(self, data_row):
        param, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/{param}/all (endp 41)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/{param}/all')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.contracts.[*].customer', expected_value='Web Browser')

    @json_dataset('data/dataset_42.json')
    @clear_session({'spanId': 42})
    def test_42_get_models_roee_param_all_dataDependency(self, data_row):
        param, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/{param}/all/dataDependency (endp 42)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/{param}/all/dataDependency')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].type', expected_value='edge')

    @json_dataset('data/dataset_43.json')
    @clear_session({'spanId': 43})
    def test_43_get_models_roee_param_all_dataDependency_span(self, data_row):
        param, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/{param}/all/dataDependency/span (endp 43)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/{param}/all/dataDependency/span')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_44.json')
    @clear_session({'spanId': 44})
    def test_44_get_models_roee_har_entry_id(self, data_row):
        id_, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/har/entry/{id} (endp 44)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        qstr = '?' + urlencode([('fromQueue', 'false')])
        resp = trcc_api_service_tradmin.get(f'/models/roee/har/entry/{id_}' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_45.json')
    @clear_session({'spanId': 45})
    def test_45_get_models_roee_har(self, data_row):
        maxRevisionId, selectedEndpoint, services = data_row

        # GET http://trcc-api-service.tradmin/models/roee/har (endp 45)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        qstr = '?' + urlencode([('fromQueue', 'false'), ('maxEntryId', ''), ('maxRevisionId', maxRevisionId), ('methods', ''), ('pathSearch', ''), ('selectedEndpoint', selectedEndpoint), ('services', services), ('sources', ''), ('statusTypes', '')])
        resp = trcc_api_service_tradmin.get('/models/roee/har' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_46.json')
    @clear_session({'spanId': 46})
    def test_46_get_models_roee_packs_testPackId(self, data_row):
        testPackId, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/packs/{testPackId} (endp 46)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        qstr = '?' + urlencode([('metadataOnly', '1')])
        resp = trcc_api_service_tradmin.get(f'/models/roee/packs/{testPackId}' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.tests.[*].ctype', expected_value='text/html')

    @clear_session({'spanId': 47})
    def test_47_get_models_roee_sources(self):
        # GET http://trcc-api-service.tradmin/models/roee/sources (endp 47)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/sources')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 48})
    def test_48_get_models_roee_status(self):
        # GET http://trcc-api-service.tradmin/models/roee/status (endp 48)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/status')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_49.json')
    @clear_session({'spanId': 49})
    def test_49_get_models_roee_suites_all_param(self, data_row):
        param, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/{param} (endp 49)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/suites/all/{param}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.overrides.model.[*]', expected_value='drop_all_links')

    @clear_session({'spanId': 50})
    def test_50_get_models_roee_suites_all_profiles(self):
        # GET http://trcc-api-service.tradmin/models/roee/suites/all/profiles (endp 50)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/suites/all/profiles')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].model', expected_value='roee')

    @json_dataset('data/dataset_51.json')
    @clear_session({'spanId': 51})
    def test_51_post_models_roee_suites_all_runs(self, data_row):
        agentId, testPackId = data_row

        # POST http://trcc-api-service.tradmin/models/roee/suites/all/runs (endp 51)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        with open('data/payload_for_endp_51.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.agentId', agentId)
        apply_into_json(json_payload, '$.testPackId', testPackId)
        resp = trcc_api_service_tradmin.post('/models/roee/suites/all/runs', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(201)

    @json_dataset('data/dataset_52.json')
    @clear_session({'spanId': 52})
    def test_52_get_models_roee_suites_all_runs_runId(self, data_row):
        runId, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/runs/{runId} (endp 52)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/suites/all/runs/{runId}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.model', expected_value='roee')

    @clear_session({'spanId': 53})
    def test_53_get_models_roee_suites_all_runs_state(self):
        # GET http://trcc-api-service.tradmin/models/roee/suites/all/runs/state (endp 53)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/suites/all/runs/state')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_54.json')
    @clear_session({'spanId': 54})
    def test_54_get_models_roee_suites_all_runs(self, data_row):
        amount, completedOnly = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/runs (endp 54)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        qstr = '?' + urlencode([('amount', amount), ('completedOnly', completedOnly), ('inclusive', 'false'), ('reverse', 'false')])
        resp = trcc_api_service_tradmin.get('/models/roee/suites/all/runs' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].model', expected_value='roee')

    @clear_session({'spanId': 55})
    def test_55_get_users_current(self):
        # GET http://trcc-api-service.tradmin/users/current (endp 55)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/users/current')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 56})
    def test_56_get_admin_config(self):
        # GET http://trcc-api-service.tradmin/admin/config (endp 56)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/admin/config')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.organizationName', expected_value='roee')

    @clear_session({'spanId': 57})
    def test_57_post_models_modelSettings(self):
        # POST http://trcc-api-service.tradmin/models/modelSettings (endp 57)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        with open('data/payload_for_endp_57.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        resp = trcc_api_service_tradmin.post('/models/modelSettings', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].settings.git.repository', expected_value='gadotroee/tests')

    @json_dataset('data/dataset_58.json')
    @clear_session({'spanId': 58})
    def test_58_post_models_roee_revisions(self, data_row):
        maxEntryId, revisionId, sourceRevisionId = data_row

        # POST http://trcc-api-service.tradmin/models/roee/revisions (endp 58)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        with open('data/payload_for_endp_58.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.maxEntryId', maxEntryId)
        apply_into_json(json_payload, '$.revisionId', revisionId)
        apply_into_json(json_payload, '$.sourceRevisionId', sourceRevisionId)
        resp = trcc_api_service_tradmin.post('/models/roee/revisions', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('p', expected_value='Ok')

    @clear_session({'spanId': 59})
    def test_59_get_models_roee_revisions_latest(self):
        # GET http://trcc-api-service.tradmin/models/roee/revisions/latest (endp 59)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/revisions/latest')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 60})
    def test_60_get_models_roee_suites(self):
        # GET http://trcc-api-service.tradmin/models/roee/suites (endp 60)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/models/roee/suites')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].lastEnvInfo.profileName', expected_value='cluster')

    @clear_session({'spanId': 61})
    def test_61_get_tapping_state(self):
        # GET http://trcc-api-service.tradmin/tapping/state (endp 61)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/tapping/state')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.[*].type', expected_value='passive')

    @json_dataset('data/dataset_62.json')
    @clear_session({'spanId': 62})
    def test_62_get_agents_agentId_injectorConfig(self, data_row):
        agentId, = data_row

        # GET http://trcc-api-service.tradmin/agents/{agentId}/injectorConfig (endp 62)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/agents/{agentId}/injectorConfig')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_63.json')
    @clear_session({'spanId': 63})
    def test_63_get_models_roee_suites_all_agents_agentId_profiles_cluster(self, data_row):
        agentId, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/agents/{agentId}/profiles/cluster (endp 63)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/suites/all/agents/{agentId}/profiles/cluster')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.name', expected_value='cluster')

    @json_dataset('data/dataset_64.json')
    @clear_session({'spanId': 64})
    def test_64_post_models_roee_suites_all_runs_runId(self, data_row):
        endTime, rcaDataFileName, runId, startTime, status = data_row

        # POST http://trcc-api-service.tradmin/models/roee/suites/all/runs/{runId} (endp 64)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        with open('data/payload_for_endp_64.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.endTime', endTime)
        apply_into_json(json_payload, '$.rcaDataFileName', rcaDataFileName)
        apply_into_json(json_payload, '$.startTime', startTime)
        apply_into_json(json_payload, '$.status', status)
        resp = trcc_api_service_tradmin.post(f'/models/roee/suites/all/runs/{runId}', json=json_payload)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('p', expected_value='Ok')

    @clear_session({'spanId': 65})
    def test_65_get_admin_whoami(self):
        # GET http://trcc-api-service.tradmin/admin/whoami (endp 65)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get('/admin/whoami')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_jsonpath('$.organizationName', expected_value='roee')

    @json_dataset('data/dataset_66.json')
    @clear_session({'spanId': 66})
    def test_66_get_models_roee_suites_all_runs_runId_downloadTests(self, data_row):
        runId, = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/runs/{runId}/downloadTests (endp 66)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        resp = trcc_api_service_tradmin.get(f'/models/roee/suites/all/runs/{runId}/downloadTests')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_67.json')
    @clear_session({'spanId': 67})
    def test_67_get_models_roee_suites_all_runs_runId_uploadUrl(self, data_row):
        fileName, runId = data_row

        # GET http://trcc-api-service.tradmin/models/roee/suites/all/runs/{runId}/uploadUrl (endp 67)
        trcc_api_service_tradmin = get_http_target('TARGET_TRCC_API_SERVICE_TRADMIN', authenticate)
        qstr = '?' + urlencode([('fileName', fileName)])
        resp = trcc_api_service_tradmin.get(f'/models/roee/suites/all/runs/{runId}/uploadUrl' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


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

    @clear_session({'spanId': 39})
    def test_39_get_(self):
        # GET http://trdemo.stg.testr.io/ (endp 39)
        trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', authenticate)
        resp = trdemo_stg_testr_io.get('/')
        resp.assert_ok()
        # resp.assert_status_code(307)


@data_driven_tests
class Tests_widget_intercom_io(unittest.TestCase):

    @json_dataset('data/dataset_10.json')
    @clear_session({'spanId': 10})
    def test_10_get_widget_param(self, data_row):
        param, = data_row

        # GET https://widget.intercom.io/widget/{param} (endp 10)
        widget_intercom_io = get_http_target('TARGET_WIDGET_INTERCOM_IO', authenticate)
        resp = widget_intercom_io.get(f'/widget/{param}')
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_www_google_analytics_com(unittest.TestCase):

    @json_dataset('data/dataset_28.json')
    @clear_session({'spanId': 28})
    def test_28_post_j_collect(self, data_row):
        _gid, _u, _v, a, cd13, cid, de, gjid, gtm, jid, sd, sr, tid, z = data_row

        # POST https://www.google-analytics.com/j/collect (endp 28)
        www_google_analytics_com = get_http_target('TARGET_WWW_GOOGLE_ANALYTICS_COM', authenticate)
        qstr = '?' + urlencode([('_gid', _gid), ('_r', '1'), ('_s', '1'), ('_u', _u), ('_v', _v), ('a', a), ('aip', '1'), ('cd13', cd13), ('cid', cid), ('de', de), ('dl', '/'), ('dr', ''), ('dt', '-'), ('gjid', gjid), ('gtm', gtm), ('je', '0'), ('jid', jid), ('sd', sd), ('sr', sr), ('t', 'pageview'), ('tid', tid), ('ul', 'en-us'), ('v', '1'), ('vp', ''), ('z', z)])
        resp = www_google_analytics_com.post('/j/collect' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_www_google_com(unittest.TestCase):

    @json_dataset('data/dataset_1.json')
    @clear_session({'spanId': 1})
    def test_01_post_param(self, data_row):
        aftp, atyp, ei, fld, m, me, mem, net, param, pv, rt, sys_, wh = data_row

        # POST https://www.google.com/{param} (endp 1)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('adh', ''), ('aftp', aftp), ('atyp', atyp), ('bl', 'ETbN'), ('conn', 'onchange'), ('ct', 'slh'), ('ei', ei), ('fld', fld), ('ima', '0'), ('imad', '0'), ('ime', '1'), ('imea', '0'), ('imeb', '0'), ('imeh', '1'), ('imex', '1'), ('imn', '2'), ('m', m), ('me', me), ('mem', mem), ('net', net), ('pv', pv), ('rt', rt), ('s', 'web'), ('scp', '0'), ('sto', ''), ('sys', sys_), ('t', 'all'), ('v', 't1'), ('wh', wh), ('zx', str(int(time.time() * 1000)))])
        resp = www_google_com.post(f'/{param}' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_2.json')
    @clear_session({'spanId': 2})
    def test_02_get_search(self, data_row):
        aqs, ie = data_row

        # GET https://www.google.com/search (endp 2)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('aqs', aqs), ('ie', ie), ('oq', 'trdemo.stg'), ('q', 'trdemo.stg'), ('sourceid', 'chrome')])
        resp = www_google_com.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div h1', expected_value='קישורי נגישות')
        # resp.assert_cssselect('html head title', expected_value='trdemo.stg - חיפוש ב-Google')


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
