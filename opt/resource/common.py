import json
import sys
import tempfile

VERSION = '1.0'

def get_payload():
    payload = json.load(sys.stdin)
    _, fname = tempfile.mkstemp()
    print("Logging payload to {}".format(fname), file=sys.stderr)
    print("Payload: {}".format(payload), file=sys.stderr)
    with open(fname, 'w') as fp:
        fp.write(json.dumps(payload))
    return payload

def get_version():
	return VERSION
