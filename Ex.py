from jinja2 import Template
from markupsafe import escape

link1 = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm = escape(link1)
print(tm)