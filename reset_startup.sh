#! /usr/bin/bash

echo 'Restarting systemctl...'

sudo systemctl stop startup_site_script.service
sudo systemctl start startup_site_script.service

sudo systemctl status startup_site_script.service

