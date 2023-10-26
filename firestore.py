import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# Firebase credentials embedded in the script (replace with your own credentials)
firebase_config = {
  "type": "service_account",
  "project_id": "sjshoppers-60328",
  "private_key_id": "8fec9e9fcbfb9012b40aa7a4ed00a012a429d723",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCUAuwLFfl/A31T\nj/6y2iDgFG0301nMYrVAjaDfp9AT4nKdB+aiThRG4WrHedgCoNl5Y5O+Hd850HEJ\n85SQlDYa+V3ZOUwo5Wk0uljWRxkbWS4lxn4rcD83d8UbDfZYYJ3ezWNjOUgmnhJJ\n3H2eM5KkAufWqMxjyiqhyssjZtHZJaf3uZwkoV76YBsKghTy9bBW4b2n0tXN+QlO\nGmp4R0Vrhape11aUFrQ7GQlHzKpvjh5ZHhrHEQcsMVefbgSnVpUTI4LoPmqz2Y8i\n0e5qlOmy+Tgqh79lYukIfxX4OrO2tM1zHQuqA4SVUJzxhM90pJ/onvdoDFkrl73M\nOil8usFHAgMBAAECggEALqmrLCWN5oa9nLohdNaDFdIqyrZVsbOO7B6akNhxp8s1\nEh+7DQFrsBsCFIhr2wxF89i6a+40AaCe+qGx/VDUq/VhKoo/YgdNf0OenVOF7VLU\n0zD8dwpoy751RD3HI/611tfO1Snqfs5H+sRKUDV3LkECQXEvGujSPvbVyz/vubME\nODN2v588sIi4Mu+Dm7p8FoNLYQ4n+cAVSXiT2STzFxkTdpksyBtEH28QqD7dA9be\nRE2Mo+LJaNu5x7E2Euku79dnL8OlKq+olYAou6wcHZaZfgssdSjqnX1W6pURdB/n\nfqee0eVcrfkfA5OAziDhhPWPIltOs3DcG/XHCcDX2QKBgQDHDEw1hrWg7k6uteP7\nQWfOSzv6syK6e09L48X5RgpcR8T8qiqcB0YcuGzBaioaXi6kPYduWSafk1Wu1fsP\nu57i+tRuCd2t0gCbDZm67cggFvzmM5zV0X3yVajlCCh124zVW8LUMmHt2H+RVHKp\nu4KbzDsALb4gPuO1pN3ZKWmGvwKBgQC+XFZAGdRFf+SJa7j/uhcFGoRm/DoW+aBa\nlypa3DPzHo8hH9xO/L9K0zaN3dOpcMKj/Z50jnvy2URMiv18+doBimMtlcRpXkJz\n3f/nQ95zz5tQ++JQSDd12qcz2CCdImBxL6ErX9Cjv9LcVhmCM7NYUqVsBmQwgJ3b\n5fEYYiMveQKBgQC88kSJbvWM7YqNOCZRBLZIUox+H3vw70rHrFDqnn0JOiuY+ON3\nt0Pr0XmTZHbRDuRRjgK4UjJiulZUn9UyCxT5O8dZKU5gSP/AL/nlQwB8zbWFxCq1\noaZf2sZ3mvXlYuLeSbu4+JaTU7dMupAZ5OBHimfbdJCNRYWckQLyuOfuOwKBgHgf\ntJ3Grtkcl47QV3GocJZb4WlLiSyuYa5I7gVgJ7gndJKmlFOT0vLYzfhAHy0xZuIt\nTSyoLTdWO29B1ixjTlrihSti8wq63JxZXv8FKP9T5uL30BxxNe49CH4CyLHf25QR\nRlcko3hxuBIqkvZCwc3eeVztu5OP1g3J0JZed22hAoGBAIfO0y1N6RY+GtN6YM9r\natyFZjv3IbBLT3+H4wA8kv5NQSKkt1zbZecyp3cu7fvDLDp+twf1UYQgHjM6oY4K\nLlLw5K81eI877XSU5e1zXTml0WHyUVMxgR5iP1zeMm0OLiDwb4RU9kIOSpV24hot\np/bLnIlv1lOoWq3NGMuCywyV\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-al7nd@sjshoppers-60328.iam.gserviceaccount.com",
  "client_id": "102095730702280727268",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-al7nd%40sjshoppers-60328.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
for i in [1,2,4]:
# Initialize Firebase with the embedded credentials


# Reference to the root of your Firebase database
# root_ref = db.reference()
    database = firestore.client()

# Sample data to be stored
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

# You can replace 'your-node' with the desired node where you want to store the data
    dbref=database.collection('testers')

# Set the data in the Firebase database
    dbref.document() .set(data)

    print("Data stored in Firebase.")

# Clean up the Firebase app (optional)
# firebase_admin.delete_app(firebase_admin.get_app())
print('OK')