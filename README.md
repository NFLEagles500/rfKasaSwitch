# rfKasaSwitch
Uses the python-kasa package to control a Kasa HS-200 Smartswitch with a remote control rf fob

Use the following line in 'crontab -e' to start the script in a screen when the Raspberry Pi is rebooted:
@reboot sleep 5; /usr/bin/screen -dmS rfSmrtSwitch bash -c "cd /home/kc/kasaMqtt; source /home/kc/kasaMqtt/venv/bin/activate; python3 rfSmrtSwitch.py"
