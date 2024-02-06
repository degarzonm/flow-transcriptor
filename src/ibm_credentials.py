
from dotenv import dotenv_values
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def load_credentials():
    """
    Load IBM credentials and create the WebSocket URL.
    """
    env_vars = dotenv_values()
    ibm_key = env_vars.get('IBM_API_KEY')
    ibm_speech_service_id = env_vars.get('IBM_SPEECH_SERVICE_INSTANCE_ID')
    ibm_speech_service_wss = env_vars.get('IBM_SPEECH_SERVICE_REGION')+env_vars.get('IBM_SPEECH_SERVICE_URL')+ibm_speech_service_id
    ibm_lang_model = env_vars.get('IBM_LANG_MODEL')

    iam_authenticator = IAMAuthenticator(ibm_key)
    ibm_websocket_speech_token = iam_authenticator.token_manager.get_token()

    ws_url = "wss://" + ibm_speech_service_wss + "/v1/recognize"
    ws_uri = f"{ws_url}?access_token={ibm_websocket_speech_token}&model={ibm_lang_model}"

    print('URI final: ' + ws_uri[:50] + '....' + ws_uri[-50:])
    
    return ws_uri