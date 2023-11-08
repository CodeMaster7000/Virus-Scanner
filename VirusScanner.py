from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint

configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment to setup prefix (e.g. Bearer) for API key:
# configuration.api_key_prefix['Apikey'] = 'Bearer'

api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
input_file = '/path/to/file'
try:
    api_response = api_instance.scan_file(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_file: %s\n." % e)
