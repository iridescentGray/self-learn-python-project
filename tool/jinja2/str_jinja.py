from jinja2 import Template

str = "aijsaodjoiajoidjioasjdoj {{name}}  {{age}}"

name = "Alan"
age = 25

template = Template(str)
filled_content = template.render(name=name, age=age)

print(filled_content)
print("New file generated successfully.")
