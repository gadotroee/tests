from up9lib import *

"""
This is the file to inject authentication instructions into tests.
Each test will call `authenticate()` function, passing instance of `TargetService` object into it. 
There will be made one call per service, per each test case. 
You can use `if target_key=='...'` logic when you want to have different authentication for different services. 
Look below for examples of coding authentication of different types: header, cookie, OAuth.
"""


def authenticate(target_key: str, target: TargetService):
    # Uncomment one of below lines and customize corresponding function:
    #
    # authenticate_header(target)
    # authenticate_cookie(target)
    # authenticate_oauth(target)
    if target_key == 'TARGET__5142311_FLS_DOUBLECLICK_NET':
        pass
    elif target_key == 'TARGET_ADSERVICE_GOOGLE_COM':
        pass
    elif target_key == 'TARGET_API_IAM_INTERCOM_IO':
        pass
    elif target_key == 'TARGET_AUTH_STG_TESTR_IO':
        pass
    elif target_key == 'TARGET_BAT_BING_COM':
        pass
    elif target_key == 'TARGET_HTTPBIN_ORG':
        pass
    elif target_key == 'TARGET_IB_ADNXS_COM':
        pass
    elif target_key == 'TARGET_OGS_GOOGLE_COM':
        pass
    elif target_key == 'TARGET_STATS_G_DOUBLECLICK_NET':
        pass
    elif target_key == 'TARGET_STG_TESTR_IO':
        pass
    elif target_key == 'TARGET_TRCC_API_SERVICE_TRADMIN':
        pass
    elif target_key == 'TARGET_TRDEMO_STG_TESTR_IO':
        pass
    elif target_key == 'TARGET_WIDGET_INTERCOM_IO':
        pass
    elif target_key == 'TARGET_WWW_GOOGLE_ANALYTICS_COM':
        pass
    elif target_key == 'TARGET_WWW_GOOGLE_COM':
        pass
    elif target_key == 'TARGET_WWW_IL_KAYAK_COM':
        pass
    elif target_key == 'TARGET_WWW_KAYAK_COM':
        pass
    else:
        pass



def authenticate_header(target: TargetService):
    # Header authentication is very simple,
    # you just need to call `target.additional_headers()`
    # and pass dictionary of headers to it.
    # These headers will be used for all API calls for corresponding service.

    token = "ABCDEF...XYZ"  # for static header value

    # token = os.environ.get("ENV_VAR")  # to load key from env variable

    # If your token is stored inside file, use below code to load it
    # with open("filename") as fp:
    #    token = fp.read()

    # set the header           <     name    >: <      value    >
    target.additional_headers({"Authorization": "Bearer " + token})
    # target.additional_headers({"X-Api-Key": token})  # any header can be set like that


def authenticate_cookie(target: TargetService):
    # All `TargetService` instances share same cookie storage
    # Just make series of requests that sets desired cookie. Like example below:

    # we request a "login form" page, if needed
    resp = target.get("/")
    resp.assert_ok()
    additional_key = resp.extract_cssselect("body form input[name='sec_key'] @value")  # taking some data from it

    # assuming this POST request will issue Set-Cookie header
    resp = target.post("/login", data={"login": "user@company.com", "password": "SecrPass", "sec_key": additional_key})
    resp.assert_ok()

    # If you have a cookie obtained somehow differently and want to add it into session storage, use this:
    merge_cookies_into_session({"name": "sessionID", "value": "21312434",
                                "path": "/", "domain": "myserver.com", "secure": True})


def authenticate_oauth(target: TargetService):
    # OAuth authentication schemas are usually implemented with a series of requests
    # Good implementation for it is available here:
    # https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#web-application-flow

    client_id = r'your_client_id'
    client_secret = r'your_client_secret'
    redirect_uri = 'https://your.callback/uri'
    scope = ['scope1', 'scope2']

    from requests_oauthlib import OAuth2Session
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    # ... some OAuth flow calls go here, depends on flow specifics ...

    token = oauth.fetch_token(redirect_uri)  # for example, we fetch Authorization token
    target.additional_headers({"Authorization": "Bearer " + token})

    merge_cookies_into_session(oauth.cookies)  # this is important to import cookies from OAuth, if any


