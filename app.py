from flask import Flask, render_template
app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', token_info=token_info)

@app.route('/news')
def news_page():
    return render_template('news.html', news=news)

@app.route('/token_info')
def token_info_page():
    return render_template('token_info.html', token_info=token_info)

if __name__ == '__main__':
    app.run(debug=True)
