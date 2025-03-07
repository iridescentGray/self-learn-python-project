from jinja2 import Template

template_file = "template.j2"
output_file = "output.py"

name = "Alan"
age = 25

with open(template_file, "r") as f:
    template_content = f.read()

template = Template("template.j2")
filled_content = template.render(name=name, age=age)

with open(output_file, "w") as f:
    f.write(filled_content)

print("New file generated successfully.")
