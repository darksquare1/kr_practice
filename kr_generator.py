import os
import random
import subprocess
import sys

class KrGenerator:
    def __init__(self, template):
        self.template_path = self.resource_path(template)
        with open(self.template_path, 'r', encoding='utf-8') as f:
            self.template = f.read()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def _create_random_tasks(self):
        import tasks
        self.tasks = []
        for task in tasks.ALL_TASKS:
            self.tasks.append(random.choice(task))

    def _fill_template(self):
        for ind, task in enumerate(self.tasks, 1):
            self.template = self.template.replace(f'%TASK_{ind}%', f'\\item {task}')

    def _create_pdf(self):
        output_path = self.resource_path('files/kr.tex')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.template)
        subprocess.run(['pdflatex', '-output-directory', self.resource_path('files'), output_path])
        no_need_files = [self.resource_path(f'files/kr.{ext}') for ext in ['aux', 'log', 'out', 'tex']]
        for file in no_need_files:
            if os.path.exists(file):
                os.remove(file)

    def _create_tasks_pdf(self):
        self._create_random_tasks()
        self._fill_template()
        self._create_pdf()

    def __call__(self):
        self._create_tasks_pdf()