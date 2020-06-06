import glob
import importlib
import os

page_paths = glob.glob('pages/**/*.py', recursive=True)

page_templates = []

for page_path in page_paths:
  python_module = page_path.replace('/', '.').replace('.py', '')
  output_path = page_path.replace('pages', 'dist').replace('.py', '.html')

  template = {
    'module': importlib.import_module(python_module),
    'output_path': output_path
  }

  page_templates.append(template)

for page_template in page_templates:
  if not os.path.exists(os.path.dirname(page_template.get('output_path'))):
    os.mkdir(os.path.dirname(page_template.get('output_path')))

  with open(os.getcwd() + '/' + page_template.get('output_path'), 'w+') as file:
    file.write(page_template['module'].template())
