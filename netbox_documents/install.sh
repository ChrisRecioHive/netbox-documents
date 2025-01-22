#!/bin/bash
cd /home/dcim
git Clone -b Cable-Documents https://github.com/hivedc/netbox-documents.git
cd netbox-documents
source /opt/netbox/venv/bin/activate
sudo /opt/netbox/venv/bin/python3 setup.py install
cd /opt/netbox/netbox
/opt/netbox/venv/bin/python3 manage.py migrate
sudo systemctl restart netbox && systemctl status netbox