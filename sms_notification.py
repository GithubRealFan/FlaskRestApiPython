from flask import Flask, request
from twilio.rest import Client
import stripe

app = Flask(__name__)

# Set up Stripe API key
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

# Set up Twilio API key
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_client = Client(account_sid, auth_token)

@app.route('/payment', methods=['POST'])
def process_payment():
    # Get amount from request body
    amount = request.json['amount']

    # Create Stripe charge
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        source='tok_visa',  # Replace with actual payment token from client
        description='Payment received.'
    )

    # Send SMS notification
    message = twilio_client.messages.create(
        body=f"New payment of ${amount} received.",
        from_='YOUR_TWILIO_PHONE_NUMBER',
        to='RECIPIENT_PHONE_NUMBER'
    )

    return "Payment processed successfully.", 200

if __name__ == '__main__':
    app.run()
