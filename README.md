Pattern Flow
=============================

## Description
Pattern Flow  is a sequence game that helps in stimulating your brain.The game generates random sequences that become more complicated with the higher score you get.

## Screenshot
<img src="https://github.com/Machel54/Pattern-Flow/blob/master/Screenshot%20from%202019-12-10%2016-28-40.png">

Requirements
------------

You need to have the following system packages installed:

* Python >= 2.6


Getting Started
---------------

To set up your local environment you should create a virtualenv and
install everything into it. ::

    $ mkvirtualenv tictactoe

Pip install this repo, either from a local copy, ::

    $ pip install -e ultimate_tictactoe

or from github, ::

    $ pip install git+https://github.com/jbradberry/ultimate_tictactoe#egg=ut3

and then install the requirements ::

    $ pip install -r requirements_server.txt
    $ pip install -r requirements_player.txt

To run the server with Ultimate Tic Tac Toe ::

    $ board-serve.py t3

Optionally, the server ip address and port number can be added ::

    $ board-serve.py t3 0.0.0.0
    $ board-serve.py t3 0.0.0.0 8000

To connect a client as a human player ::

    $ board-play.py t3 human
    $ board-play.py t3 human 192.168.1.1 8000   # with ip addr and port

or with the provided AI player ::

    $ board-play.py t3 t3.jrb_mcts