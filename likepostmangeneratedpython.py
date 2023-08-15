import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.dropbox.com/oauth2/token"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Authorization"] = "Basic M2Q5enRhZXZxeW81NGJ2OmxxcmVxN3d2YmRiZDNwcQ=="

data = "code=UTpKLfYsy7cAAAAAAAAEJnUxjDjMbqaBVecNk_Yx6DY&grant_type=authorization_code"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

################################################################################################