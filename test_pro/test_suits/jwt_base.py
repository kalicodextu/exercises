import jwt
import yaml

def get_token_payload(token):
    payload = dict()
    try:
        with open('./data/token/test.conf', 'r') as fp:
            config = yaml.load(fp).get('encryption')
            payload = jwt.decode(token, config.get('key'), config.get('algorithm'))
    except Exception as e:
        raise str(e)
    finally:
        return payload

