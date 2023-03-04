import urllib.request
import json
import os
import ssl
import form as form

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') axzdknd getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
 def llamarservicio():
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "age": form.age,
            "job": form.job,
            "marital": form.marital,
            "education": form.education,
            "default": form.default,
            "housing": form.housing,
            "loan": form.loan,
            "contact": form.contact,
            "month": form.month,
            "duration": int(form.duration),
            "campaign": int(form.campaign),
            "pdays": int(form.pdays),
            "previous": int(form.previous),
            "poutcome": form.poutcome,
            "emp": float(form.rate),
            "cons": float(form.priceIdx),
            "conf": float(form.confIdx),
            "euribor3m": float(form.euribor3m),
            "employed": int(form.employed)
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'https://fca-regression.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = 'AnVcIXbYyV9KbCKmAGmbV2gNhpMAdmXg '
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'fca-deploy2' }

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    return(result)
    print(result)

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))