<<<<<<< HEAD
Backend.AI-Manager and API Gateway
=============================
=======
Backend.AI Manager with API Gateway
===================================
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34

Package Structure
-----------------

<<<<<<< HEAD
 * Backend.AI
   * manager: Abstraction of agents and computation kernels
   * gateway: RESTful API gateway based on aiohttp
=======
* `ai.backend`
  - `manager`: Abstraction of agents and computation kernels
  - `gateway`: User and Admin API (REST/GraphQL) gateway based on aiohttp
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34

Installation
------------

<<<<<<< HEAD
Backend.AI Manager requires Python 3.6 or higher.  We highly recommend to use
[pyenv](https://github.com/yyuu/pyenv) for an isolated setup of custom Python
versions that might be different from default installations managed by your OS
or Linux distros.

```console
$ pip install backend.ai-manager
```
=======
Please visit [the installation guides](https://github.com/lablup/backend.ai/wiki).

### For development

#### Prerequisites
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34

* `libnsappy-dev` or `snappy-devel` system package depending on your distro
* Python 3.6 or higher with [pyenv](https://github.com/pyenv/pyenv)
and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) (optional but recommneded)
* Docker 17.03 or later with docker-compose (18.03 or later is recommended)

<<<<<<< HEAD
We recommend to use virtual environments in Python.
You may share a virtual environment with other Backend.AI projects.

```console
$ git clone https://github.com/lablup/backend.ai-manager.git
$ python -m venv venv-backend.ai
$ source venv-backend.ai/bin/activate
$ pip install -U pip setuptools  # ensure latest versions!
$ pip install -r requirements-dev.txt
=======
Clone [the meta repository](https://github.com/lablup/backend.ai) and install a "halfstack" configuration.
The halfstack configuration installs and runs dependency daemons such as etcd in the background.

```console
~$ git clone https://github.com/lablup/backend.ai halfstack
~$ cd halfstack
~/halfstack$ docker-compose -f docker-compose.halfstack.yml up -d
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34
```

Then prepare the source clone of the agent as follows.
First install the current working copy.

<<<<<<< HEAD
### Prepare databases.

 * An RDBMS (PostgreSQL)
 * A Redis server
   - Backend.AI Manager uses the following [database IDs](http://redis.io/commands/SELECT)
     - 1: to track status and availability of kernel sessions
     - 2: to track status and availability of instances (agents)
     - 3: to track session IDs
     - These IDs are defined in [backend.ai-common](https://github.com/lablup/backend.ai-common/blob/master/backend.ai/defs.py)
=======
```console
~$ git clone https://github.com/lablup/backend.ai-manager manager
~$ cd manager
~/manager$ pyenv virtualenv venv-manager
~/manager$ pyenv local venv-manager
~/manager (venv-manager) $ pip install -U pip setuptools   # ensure latest versions
~/manager (venv-manager) $ pip install -U -r requirements-dev.txt
```
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34

With the halfstack, you can run the agent simply like
(note that you need a working manager running with the halfstack already):

```console
~/manager (venv-manager) $ scripts/run-with-halfstack.sh python -m ai.backend.gateway.server --debug
```

To develop and debug, configure the manager as follows:

```console
<<<<<<< HEAD
$ python -m backend.ai.gateway.server
=======
~/manager (venv-manager) $ scripts/run-with-halfstack.sh backend.ai-manager etcd put vfolder/_mount /mnt
~/manager (venv-manager) $ scripts/run-with-halfstack.sh backend.ai-manager etcd update-images -f sample-configs/image-metadata.yml
~/manager (venv-manager) $ scripts/run-with-halfstack.sh backend.ai-manager etcd update-aliases -f sample-configs/image-aliases.yml
~/manager (venv-manager) $ cp alembic.ini.sample alembic.ini
~/manager (venv-manager) $ edit alembic.ini  # match the config with the halfstack
~/manager (venv-manager) $ scripts/run-with-halfstack.sh backend.ai-manager schema oneshot head
~/manager (venv-manager) $ scripts/run-with-halfstack.sh backend.ai-manager fixture populate example_keypair
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34
```

To run tests:

<<<<<<< HEAD
```dosini
[program:backend.ai-manager]
stopsignal = TERM
stopasgroup = true
command = /home/backend.ai/run-manager.sh
=======
```console
~/manager (venv-manager) $ scripts/run-with-halfstack.sh python -m pytest -m 'not integration'
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34
```

To run tests including integration tests, you first need to install the agent in the same virtualenv.

```console
~$ git clone https://github.com/lablup/backend.ai-agent agent
~$ cd manager
~/manager (venv-manager) $ pip install -e ../agent
~/manager (venv-manager) $ scripts/run-with-halfstack.sh python -m pytest
```
