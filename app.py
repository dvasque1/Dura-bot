
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return '✅ DURA Bot está activo y escuchando mensajes de Twilio'
    return 'Mensaje recibido correctamente por DURA Bot'

if __name__ == '__main__':
    app.run()
