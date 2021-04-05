from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_api_goavail_io(unittest.TestCase):

    @clear_session({'spanId': 16})
    def test_016_get_api_v1_metadata_pricings_pricePlanId(self):
        # GET https://api.goavail.io/api/v1/locations/airports (endp 14)
        api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
        resp = api_goavail_io.get('/api/v1/locations/airports')
        pricePlanId = jsonpath('$.items.[*].vehicleCategories.*.pricePlanId', resp)

        # GET https://api.goavail.io/api/v1/metadata/pricings/{pricePlanId} (endp 16)
        resp = api_goavail_io.get(f'/api/v1/metadata/pricings/{pricePlanId}')

    @clear_session({'spanId': 17})
    def test_017_get_api_v1_system_configs(self):
        # GET https://api.goavail.io/api/v1/system-configs (endp 17)
        api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
        resp = api_goavail_io.get('/api/v1/system-configs')

    @clear_session({'spanId': 18})
    def test_018_get_api_v1_vehicles_metadata_categories(self):
        # GET https://api.goavail.io/api/v1/vehicles/metadata/categories (endp 18)
        api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
        resp = api_goavail_io.get('/api/v1/vehicles/metadata/categories')


@data_driven_tests
class Tests_api_permutive_com(unittest.TestCase):

    @json_dataset('data/dataset_63.json')
    @clear_session({'spanId': 63})
    def test_063_post_param_batch_events(self, data_row):
        ad_unit_path, advertiser_id, author, autonomous_system_number, campaign_id, category, description, desturl, domain, k, k1, key, name, param, param1, query, slot_element_id, user_agent, utitle, view_id = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        href = url_part('/4', cssselect('article#F_Content div.block.B6 div.block.B6 div.block.B3 div.block.B3 div.element.B3.ghcite.noBottomPadding div div.cell.cshort.layout1 a[href] @href', resp))

        # GET https://www.ynet.co.il/digital/technews/article/{href} (endp 36)
        resp = www_ynet_co_il.get(f'/digital/technews/article/{href}')
        title = cssselect('html head meta[content] @content', resp)

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        referrer = jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp)
        url = jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp)
        ip_hash = jsonpath('$.data.userEvents.events.[*].properties.ip_hash', resp)
        isp = jsonpath('$.data.geoip.isp.isp', resp)
        organization = jsonpath('$.data.geoip.isp.isp', resp)
        segment_id = jsonpath('$.data.userEvents.events.[*].properties.segment_id', resp)
        session_id = jsonpath('$.data.userEvents.events.[*].session_id', resp)
        user_id = jsonpath('$.data.userIdentify.identity.identify.id', resp)

        # POST https://api.permutive.com/{param}/batch/events (endp 63)
        qstr = '?' + urlencode([('enrich', 'false'), ('k', k1)])
        resp = api_permutive_com.post(f'/{param1}/batch/events' + qstr)

    @json_dataset('data/dataset_64.json')
    @clear_session({'spanId': 64})
    def test_064_post_param_events(self, data_row):
        domain, k, k1, param, param1, query, user_agent, view_id = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        href = url_part('/4', cssselect('article#F_Content div.block.B6 div.block.B6 div.block.B3 div.block.B3 div.element.B3.ghcite.noBottomPadding div div.cell.cshort.layout1 a[href] @href', resp))

        # GET https://www.ynet.co.il/digital/technews/article/{href} (endp 36)
        resp = www_ynet_co_il.get(f'/digital/technews/article/{href}')
        referrer = cssselect('div div div.hContainer.ynet div.RelativeElementsContainer.site_page_root div.layoutContainer div.layoutItem.category-header span.no-small-vp div div.CategoryHeader div.rightWrapper div.logo a[href] @href', resp)
        title = cssselect('html head meta[content] @content', resp)
        dest_url = cssselect('html head meta[content] @content', resp)

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        url = jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp)
        session_id = jsonpath('$.data.userEvents.events.[*].session_id', resp)
        user_id = jsonpath('$.data.userIdentify.identity.identify.id', resp)

        # POST https://api.permutive.com/{param}/events (endp 64)
        qstr = '?' + urlencode([('enrich', 'false'), ('k', k1)])
        resp = api_permutive_com.post(f'/{param1}/events' + qstr)

    @json_dataset('data/dataset_65.json')
    @clear_session({'spanId': 65})
    def test_065_post_param_internal_errors(self, data_row):
        additional_details, domain, k, k1, param, param1, query, user_agent = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        url = cssselect('html head meta[content] @content', resp)

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        user_id = jsonpath('$.data.userIdentify.identity.identify.id', resp)

        # POST https://api.permutive.com/{param}/internal/errors (endp 65)
        qstr = '?' + urlencode([('k', k1)])
        resp = api_permutive_com.post(f'/{param1}/internal/errors' + qstr)


@data_driven_tests
class Tests_availcarsharing_com(unittest.TestCase):

    @clear_session({'spanId': 1})
    def test_001_get_(self):
        # GET https://availcarsharing.com/ (endp 1)
        availcarsharing_com = get_http_target('TARGET_AVAILCARSHARING_COM', authenticate)
        resp = availcarsharing_com.get('/')

    @clear_session({'spanId': 2})
    def test_002_get_app_callback(self):
        # GET https://availcarsharing.com/app/callback (endp 2)
        availcarsharing_com = get_http_target('TARGET_AVAILCARSHARING_COM', authenticate)
        resp = availcarsharing_com.get('/app/callback')

    @clear_session({'spanId': 3})
    def test_003_get_manifest_webmanifest(self):
        # GET https://availcarsharing.com/manifest.webmanifest (endp 3)
        availcarsharing_com = get_http_target('TARGET_AVAILCARSHARING_COM', authenticate)
        resp = availcarsharing_com.get('/manifest.webmanifest')


@data_driven_tests
class Tests_backend_upapi_net(unittest.TestCase):

    @json_dataset('data/dataset_55.json')
    @clear_session({'spanId': 55})
    def test_055_post_ae(self, data_row):
        adSize, adUnit, adUnitCode, amount, auctionID, bidderExternalID, cv, cv1, dfpAdUnit, pid, pid1, seid, timeout, websiteID = data_row

        # POST https://backend.upapi.net/tc (endp 59)
        backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
        qstr = '?' + urlencode([('cv', cv), ('nr', '1'), ('pid', pid), ('upapi', 'true'), ('z', '1')])
        resp = backend_upapi_net.post('/tc' + qstr)
        creativeID = jsonpath('$.*.id', resp)

        # POST https://backend.upapi.net/ae (endp 55)
        qstr = '?' + urlencode([('cv', cv1), ('nr', '1'), ('pid', pid1), ('seid', seid), ('upapi', 'true')])
        resp = backend_upapi_net.post('/ae' + qstr)

    @json_dataset('data/dataset_56.json')
    @clear_session({'spanId': 56})
    def test_056_post_as(self, data_row):
        auctionID, cv, pid, provider, websiteID = data_row

        # POST https://backend.upapi.net/as (endp 56)
        backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
        qstr = '?' + urlencode([('cv', cv), ('nr', '1'), ('pid', pid), ('upapi', 'true')])
        resp = backend_upapi_net.post('/as' + qstr)

    @json_dataset('data/dataset_57.json')
    @clear_session({'spanId': 57})
    def test_057_get_pv(self, data_row):
        cv, pid, sid, w = data_row

        # GET https://backend.upapi.net/pv (endp 57)
        backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
        qstr = '?' + urlencode([('aa', 'true'), ('br', 'chrome'), ('cv', cv), ('pid', pid), ('r', 'true'), ('rt', '0'), ('sid', sid), ('upapi', 'true'), ('w', w)])
        resp = backend_upapi_net.get('/pv' + qstr)

    @json_dataset('data/dataset_58.json')
    @clear_session({'spanId': 58})
    def test_058_post_r(self, data_row):
        auctionID, bidderExternalID, spaceExternalID, websiteID = data_row

        # POST https://backend.upapi.net/r (endp 58)
        backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
        qstr = '?' + urlencode([('nr', '1'), ('upapi', 'true')])
        resp = backend_upapi_net.post('/r' + qstr)

    @json_dataset('data/dataset_60.json')
    @clear_session({'spanId': 60})
    def test_060_post_v(self, data_row):
        auctionID, bidderExternalID, spaceExternalID, websiteID = data_row

        # POST https://backend.upapi.net/v (endp 60)
        backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
        qstr = '?' + urlencode([('nr', '1'), ('upapi', 'true')])
        resp = backend_upapi_net.post('/v' + qstr)


@data_driven_tests
class Tests_cds_taboola_com(unittest.TestCase):

    @json_dataset('data/dataset_96.json')
    @clear_session({'spanId': 96})
    def test_096_get_(self, data_row):
        _r, k, query = data_row

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        uid = url_part('?ui', jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp))

        # GET https://cds.taboola.com/ (endp 96)
        cds_taboola_com = get_http_target('TARGET_CDS_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('_r', _r), ('uid', uid)])
        resp = cds_taboola_com.get('/' + qstr)


@data_driven_tests
class Tests_drivedrift_zendesk_com(unittest.TestCase):

    @clear_session({'spanId': 23})
    def test_023_get_embeddable_config(self):
        # GET https://drivedrift.zendesk.com/embeddable/config (endp 23)
        drivedrift_zendesk_com = get_http_target('TARGET_DRIVEDRIFT_ZENDESK_COM', authenticate)
        resp = drivedrift_zendesk_com.get('/embeddable/config')

    @json_dataset('data/dataset_24.json')
    @clear_session({'spanId': 24})
    def test_024_get_embeddable_blip(self, data_row):
        data, = data_row

        # GET https://drivedrift.zendesk.com/embeddable_blip (endp 24)
        drivedrift_zendesk_com = get_http_target('TARGET_DRIVEDRIFT_ZENDESK_COM', authenticate)
        qstr = '?' + urlencode([('data', data), ('type', 'pageView')])
        resp = drivedrift_zendesk_com.get('/embeddable_blip' + qstr)


@data_driven_tests
class Tests_events_browsiprod_com(unittest.TestCase):

    @json_dataset('data/dataset_52.json')
    @clear_session({'spanId': 52})
    def test_052_post_events_demand(self, data_row):
        adix, aid, au, bpid, bpvid, d, et, f, h, ill, im, isa, lid, mv, ol, p, param, piv, praw, pt, pv, pvid, pw, r, rc, res, saas, sk, ul, url, vpa, vps, w = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        plid = cssselect('article#F_Content div.block.B6 div.block.B6 div.block.spacer div.block div.element.ghcite.noBottomPadding.no-responsive div.general_banner_ad[data-adunit] @data-adunit', resp)

        # POST https://events.browsiprod.com/events/demand (endp 52)
        events_browsiprod_com = get_http_target('TARGET_EVENTS_BROWSIPROD_COM', authenticate)
        qstr = '?' + urlencode([('p', p)])
        resp = events_browsiprod_com.post('/events/demand' + qstr)

    @json_dataset('data/dataset_53.json')
    @clear_session({'spanId': 53})
    def test_053_post_events_supply(self, data_row):
        aid, bpvid, crs, d, et, grs, ie, k, mch, mcs, mcw, mi, mv, p, pl, pvid, pw, query, res, rsn, sf, sid, sk, sl, ua, uid, url = data_row

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        r = jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp)

        # POST https://events.browsiprod.com/events/supply (endp 53)
        events_browsiprod_com = get_http_target('TARGET_EVENTS_BROWSIPROD_COM', authenticate)
        qstr = '?' + urlencode([('p', p)])
        resp = events_browsiprod_com.post('/events/supply' + qstr)


@data_driven_tests
class Tests_la_sync_taboola_com(unittest.TestCase):

    @json_dataset('data/dataset_89.json')
    @clear_session({'spanId': 89})
    def test_089_get_sg_google_network_vg_id_rtb(self, data_row):
        content_id, redir = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://la-sync.taboola.com/sg/google-network/{vg_id}/rtb (endp 89)
        la_sync_taboola_com = get_http_target('TARGET_LA_SYNC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('orig', 'trc'), ('redir', redir)])
        resp = la_sync_taboola_com.get(f'/sg/google-network/{vg_id}/rtb' + qstr)

    @json_dataset('data/dataset_91.json')
    @clear_session({'spanId': 91})
    def test_091_get_sg_pulsepointrtb_network_vg_id_rtb_h_(self, data_row):
        content_id, pid, pid1, rurl = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://bh.contextweb.com/bh/rtset (endp 82)
        bh_contextweb_com = get_http_target('TARGET_BH_CONTEXTWEB_COM', authenticate)
        qstr = '?' + urlencode([('ev', '1'), ('orig', 'trc'), ('pid', pid), ('rurl', rurl)])
        resp = bh_contextweb_com.get('/bh/rtset' + qstr)
        taboola_hm = get_data_from_cookie('V')

        # GET https://la-sync.taboola.com/sg/pulsepointrtb-network/{vg_id}/rtb-h/ (endp 91)
        la_sync_taboola_com = get_http_target('TARGET_LA_SYNC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('ev', '1'), ('orig', 'trc'), ('pid', pid1), ('taboola_hm', taboola_hm)])
        resp = la_sync_taboola_com.get(f'/sg/pulsepointrtb-network/{vg_id}/rtb-h/' + qstr)


@data_driven_tests
class Tests_match_taboola_com(unittest.TestCase):

    @json_dataset('data/dataset_94.json')
    @clear_session({'spanId': 94})
    def test_094_get_sg_mediaforcebidder_network_param_rtb_h(self, data_row):
        content_id, = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)
        param = get_data_from_header('vg_id', resp)

        # GET https://rtb.mfadsrvr.com/sync (endp 85)
        rtb_mfadsrvr_com = get_http_target('TARGET_RTB_MFADSRVR_COM', authenticate)
        qstr = '?' + urlencode([('ssp', 'taboola')])
        resp = rtb_mfadsrvr_com.get('/sync' + qstr)
        taboola_hm = url_part('?taboola_hm', get_data_from_header('location', resp))

        # GET https://trc.taboola.com/sg/mediaforcebidder-network/{vg_id}/rtb-h (endp 77)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/mediaforcebidder-network/{vg_id}/rtb-h' + qstr)
        query = url_part('?query', get_data_from_header('location', resp))
        tbid = get_data_from_cookie('t_gid')

        # GET https://match.taboola.com/sg/mediaforcebidder-network/{param}/rtb-h (endp 94)
        match_taboola_com = get_http_target('TARGET_MATCH_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('isDirect', '0'), ('query', query), ('taboola_hm', taboola_hm), ('tbid', tbid)])
        resp = match_taboola_com.get(f'/sg/mediaforcebidder-network/{param}/rtb-h' + qstr)


@data_driven_tests
class Tests_match_zorosrv_com(unittest.TestCase):

    @json_dataset('data/dataset_95.json')
    @clear_session({'spanId': 95})
    def test_095_get_match(self, data_row):
        content_id, excid, taboola_hm = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://rtb.mfadsrvr.com/sync (endp 85)
        rtb_mfadsrvr_com = get_http_target('TARGET_RTB_MFADSRVR_COM', authenticate)
        qstr = '?' + urlencode([('ssp', 'taboola')])
        resp = rtb_mfadsrvr_com.get('/sync' + qstr)
        extuid = url_part('?taboola_hm', get_data_from_header('location', resp))
        taboola_hm = url_part('?taboola_hm', get_data_from_header('location', resp))

        # GET https://trc.taboola.com/sg/mediaforcebidder-network/{vg_id}/rtb-h (endp 77)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/mediaforcebidder-network/{vg_id}/rtb-h' + qstr)
        query = url_part('?query', get_data_from_header('location', resp))

        # GET https://la-sync.taboola.com/sg/mediamath-ssp-network/{vg_id}/rtb-h/ (endp 90)
        la_sync_taboola_com = get_http_target('TARGET_LA_SYNC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = la_sync_taboola_com.get(f'/sg/mediamath-ssp-network/{vg_id}/rtb-h/' + qstr)
        tabid = get_data_from_cookie('t_gid')

        # GET https://match.zorosrv.com/match (endp 95)
        match_zorosrv_com = get_http_target('TARGET_MATCH_ZOROSRV_COM', authenticate)
        qstr = '?' + urlencode([('excid', excid), ('extuid', extuid), ('query', query), ('tabid', tabid)])
        resp = match_zorosrv_com.get('/match' + qstr)


@data_driven_tests
class Tests_nr_events_taboola_com(unittest.TestCase):

    @json_dataset('data/dataset_71.json')
    @clear_session({'spanId': 71})
    def test_071_get_newsroom_1_0_param_get_action(self, data_row):
        page_dashboard, page_template, param, param1, ui, view_id = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        url = cssselect('html head meta[content] @content', resp)

        # GET https://nr-events.taboola.com/newsroom/1.0/{param}/get-action (endp 71)
        nr_events_taboola_com = get_http_target('TARGET_NR_EVENTS_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('page.dashboard', page_dashboard), ('page.template', page_template), ('page.url', url), ('ui', ui), ('view.id', view_id)])
        resp = nr_events_taboola_com.get(f'/newsroom/1.0/{param1}/get-action' + qstr)

    @json_dataset('data/dataset_72.json')
    @clear_session({'spanId': 72})
    def test_072_get_newsroom_1_0_param_notify_impression(self, data_row):
        page_dashboard, page_template, param, param1, ui, view_id = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        url = cssselect('html head meta[content] @content', resp)

        # GET https://nr-events.taboola.com/newsroom/1.0/{param}/notify-impression (endp 72)
        nr_events_taboola_com = get_http_target('TARGET_NR_EVENTS_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('page.dashboard', page_dashboard), ('page.template', page_template), ('page.url', url), ('ui', ui), ('view.id', view_id)])
        resp = nr_events_taboola_com.get(f'/newsroom/1.0/{param1}/notify-impression' + qstr)


@data_driven_tests
class Tests_pixel_onaudience_com(unittest.TestCase):

    @json_dataset('data/dataset_86.json')
    @clear_session({'spanId': 86})
    def test_086_get_(self, data_row):
        content_id, partner, taboola_hm = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://trc.taboola.com/sg/neustar/{vg_id}/cm (endp 78)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/neustar/{vg_id}/cm' + qstr)
        mapped = get_data_from_cookie('t_gid')

        # GET https://pixel.onaudience.com/ (endp 86)
        pixel_onaudience_com = get_http_target('TARGET_PIXEL_ONAUDIENCE_COM', authenticate)
        qstr = '?' + urlencode([('mapped', mapped), ('partner', partner)])
        resp = pixel_onaudience_com.get('/' + qstr)


@data_driven_tests
class Tests_profile_goavail_io(unittest.TestCase):

    @clear_session({'spanId': 27})
    def test_027_get_api_v1_profile(self):
        # GET https://profile.goavail.io/api/v1/profile (endp 27)
        profile_goavail_io = get_http_target('TARGET_PROFILE_GOAVAIL_IO', authenticate)
        resp = profile_goavail_io.get('/api/v1/profile')

    @clear_session({'spanId': 28})
    def test_028_get_api_v1_profile_cards(self):
        # GET https://profile.goavail.io/api/v1/profile/cards (endp 28)
        profile_goavail_io = get_http_target('TARGET_PROFILE_GOAVAIL_IO', authenticate)
        resp = profile_goavail_io.get('/api/v1/profile/cards')

    @clear_session({'spanId': 29})
    def test_029_get_api_v1_profile_credits(self):
        # GET https://profile.goavail.io/api/v1/profile/credits (endp 29)
        profile_goavail_io = get_http_target('TARGET_PROFILE_GOAVAIL_IO', authenticate)
        resp = profile_goavail_io.get('/api/v1/profile/credits')


@data_driven_tests
class Tests_sb_scorecardresearch_com(unittest.TestCase):

    @json_dataset('data/dataset_73.json')
    @clear_session({'spanId': 73})
    def test_073_get_b(self, data_row):
        c1, c2, c3, cv, k, ns__t, ns_c, query = data_row

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        c7 = jsonpath('$.data.userEvents.events.[*].properties.desturl', resp)
        c8 = jsonpath('$.data.userEvents.events.[*].properties.utitle', resp)
        c9 = jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp)

        # GET https://sb.scorecardresearch.com/b (endp 73)
        sb_scorecardresearch_com = get_http_target('TARGET_SB_SCORECARDRESEARCH_COM', authenticate)
        qstr = '?' + urlencode([('c1', c1), ('c2', c2), ('c3', c3), ('c7', c7), ('c8', c8), ('c9', c9), ('cv', cv), ('ns__t', ns__t), ('ns_c', ns_c)])
        resp = sb_scorecardresearch_com.get('/b' + qstr)


@data_driven_tests
class Tests_server_exposebox_com(unittest.TestCase):

    @json_dataset('data/dataset_44.json')
    @clear_session({'spanId': 44})
    def test_044_get_dmp_iftags(self, data_row):
        c, = data_row

        # GET https://server.exposebox.com/dmp/iftags (endp 44)
        server_exposebox_com = get_http_target('TARGET_SERVER_EXPOSEBOX_COM', authenticate)
        qstr = '?' + urlencode([('c', c)])
        resp = server_exposebox_com.get('/dmp/iftags' + qstr)

    @json_dataset('data/dataset_45.json')
    @clear_session({'spanId': 45})
    def test_045_get_layouts_(self, data_row):
        cb, cid, id_ = data_row

        # GET https://server.exposebox.com/layouts/ (endp 45)
        server_exposebox_com = get_http_target('TARGET_SERVER_EXPOSEBOX_COM', authenticate)
        qstr = '?' + urlencode([('cb', cb), ('cid', cid), ('id', id_)])
        resp = server_exposebox_com.get('/layouts/' + qstr)

    @json_dataset('data/dataset_46.json')
    @clear_session({'spanId': 46})
    def test_046_get_placement_iframe_html(self, data_row):
        c, clicktr, p, ph, pw = data_row

        # GET https://server.exposebox.com/placement-iframe.html (endp 46)
        server_exposebox_com = get_http_target('TARGET_SERVER_EXPOSEBOX_COM', authenticate)
        qstr = '?' + urlencode([('c', c), ('clicktr', clicktr), ('p', p), ('ph', ph), ('pw', pw)])
        resp = server_exposebox_com.get('/placement-iframe.html' + qstr)


@data_driven_tests
class Tests_trc_taboola_com(unittest.TestCase):

    @json_dataset('data/dataset_76.json')
    @clear_session({'spanId': 76})
    def test_076_get_sg_google_network_vg_id_rtb_h_(self, data_row):
        content_id, taboola_hm = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://trc.taboola.com/sg/google-network/{vg_id}/rtb-h/ (endp 76)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('google_cver', '1'), ('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/google-network/{vg_id}/rtb-h/' + qstr)

    @json_dataset('data/dataset_79.json')
    @clear_session({'spanId': 79})
    def test_079_get_sg_storygize_network_vg_id_rtb_h(self, data_row):
        content_id, endDate, endDate1, includeRaf, perPage, startDate, startDate1, taboola_hm = data_row

        # GET https://api.goavail.io/api/v1/locations/airports (endp 14)
        api_goavail_io = get_http_target('TARGET_API_GOAVAIL_IO', authenticate)
        resp = api_goavail_io.get('/api/v1/locations/airports')
        locationId = jsonpath('$.items.[*].locationId', resp)

        # POST https://api.goavail.io/api/v1/locations/{locationId}/vehicle-categories/search (endp 13)
        resp = api_goavail_io.post(f'/api/v1/locations/{locationId}/vehicle-categories/search')
        categoryId = jsonpath('$.[*].categoryId', resp)

        # POST https://api.goavail.io/api/v1/bookings/prices-estimate (endp 12)
        resp = api_goavail_io.post('/api/v1/bookings/prices-estimate')

        # GET https://api.goavail.io/api/v1/locations (endp 15)
        qstr = '?' + urlencode([('perPage', perPage)])
        resp = api_goavail_io.get('/api/v1/locations' + qstr)

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://trc.taboola.com/sg/storygize-network/{vg_id}/rtb-h (endp 79)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/storygize-network/{vg_id}/rtb-h' + qstr)

    @json_dataset('data/dataset_80.json')
    @clear_session({'spanId': 80})
    def test_080_get_sg_thetradedesk_network_vg_id_rtb_h_(self, data_row):
        content_id, taboola_hm = data_row

        # GET https://www.ynet.co.il/ticker/flash/breakingnews.html (endp 40)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('content_id', content_id)])
        resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
        vg_id = get_data_from_header('vg_id', resp)

        # GET https://trc.taboola.com/sg/thetradedesk-network/{vg_id}/rtb-h/ (endp 80)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('taboola_hm', taboola_hm)])
        resp = trc_taboola_com.get(f'/sg/thetradedesk-network/{vg_id}/rtb-h/' + qstr)


@data_driven_tests
class Tests_up9_atlassian_net(unittest.TestCase):

    @json_dataset('data/dataset_109.json')
    @clear_session({'spanId': 109})
    def test_109_get_gateway_api_notification_log_api_2_notifications_count_unseen(self, data_row):
        cloudId, = data_row

        # GET https://up9.atlassian.net/gateway/api/notification-log/api/2/notifications/count/unseen (endp 109)
        up9_atlassian_net = get_http_target('TARGET_UP9_ATLASSIAN_NET', authenticate)
        qstr = '?' + urlencode([('cloudId', cloudId), ('currentCount', '0'), ('source', 'atlaskitNotificationLogClient')])
        resp = up9_atlassian_net.get('/gateway/api/notification-log/api/2/notifications/count/unseen' + qstr)

    @json_dataset('data/dataset_110.json')
    @clear_session({'spanId': 110})
    def test_110_get_rest_api_2_attachment_read_issue_param_credentials(self, data_row):
        maxTokenLength, param = data_row

        # GET https://up9.atlassian.net/rest/api/2/attachment/read/issue/{param}/credentials (endp 110)
        up9_atlassian_net = get_http_target('TARGET_UP9_ATLASSIAN_NET', authenticate)
        qstr = '?' + urlencode([('maxTokenLength', maxTokenLength)])
        resp = up9_atlassian_net.get(f'/rest/api/2/attachment/read/issue/{param}/credentials' + qstr)


@data_driven_tests
class Tests_www_ynet_co_il(unittest.TestCase):

    @json_dataset('data/dataset_33.json')
    @clear_session({'spanId': 33})
    def test_033_get_Ext_Comp_Ticker_param1_param2(self, data_row):
        param, param1 = data_row

        # GET https://www.ynet.co.il/Ext/Comp/Ticker/{param1}/{param2} (endp 33)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('js', '1')])
        resp = www_ynet_co_il.get(f'/Ext/Comp/Ticker/{param}/{param1}' + qstr)

    @json_dataset('data/dataset_35.json')
    @clear_session({'spanId': 35})
    def test_035_get_YediothPortal_Ext_Comp_Teaser_MarketSchedual_New_param1_param2(self, data_row):
        param, param1 = data_row

        # GET https://www.ynet.co.il/YediothPortal/Ext/Comp/Teaser/MarketSchedual_New/{param1}/{param2} (endp 35)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/YediothPortal/Ext/Comp/Teaser/MarketSchedual_New/{param}/{param1}')

    @json_dataset('data/dataset_38.json')
    @clear_session({'spanId': 38})
    def test_038_get_iphone_json_api_talkbacks_list_href_end_to_start_0(self, data_row):
        param, = data_row

        # GET https://www.ynet.co.il/home/{param} (endp 37)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        resp = www_ynet_co_il.get(f'/home/{param}')
        href = url_part('/4', cssselect('article#F_Content div.block.B6 div.block.B6 div.block.B3 div.block.B3 div.element.B3.ghcite.noBottomPadding div div.cell.cshort.layout1 a[href] @href', resp))

        # GET https://www.ynet.co.il/iphone/json/api/talkbacks/list/{href}/end_to_start/0 (endp 38)
        resp = www_ynet_co_il.get(f'/iphone/json/api/talkbacks/list/{href}/end_to_start/0')

    @json_dataset('data/dataset_39.json')
    @clear_session({'spanId': 39})
    def test_039_get_sport_article_location(self, data_row):
        cpb, cv, ii, k, li, msg, param, param1, pc, pi, ppb, query, r, ri, sd, sig, tim, type_, url = data_row

        # POST https://api.permutive.com/graphql (endp 62)
        api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
        qstr = '?' + urlencode([('k', k)])
        resp = api_permutive_com.post('/graphql' + qstr)
        dest_url = url_part('/1', jsonpath('$.data.userEvents.events.[*].properties.dest_url', resp))

        # GET https://trc-events.taboola.com/{dest_url}/log/2/debug (endp 97)
        trc_events_taboola_com = get_http_target('TARGET_TRC_EVENTS_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('cv', cv), ('id', str(random.randint(1107, 9319))), ('idx', 'pc'), ('lt', 'deflated'), ('msg', msg), ('pc', pc), ('st', '1'), ('tim', tim), ('type', type_)])
        resp = trc_events_taboola_com.get(f'/{dest_url}/log/2/debug' + qstr)
        ui = get_data_from_cookie('t_gid')

        # GET https://trc.taboola.com/{param1}/log/{param2}/click (endp 81)
        trc_taboola_com = get_http_target('TARGET_TRC_TABOOLA_COM', authenticate)
        qstr = '?' + urlencode([('cpb', cpb), ('ii', ii), ('it', 'text'), ('li', li), ('lti', 'deflated'), ('pi', pi), ('ppb', ppb), ('pt', 'text'), ('r', r), ('ri', ri), ('sd', sd), ('sig', sig), ('ui', ui), ('url', url), ('vi', str(int(time.time() * 1000)))])
        resp = trc_taboola_com.get(f'/{param}/log/{param1}/click' + qstr)
        location = url_part('/3', get_data_from_header('location', resp))

        # GET https://www.ynet.co.il/sport/article/{location} (endp 39)
        www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
        qstr = '?' + urlencode([('utm_medium', 'organic'), ('utm_source', 'Taboola_internal')])
        resp = www_ynet_co_il.get(f'/sport/article/{location}' + qstr)


@data_driven_tests
class Tests_z_ynet_co_il(unittest.TestCase):

    @json_dataset('data/dataset_47.json')
    @clear_session({'spanId': 47})
    def test_047_get_fast_content_param_coronavirus_coronaviruId(self, data_row):
        coronaviruId, param = data_row

        # GET https://z.ynet.co.il/fast/content/{param}/coronavirus/{coronaviruId} (endp 47)
        z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
        resp = z_ynet_co_il.get(f'/fast/content/{param}/coronavirus/{coronaviruId}')

    @json_dataset('data/dataset_48.json')
    @clear_session({'spanId': 48})
    def test_048_get_mShort_commerce_param_YnetShopsIframe(self, data_row):
        param, = data_row

        # GET https://z.ynet.co.il/mShort/commerce/{param}/YnetShopsIframe (endp 48)
        z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
        resp = z_ynet_co_il.get(f'/mShort/commerce/{param}/YnetShopsIframe')

    @json_dataset('data/dataset_49.json')
    @clear_session({'spanId': 49})
    def test_049_get_short_content_param_NewsletterIframe_(self, data_row):
        param, = data_row

        # GET https://z.ynet.co.il/short/content/{param}/NewsletterIframe/ (endp 49)
        z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
        resp = z_ynet_co_il.get(f'/short/content/{param}/NewsletterIframe/')
