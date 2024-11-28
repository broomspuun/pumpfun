import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    filename='app.log',  # Имя файла для логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат записи
)

# Данные о токене
token_info = {
    'name': 'MyToken',
    'symbol': 'MTK',
    'total_supply': '1,000,000',
    'current_price': '0.50 USD',
    'whitepaper': 'https://example.com/whitepaper.pdf',
}

# Статичные новости
news = [
    {'title': 'Токен стал доступен на бирже X', 'date': '2024-11-01', 'content': 'Описание новости о листинге.'},
    {'title': 'Предстоящее обновление сети', 'date': '2024-12-01', 'content': 'Что нового в следующем обновлении.'},
]

@app.before_request
def log_request_info():
    """Логирование данных входящих запросов."""
    logging.info(f"Endpoint: {request.endpoint}, Method: {request.method}, Data: {request.get_data(as_text=True)}")

@app.route('/')
def index():
    return render_template('index.html', token_info=token_info)

@app.route('/news')
def news_page():
    return render_template('news.html', news=news)

@app.route('/token_info')
def token_info_page():
    return render_template('token_info.html', token_info=token_info)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No JSON data provided'}), 400
    message = data.get('message', 'No message provided')
    return jsonify({'status': 'success', 'message': f'Ping received: {message}'})

if __name__ == '__main__':
    app.run(debug=True)
