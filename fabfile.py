from fabric.api import *

env.user = 'username'
env.password = 'password'
env.parallel = 'True'
env.cwd = '/home/username/'
env.warn_only = 'True'

env.roledefs = {
    'prod': ['127.0.0.1'],
}

project_name = 'myproject'


@roles('prod')
def update():
    with cd(f'~/{project_name}'):
        # run('git reset --hard')
        run('git pull origin master')

        with prefix('source venv/bin/activate'):
            run('pip install -r requirements.txt')
            run('./manage.py migrate')
            run('./manage.py collectstatic --noinput')
            run('./manage.py compilemessages')

        sudo(f'supervisorctl restart {project_name}')
        # sudo('service nginx restart')
