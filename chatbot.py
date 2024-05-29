import os
import openai
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Configurar API do OpenAI
openai.api_key = 'SUA_CHAVE_API_OPENAI'

# Configurar API do Twilio
twilio_account_sid = 'SUA_CONTA_SID_TWILIO'
twilio_auth_token = 'SEU_AUTH_TOKEN_TWILIO'
twilio_whatsapp_number = 'SEU_NUMERO_WHATSAPP_TWILIO'
client = Client(twilio_account_sid, twilio_auth_token)

app = Flask(__name__)

def send_greeting():
    greeting_message = (
        "Olá! Bem-vindo à Doces Vermelhos! 🍰\n"
        "Eu sou seu assistente virtual. Como posso ajudar você hoje?\n"
        "1. Ver nosso cardápio\n"
        "2. Fazer um pedido\n"
        "3. Saber sobre nossas promoções\n"
        "4. Falar com um atendente"
    )
    return greeting_message

def get_response_from_chatgpt(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    response = MessagingResponse()
    message = response.message()

    if incoming_msg.lower() in ['oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']:
        message.body(send_greeting())
    else:
        chatgpt_response = get_response_from_chatgpt(incoming_msg)
        message.body(chatgpt_response)
    
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
