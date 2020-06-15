from application import app, db, manager
from www import *
from flask_script import Server, Command
import click

manager.add_command('runserver', Server(host='127.0.0.1', use_reloader=False))


@Command
def print_info():
    click.echo("I am print my flask Info.")


manager.add_command('print', print_info)
from job.launcher import JobLaunch
manager.add_command('runjob', JobLaunch)


def main():
    manager.run()


if __name__ == "__main__":
    # from common.models.user import User
    # db.Model = User
    # db.create_all()
    # app.run(host="127.0.0.1", debug=True)
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
