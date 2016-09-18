#My first web app! By <strong>hamza</strong>.root@ed6a0fc2e0b1:/# c
#bash: c: command not found
#root@ed6a0fc2e0b1:/# cat bott.py
import os
from bottle import route, run, template

index_html = '''My first web app! By <strong>{{ author }}</strong>.'''


@route('/')
def index():
    return template(index_html, author='Real Python')


@route('/name/<name>')
def name(name):
    return template(index_html, author=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
