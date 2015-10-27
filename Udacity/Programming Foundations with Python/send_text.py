from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc3e784dfec9c8af0a16959f2a2f11e17"
auth_token  = "34b6e22741f3b7211299b2d250e5bdd2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi buddy!",
    to="+37525",    # Replace with your phone number
    from_="+14794372872") # Replace with your Twilio number
print (message.sid)