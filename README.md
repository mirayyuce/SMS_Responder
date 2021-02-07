Auto SMS Responder based on the inbound message text. 

1. Go to https://ngrok.com/
     - Signup for free
     - Download the file and unzip it 
     - From the commandline run: ./ngrok http 5000
     - Copy the forwarding address (https://RANDOM_CHARACTERS.ngrok.io)
     - This address is generated randomly each time we run ./ngrok http 5000

2. Go to https://telnyx.com/
     - Signup for free
     - Follow the instructions here: https://developers.telnyx.com/docs/v2/messaging/quickstarts/portal-setup
       - In the portal go to Messaging
       - Under 'Inbound Settings', for 'Send a webhook to this URL:' paste the the ngrok URL: (https://RANDOM_CHARACTERS.ngrok.io/webhooks)
       - Each time we restart the app we need to update this URL in the portal
     - Follow the instructions for Python here: https://developers.telnyx.com/docs/v2/messaging/quickstarts/dev-env-setup

3. Download this repo
     - Go to configs.py
       - Change source_number to Telnyx phone number
       - Add the Telnyx API Key (It is at the portal. Find API Keys in the left frame)
       - Add or remove any word-sentence matching to word_dict. Keys are expected to be alphanumeric without special characters and without spaces, eg: pizza, icecream
          
4. Run ./ngrok http 5000       
5. From another terminal run receiver.py
6. Send a message to the Telnyx number 
7. Receive the answer



