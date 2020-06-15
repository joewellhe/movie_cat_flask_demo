import argparse
import click
import sys
import traceback
import importlib
from flask_script import Command


class JobLaunch(Command):
    """
    Job管理类 提供统一管理task的job命令
    运行方式如下
    python mananger.py runjob -n tesk_demo (job/tasks/task_demo.py)
    """
    capture_all_args = True

    def run(self, *args, **kwargs):
        sys_args = sys.argv[2:]
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('-n', '--name', dest='name', metavar='name', required=True,
                            help='job任务的文件名 不带.py后缀 如 -n=task_demo')
        parser.add_argument('-a', '--act', dest='act', metavar='act', required=False, help='job行为')
        parser.add_argument('-p', '--params', dest='params', metavar='params', nargs="*",
                            required=False, help='其他参数')

        params = parser.parse_args(sys_args)
        if 'name' not in params or not params.name:
            click.echo(self.tips())
            return

        try:
            # from job.tasks.task_demo import TaskDemo
            module_name = 'job.tasks.{}'.format(params.name)
            module = importlib.import_module(module_name)
            module.JobTask().run(params.__dict__)
        except Exception as e:
            traceback.print_exc()

    def tips(self):
        tip_msg = '''
        指定运行的task文件的文件名 不用带.py后缀
        Job运行样例如下 
        python mananger.py runjob -n tasks/tesk_demo (job/tasks/task_demo.py)
        '''
        return tip_msg
