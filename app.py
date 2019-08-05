from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

app = Flask(__name__)


@app.route('/index')


def index():
    return render_template('home.html')


@app.route('/iPhone/', methods=['POST'])


def iPhone_list():
    page = requests.get('https://everymac.com/systems/apple/ipad/', headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all(id='contentcenter_specs_externalnav_2')
    list = [];
    for title in soup.find_all(id='contentcenter_specs_externalnav_2'):
        list.append(title.text)
    return render_template('home.html', items=list)


if __name__ == "__main__":
    app.run(debug=True)
