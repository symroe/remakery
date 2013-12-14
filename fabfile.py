from fabric.api import run, env, sudo, cd

env.hosts = ['remakery.talusdesign.co.uk:7822',]
# env.user = "remakery"
env.config_path = "config"
env.depoy_path = "/var/www/remakery/"

def service(name, command='restart'):
    sudo('service %s %s' % (name, command))

def configure_nginx():
    update_from_git()
    config_file = "%s%s/nginx" % (env.depoy_path, env.config_path)
    sudo('cp -f %s /etc/nginx/sites-available/' % config_file)
    service('nginx')

def update_from_git():
    with cd(env.depoy_path):
        run("git pull origin master")