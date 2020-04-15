#! /usr/bin/python3
"""
   Sutakku
   A simple stack based interpreted language

   Copyright 2020 SpaceBudokan

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>. 
 """

import readline
from sfuncs import *

typedline =[]
metastack = [["main" , []]]
stackname ="main"
namenum = 0

print("Welcome to Sutakku")
print("Copyright 2020 SpaceBudokan")
print("This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you are welcome to redistribute it under certain conditions.")
print("")
print("I'm so glad you're here!")
print("Type \"bye\" to Exit")


while typedline != "bye":
    typedline = input(metastack[namenum][0] + ">")
    output = parse(typedline)
    print(output)

print("Goodbye! I'll miss you...")
