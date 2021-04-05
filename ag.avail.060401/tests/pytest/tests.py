from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_api2_branch_io(unittest.TestCase):
  @json_dataset('data/test_2_post_v1_open.json')
  @clear_session({'spanId': 2})
  def test_2_post_v1_open(self, data_row):
    branch_key, browser_fingerprint_id, current_url, screen_height, screen_width, sdk, = data_row

    # endpoint 2
    api2_branch_io = get_http_target('TARGET_API2_BRANCH_IO', authenticate)
    resp = api2_branch_io.post('/v1/open', data=[('branch_key', branch_key), ('browser_fingerprint_id', browser_fingerprint_id), ('current_url', current_url), ('options', '{}'), ('screen_height', screen_height), ('screen_width', screen_width), ('sdk', sdk)])
    resp.assert_status_code(200)

  @json_dataset('data/test_3_post_v1_pageview.json')
  @clear_session({'spanId': 3})
  def test_3_post_v1_pageview(self, data_row):
    branch_key, browser_fingerprint_id, callback_string, data, identity_id, metadata, sdk, session_id, = data_row

    # endpoint 3
    api2_branch_io = get_http_target('TARGET_API2_BRANCH_IO', authenticate)
    resp = api2_branch_io.post('/v1/pageview', data=[('branch_key', branch_key), ('browser_fingerprint_id', browser_fingerprint_id), ('callback_string', callback_string), ('data', data), ('event', 'pageview'), ('feature', 'journeys'), ('has_app_websdk', 'false'), ('identity_id', identity_id), ('initial_referrer', ''), ('is_iframe', 'false'), ('metadata', metadata), ('open_app', 'false'), ('sdk', sdk), ('session_id', session_id), ('source', 'web-sdk'), ('user_language', 'en')])
    resp.assert_status_code(200)

@data_driven_tests
class Tests_api_goavail_io(unittest.TestCase):
  @clear_session({'spanId': 4})
  def test_4_get_api_v1_locations_airports(self):
    # endpoint 4
    api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
    resp = api_goavail_io.get('/api/v1/locations/airports')
    resp.assert_status_code(200)

  @clear_session({'spanId': 5})
  def test_5_get_api_v1_system_configs(self):
    # endpoint 5
    api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
    resp = api_goavail_io.get('/api/v1/system-configs')
    resp.assert_status_code(200)

@data_driven_tests
class Tests_availcarsharing_com(unittest.TestCase):
  @clear_session({'spanId': 9})
  def test_9_get_manifest_webmanifest(self):
    # endpoint 9
    availcarsharing_com = get_http_target('TARGET_AVAILCARSHARING_COM', authenticate)
    resp = availcarsharing_com.get('/manifest.webmanifest')
    resp.assert_status_code(200)

