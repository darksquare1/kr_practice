
import subprocess
import os
import random


class KrGenerator:
    def __init__(self, template):
        with open(template, 'r', encoding='utf-8') as f:
            self.template = f.read()

    def _create_random_tasks(self):
        import tasks
        self.tasks = []
        for task in tasks.ALL_TASKS:
            self.tasks.append(random.choice(task))

    def _fill_template(self):
        for ind, task in enumerate(self.tasks):
            self.template = self.template.replace(f'%TASK_{ind}%', f'\\item {task}')

    def _create_pdf(self):
        with open('files/kr.tex', 'w', encoding='utf-8') as f:
            f.write(self.template)
        subprocess.run(['pdflatex', '-output-directory', 'files', 'files/kr.tex'])
        no_need_files = ['files/kr.aux', 'files/kr.log', 'files/kr.out', 'files/kr.tex']
        for file in no_need_files:
            if os.path.exists(file):
                os.remove(file)

    def _create_tasks_pdf(self):
        self._create_random_tasks()
        self._fill_template()
        self._create_pdf()
    def __call__(self):
        self._create_tasks_pdf()


if __name__ == '__main__':
    KrGenerator('files/template.tex')()