from __future__ import with_statement
from fabric.api import local, run, cd, env, sudo

env.hosts = ['django@45.55.207.93']
# env.user = 'django'

def deploy():
    code_dir = '/home/django/geo_church'
    with cd(code_dir):
        run('git pull origin master')
        # result = sudo('supervisorctl restart django')
        # print result

