from fabric.api import *

def greetings(MSG):
    print(f"Good {MSG}")

def system_info():
    print("Print disk space")
    local("df -h")

    print("Print memory info")
    local("free -m")

    print("Print uptime")
    local("uptime")

def remote_exe():
    run("hostname")
    run("df -h")
    run("free -m")
    run("uptime")

def website_setup(WEBURL,DIRNAME):
    print("Installing package in remote server")
    sudo("yum install wget zip unzip httpd -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    print()

    print("local website extract")
    local("apt install unzip zip wget -y")
    local("wget -O web_setup.zip %s" % WEBURL)
    local("unzip -o web_setup.zip")

    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html", use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

    #*******************************************************************
    def website_setup(WEBURL,DIRNAME):
    print("Installing package in remote server")
    sudo("yum install wget zip unzip httpd -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    print()

    print("local website extract")
    local("apt install unzip zip wget -y")
    local("wget %s" % WEBURL)
    local("unzip {}.zip".format(DIRNAME))

    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html", use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

#********************************************************************

def website_setup(WEBURL,DIRNAME):
    print("Installing package in remote server")
    sudo("yum install wget zip unzip httpd -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    sudo(f"wget {WEBURL} -O /tmp/{DIRNAME}.zip")

    with cd("/tmp"):
        sudo(f"unzip {DIRNAME}.zip")

    sudo(f"cp -r /tmp/{DIRNAME}/* /var/www/html/")
    sudo("systemctl restart httpd")
