import os

def create_project_dir(project_name):
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(os.path.join(project_name, project_name), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'tests'), exist_ok=True)

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def scaffold_project(project_name):
    create_project_dir(project_name)
    create_file(os.path.join(project_name, 'setup.py'), 'from setuptools import setup\n\nsetup()\n')
    create_file(os.path.join(project_name, 'README.md'), '# ' + project_name + '\n')
    create_file(os.path.join(project_name, '.gitignore'), '*.pyc\n__pycache__\n')
    create_file(os.path.join(project_name, project_name, '__init__.py'), '')
    create_file(os.path.join(project_name, project_name, 'main.py'), '')
    create_file(os.path.join(project_name, 'tests', '__init__.py'), '')
    create_file(os.path.join(project_name, 'tests', 'test_main.py'), '')

scaffold_project('mlops-task-1')


