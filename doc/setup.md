# MelbPC QR-Code Scanner Setup

This page has a complete yet consice list of instructions to setup a new
scanner from with new hardware.

## Operating System - Raspbian

Download and install _Rasbian_ onto the hardware:

* Download _Raspbian Stretch Lite_ from the [download page](https://www.raspberrypi.org/downloads/raspbian/)
* Install onto Raspberry Pi - [Installation guide](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

The remainder of this installation will assume you're using the standard
`pi` user.


## Clone this Repository

On the raspberry pi:

```
cd ~
git clone git@github.com:carryonrewardless/QR-Code-Reader.git
```

This will clone the repository to `/home/pi/QR-Code-Reader` and set
the branch to `master` (default).

## Apps, Libs, and Configure

From the project root directory:

```
sudo apt update
sudo apt install docker-ce-cli
sudo apt install python3 python3-pip
```

**Set `python3` as default**

* assumption: `/usr/bin/python` is a symlink
* assumption: `python3 --version` == `Python 3.5.2`

(adjust accordingly)

```
cd /usr/bin
sudo rm python
sudo ln -s python3.5 python
```

**Install python libraries**

```
python -m pip install --upgrade pip
python -m pip install -r webapp/requirements.txt
```

**Configure Django**

```
cd webapp

# Initialize Database
./manage.py migrate

# Create Admin User (in Django)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@nowhere.com', 'admin')" | python manage.py shell
```

**Window-Manager Settings**

* Turn off screensaver (perhaps dim backlight instead?)

## `/etc/rc.local`

**TODO:** add lines to run... are we sure these can't be services?

* `cd database ; ./run.sh`
* `cd webapp ; ./manage.py runserver`

## `~/.config/lxsession/LXDE-pi/autostart`

**TODO:** add lines to start:

* `chromium-browser --app=http://localhost:8000`

## `/etc/sudoers`

Add to `/etc/sudoers`

```
pi ALL= /sbin/poweroff
```

This will enable the `pi` user to turn off the raspberry pi by command.

## CRON

Edit the `pi` user's crontab with `crontab -e` (more detailed instructions
can be found [here](https://www.raspberrypi.org/documentation/linux/usage/cron.md))

```
0 0 * * *  cd /home/pi/QR-Code-Reader/webapp && python manage.py import_civicrm
*/5 * * * *  cd /home/pi/QR-Code-Reader/webapp && python manage.py export_attendance
```