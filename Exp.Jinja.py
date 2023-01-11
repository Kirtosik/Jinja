from jinja2 import Template

name1 = "Привет {{ name }}"

tm = Template(name1)
msg = tm.render(name="Кирилл")

data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}  
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg2 = tm.render(name="Кирилл")

print(msg, msg2, sep="\n" )