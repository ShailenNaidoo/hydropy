import glob
import importlib
import os

def get_page_templates():
  page_paths = glob.glob('pages/**/*.py', recursive=True)

  page_templates = []

  for page_path in page_paths:
    python_module = page_path.replace('/', '.').replace('.py', '')
    output_path = page_path.replace('pages', 'dist').replace('.py', '.html')

    module = importlib.import_module(python_module)

    template_alt = lambda *args: ''
    data_alt = lambda *args: {}

    # module['template'] = module['template'] or template_alt
    # module['data'] = module['data'] or data_alt

    template = {
      'module': {
        'template': module.template if hasattr(module, 'template') else template_alt,
        'data': module.data if hasattr(module, 'data') else data_alt
      },
      'output_path': output_path
    }

    page_templates.append(template)

    return page_templates

def generate_and_save_page_templates(page_templates):
  for page_template in page_templates:
    if not os.path.exists(os.path.dirname(page_template.get('output_path'))):
      os.mkdir(os.path.dirname(page_template.get('output_path')))

    with open(os.getcwd() + '/' + page_template.get('output_path'), 'w+') as file:
      file.write(page_template['module']['template'](page_template['module']['data']()))

generate_and_save_page_templates(
  get_page_templates()
)