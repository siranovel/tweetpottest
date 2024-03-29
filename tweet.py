import os
import urllib.parse as parse
import base64
import requests

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_KEY_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
SIGNATURE_METHOD = 'PLAIN'
tweet = 'New commit pushed! (twitter v2 oauth 1.0a)'
url_text = 'https://api.twitter.com/2/tweets'

def _conv_dict(dict_: dict):
    string = ''
    for key, val in dict_.items():
        string += key + '="' + val + '", '
    return string.rstrip(', ')

def _create_signature():
    clent_id64 = CONSUMER_KEY + ":" + CONSUMER_SECRET
    token_id64 = ACCESS_KEY + ":" + ACCESS_KEY_SECRET
    base_string = clent_id64 
　　　　　　　　　　+ chr(38) 
　　　　　　　　　　+ token_id64
    return base64.b64encode(base_string.encode()).decode()

def _create_authorization_params():
    auth_params = {}
    auth_params['oauth_consumer_key'] = parse.quote(CONSUMER_KEY, safe='')
    auth_params['oauth_token'] = parse.quote(ACCESS_KEY, safe='')
    auth_params['oauth_signature_method'] = SIGNATURE_METHOD
    auth_params['oauth_version'] = '1.0'
    auth_params['oauth_signature'] = _create_signature()

    return auth_params

def _create_authorization_header():
    auth_headr_val = 'OAuth '
    params = _create_authorization_params()
    auth_headr_val += _conv_dict(params)

    return {'Authorization': auth_headr_val}

def main():
    ctx_headers = _create_authorization_header()
    res = requests.post(url_text,
                        headers = ctx_headers,
                        params = {'text': tweet}
    )
    print(res)
    print(res.text)
                        
    
if __name__ == "__main__":
    main()

