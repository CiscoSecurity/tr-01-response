import requests

access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example

url = 'https://visibility.amp.cisco.com/iroh/iroh-response/respond/trigger/AMP%20for%20Endpoints/amp-remove-sha256-scd'

# EXAMPLE:
# parameters = {'list':'e773a9eb-296c-40df-98d8-bed46322589d',
#               'observable_type':'sha256',
#               'observable_value':'d15766ead5d8ffe68fd96d4bda75c07378fc74f76e251ae6631f4ec8226d2bcb'}

parameters = {'list':'<FILE_LIST_GUID>',
              'observable_type':'sha256',
              'observable_value':'<SHA256>'}

headers = {'Authorization':'Bearer {}'.format(access_token)}

response = requests.post(url, headers=headers, params=parameters)

print(response.json())
