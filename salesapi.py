import requests
payload = {'username': 'roshanhallo@gmail.com.dev', 'password': 'Salesforce@123TQ3F17leybYgluvBIh1eQujM','grant_type':'password','client_id':'3MVG9G9pzCUSkzZvzbHPoi50yRJf5GOtENNF36FI.cf_apS2uUe1d_fOlw08QHIkGZ1MJDElo2L5cN2SMqgUC','client_secret':'0CE6BAA21BA291BA18286B654D172E09F04F03ACF230B24DD49A2C18C17CA390'}
response_text = requests.post('https://login.salesforce.com/services/oauth2/token', params=payload)
print(response_text.text)

