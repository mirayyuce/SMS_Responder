import os
from flask import Flask, request
from send import AutoAnswer

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    """
        Simple webhook to receive messages
        
        Args:
        Returns:
            Returns 200 if the message received successfully, an error message otherwise.
    """
    
    body = request.get_json()

    try:
        # Answers only inbound messages
        if body['data']['payload']['direction'] == 'inbound':
            
            text = body['data']['payload']['text']
            sender_phone_number = body['data']['payload']['from']['phone_number']

            # Prepares the message and send
            out = AutoAnswer(text, sender_phone_number)
            out.send_message()
    except:
        return  'An error occured'

    return '', 200

if __name__ == "__main__":
    app.run(port=5000)