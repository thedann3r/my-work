import os
import json
import base64
import datetime
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
shortcode = os.getenv('SHORTCODE')
passkey = os.getenv('PASSKEY')
callback_url = "https://0e87-197-248-19-111.ngrok-free.app/mpesa/callback"

@app.route('/mpesa/pay', methods = ['POST'])
def mpesa_pay():
    phone_number = request.json.get('phone_number')
    amount = request.json.get('amount')

    access_token = get_access_token()
    if not access_token:
        return jsonify({'error' : 'Failed to get mpesa access token!'}), 500
    
    headers = {
        'Authorization' : f'Bearer {access_token}',
        'Content-Type' : 'application/json'
    }

    timestamp = get_timestamp()
    print(f"Generated Timestamp: {timestamp}")
    password = generate_password(shortcode, passkey, timestamp)

    payload = {
        "BusinessShortCode" : shortcode,
        "Password" : password,
        "Timestamp" : timestamp,
        "TransactionType" : "CustomerPayBillOnline",
        "Amount" : amount,
        "PartyA" : phone_number,
        "PartyB" : shortcode,
        "PhoneNumber" : phone_number,
        "CallBackURL" : callback_url,
        "AccountReference" : "12345678",
        "TransactionDesc" : "Payment for abc"
    }

    stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    response = requests.post(stk_push_url, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify({'message' : 'STK push initiated successfully', "data": response.json()}), 200
    else:
        return jsonify({'error' : 'Failed to initiate STK push', 'data': response.json()}), 500
    
@app.route('/mpesa/callback', methods = ['POST'])
def mpesa_callback():
    data = request.get_json()

    with open('mpesa_callback.log', 'a') as log_file:
        log_file.write(json.dumps(data, indent=4) + '\n\n')

    try:
        result_code = data['Body']['stkCallback']['ResultCode']
        result_desc = data['Body']['stkCallback']['ResultDesc']

        if result_code == 0:
            callback_metadata = data['Body']['stkCallback']['CallbackMetadata']['Item']
            amount = next(item['Value'] for item in callback_metadata if item['Name'] == 'Amount')
            mpesa_receipt_number = next(item['Value'] for item in callback_metadata if item['Name'] == 'MpesaReceiptNumber')
            phone_number = next(item['Value'] for item in callback_metadata if item['Name'] == 'PhoneNumber')

            payment_status = {
                'status' : 'success',
                'amount' : amount,
                'receipt' : mpesa_receipt_number,
                'phone' : phone_number,
                'message' : 'Payment received successfully!'
            }

        else:
            payment_status = {
                'status' : 'Failed',
                'message' : result_desc
            }
        return jsonify ({'message' : 'Callback received!'}), 200

    except KeyError:
        return jsonify ({'error' : 'invalid callback data'}), 400
    
def get_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    return response.json().get('access_token') if response.status_code == 200 else None

def generate_password(shortcode, passkey, timestamp):
    data_to_encode = f'{shortcode}{passkey}{timestamp}'
    return base64.b64encode(data_to_encode.encode()).decode('utf-8')

def get_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# timestamp = get_timestamp()
# print(f"Timestamp: {timestamp}")

if __name__ == '__main__':
    app.run(debug = True)