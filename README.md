# Chatbot

Este repositório contém o código-fonte para um chatbot desenvolvido utilizando a API do ChatGPT e integração com o WhatsApp via Twilio.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.x
- Conta na [OpenAI](https://beta.openai.com/signup/)
- Conta no [Twilio](https://www.twilio.com/)

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/kadoexec/ChatBot_IA.git
cd chatbot-doces-vermelhos
pip install -r requirements.txt

### Configurações das APIs
openai.api_key = 'SUA_CHAVE_API_OPENAI'
twilio_account_sid = 'SUA_CONTA_SID_TWILIO'
twilio_auth_token = 'SEU_AUTH_TOKEN_TWILIO'
twilio_whatsapp_number = 'SEU_NUMERO_WHATSAPP_TWILIO'

### Execução
Inicie o servidor Flask:

bash
Copiar código
python chatbot.py
Configure o webhook no Twilio para apontar para o endpoint do Flask (por exemplo, http://seu_dominio.com/webhook).
