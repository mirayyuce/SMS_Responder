import telnyx
from configs import Configs

telnyx.api_key = "KEY0177796E2E24B867AEDADB820193C8DC_0bwbJsyPBfUJwqxrlU0mYP"
configs = Configs()

class AutoAnswer():
    """
        Class to generate automatic SMS response.
        
        Args:
            text: Inbound message text
            destination_number: Receiver phone number
    """
    def __init__(self, text, destination_number):
        self.text_received = text   
        self.destination_number = destination_number

    def preprocess_text(self):
        """
            Basic cleaning of the received text. Removes white spaces, and sets the letters to lowercase.
            Args:
            Returns:
        """
        self.text_received = self.text_received.replace(" ", "").lower()

    def create_message_text(self):
        """
            Inspects the received text to prepare the answer
            Args:
            Returns: 
                Returns the matching answer from configs.word_dict. If mathcing not found it returns a fixed message.
        """

        if self.text_received in configs.word_dict:
            return configs.word_dict[self.text_received]
        else:
            return 'Please send either the word ‘pizza’ or ‘ice cream’ for a different response'

    def send_message(self):
        """
            Cleans the received text, prepares the message text and sends the message.
            Args:
            Returns: 
        """
        self.preprocess_text()
        message_text = self.create_message_text()
     
        telnyx.Message.create(
            from_=configs.source_number,
            to=self.destination_number,
            text=message_text,
        )