import os

#what email did you use for your mongodb account?
#what password did you use?

def getSecrets():
   secrets = {
       'MONGO_HOST':"",
       'MONGO_DB_NAME':"",
       'GOOGLE_CLIENT_ID': "",
       'GOOGLE_CLIENT_SECRET':"",
       'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
       'MY_EMAIL_ADDRESS':""
       }
   return secrets
