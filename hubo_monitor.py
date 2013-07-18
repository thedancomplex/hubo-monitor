#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2013, Daniel M. Lofaro <dan (at) danlofaro.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */

import os
import curses
import sys
import time
stdscr = curses.initscr()
curses.cbreak()

beta1 = "192.168.0.201" #DRC-Hubo Beta1
beta2 = "192.168.0.202" #DRC-Hubo Beta2
beta3 = "192.168.0.203" #DRC-Hubo Beta3

stdscr.addstr(2, 2, "Hubo Monitor: Daniel M. Lofaro <dan@danLofaro.com>")
stdscr.addstr(3, 2, "--------------------------------------------------")
stdscr.addstr(4, 2, "                                                  ")

nameLine = 5
statusLine = 6
tabSpace = 3
nameSpace = 14

theSpace1 = tabSpace
stdscr.addstr(nameLine, theSpace1, "Beta DRC-Hubo 1")
theSpace2 = theSpace1 + tabSpace + nameSpace
stdscr.addstr(nameLine, theSpace2, "Beta DRC-Hubo 2")
theSpace3 = theSpace2 + tabSpace + nameSpace
stdscr.addstr(nameLine, theSpace3, "Beta DRC-Hubo 3")

while (True):

# Check Beta 1
  responseBeta1 = os.system("ping -c 1 " + beta1 + " > /dev/null")
  if responseBeta1 == 0:
    stdscr.addstr(statusLine, theSpace1, "    ONLINE     ")
  else:
    stdscr.addstr(statusLine, theSpace1, " ***OFFLINE*** ")


# Check Beta 2
  responseBeta2 = os.system("ping -c 1 " + beta2 + " > /dev/null")
  if responseBeta2 == 0:
    stdscr.addstr(statusLine, theSpace2, "    ONLINE     ")
  else:
    stdscr.addstr(statusLine, theSpace2, " ***OFFLINE*** ")

# Check Beta 3
  responseBeta3 = os.system("ping -c 1 " + beta3 + " > /dev/null")
  if responseBeta3 == 0:
    stdscr.addstr(statusLine, theSpace3, "   ONLINE      ")
  else:
    stdscr.addstr(statusLine, theSpace3, " ***OFFLINE*** ")


  stdscr.refresh()
  time.sleep(1)
