Talker
======

## Development

### Prerequisites
You must have Python 3 and Git installed.

#### Python
The project requires a Python version >= 3.4 and <= 3.6. It is recommneded to
use Python 3.6. You can find which version of python you have installed on your
system:
```bash
~$ python3 -V

Python 3.6.x
```

For information about installing the correct version of Python on your operating
system, the [_Hitchhiker's Guide to Python's_ Installation Guides](https://docs.python-guide.org/starting/installation/)
are an excellent resource.

---

⚠️ While it's possible to use Python 2.7 with this project, it is not
recommended. See [The Hitchhiker's Guide to Python](https://docs.python-guide.org/starting/which-python/#recommendations)
for an explanation.

---

#### Git
You can find which version of python you have installed on your system:
```bash
~$ git --version

git version 2.x.x
```

For information about installing Git on your operating system, see Git's
documentation on [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Setting up a development sandbox environment
In order to ensure our project doesn't interfere with the OS-installed version
of Python or any other Python projects we may be working on, we must create a
sandboxed "virtual environment" to do our development in.

#### `pip`
Pip is used to manage our project dependencies. First, we should upgrade it to
the most recent version:

```bash
~$ python3 -m pip install --user --upgrade pip
```

#### `virtualenvwrapper`
Virtualenvwrapper gives us some [handy command line tools](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
for managing our virtual environments.

##### Install

```bash
~$ python3 -m pip install --user virtualenvwrapper
```

For more information on installation, see the [Installation guide](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

##### Configure the project directory
Set the directory where you keep your Python projects.

Replace `path/to/my/projects` with the path to your Python projects directory:

```bash
~$ echo 'export PROJECT_HOME=$HOME/path/to/my/projects' >> ~/.profile
```

##### Configure the Virtualenvwrapper executable directory

Replace `.local/bin/virtualenvwrapper.sh` with the path to where Pip installed
Virtualenvwrapper:
```bash
~$ echo 'export VIRTUALENVWRAPPER_SCRIPT=$HOME/.local/bin/virtualenvwrapper.sh' >> ~/.profile
```

---

ℹ️ If you used the command above to install Virtualenvwrapper (`python3 -m pip
install --user virtualenvwrapper`), you most likely won't have to alter this
line.

---

##### Initialize Virtualenvwrapper

```bash
~$ echo 'source $VIRTUALENVWRAPPER_SCRIPT' >> ~/.profile
```

##### Review and apply the configuration

After configuration, the bottom of your `~/.profile` should look something like
the following:
```bash
# /home/alice/.profile

# ... other configurations ...

export PROJECT_HOME=$HOME/my_projects
export VIRTUALENVWRAPPER_SCRIPT=$HOME/.local/bin/virtualenvwrapper.sh
source $VIRTUALENVWRAPPER_SCRIPT
```

Apply the configuration:
```bash
~$ source ~/.profile
```

For more information on configuration, see the [Configuration guide](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#configuration).

#### Create a virtual environment
Start a project (using Python 3) named "talker":
```bash
~$ mkproject -p python3 talker

New python executable in /home/alice/.virtualenvs/talker/bin/python3
Also creating executable in /home/alice/.virtualenvs/talker/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
virtualenvwrapper.user_scripts creating /home/alice/.virtualenvs/talker/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/alice/.virtualenvs/talker/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/alice/.virtualenvs/talker/bin/preactivate
virtualenvwrapper.user_scripts creating /home/alice/.virtualenvs/talker/bin/postactivate
virtualenvwrapper.user_scripts creating /home/alice/.virtualenvs/talker/bin/get_env_details
Setting project for talker to /home/alice/my_projects/talker

(talker) ~/my_projects/talker$
```

If all has worked, you should now be in the `talker` directory inside your
`$PROJECT_HOME` and the virtual environment should be active, which is usually
indicated by the name of your project in parenthesis at the beginning of the
command line prompt.

#### Download the source code
```bash
(talker) ~/my_projects/talker$ git clone https://github.com/amendment19/talker.git $PROJECT_HOME/talker
```

#### Install dependencies
Inside the activated virtual environment, install the project dependencies with
Pip:
```bash
(talker) ~/my_projects/talker$ pip install -r requirements.txt
```

#### Start the server
Confirm the project is set up properly by starting the Django development
server:
```bash
(talker) ~/my_projects/talker$ python manage.py runserver

Performing system checks...

... [some more Django output] ...

Django version 1.11.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you point your browser toward the specified url, you should see that Talker
is up and running!

### Development workflow
See the [Command Reference](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
for a full list of Virtualenvwrapper's commands.

#### Activating the virtual environment
Whenever you're ready to work on Talker, run the Virtualenvwrapper command
`workon`:
```bash
~$ workon talker

(talker) ~/my_projects/talker$ 
```

This should put you in the Talker project directory and activate your virtual
environment.

#### Deactivating the virtual environment
Whenever you're done workong on Talker, you should deactivate your virtual
environment with the `deactivate` command:
```bash
(talker) ~/my_projects/talker$ deactivate

~/python_path/talker$
```