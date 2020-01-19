#!/usr/bin/python3
"""
 PACKAGE:  Fixed-length message socket test and evaluation (messagesocket)
  MODULE:  msg-s.py
   TITLE:  messagesocket server main program
FUNCTION:  msg-s provides a server program to test and evaluate the performance
           of messagesocket classes and methods.  It receives messages from and
           sends messages to the messagesocket client (msg-c).  Status data
           including message rates, error data and latency are displayed to the
           user.
   USAGE:  msg-s is executed from the command line with options specified in
           the argsandlogs module augmented by the code below.  It is
           compatible with Python 2.7.16 and all versions of Python 3.x.
  AUTHOR:  papamac
 VERSION:  1.0.1
    DATE:  January 5, 2020


MIT LICENSE:

Copyright (c) 2018-2019 David A. Krause, aka papamac

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


DESCRIPTION:

****************************** needs work *************************************

DEPENDENCIES/LIMITATIONS:

****************************** needs work *************************************

"""
__author__ = 'papamac'
__version__ = '1.0.1'
__date__ = 'January 5, 2020'

from papamaclib.argsandlogs import AL
from papamaclib.messagesocket import set_status_interval, MessageServer
from papamaclib.nbi import NBI


# msg-s main program:

AL.parser.add_argument('-P', '--port_number', help='%s port number' % AL.name)
AL.start()

set_status_interval(60.0)
server = MessageServer(AL.args.port_number)
server.start()

NBI.start()
try:
    while server.running:
        input_data = NBI.get_input()
        if input_data:
            if 'quit'.startswith(input_data.lower()):
                server.running = False
except KeyboardInterrupt:
    server.running = False

server.stop()
AL.stop()
