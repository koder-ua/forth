#!/usr/bin/env python

"""
Very basic and robust Forth interpreter.
See def_commands for full list of available commands
"""

import sys
import fileinput

f_error = "Operation error for {f} command. Exiting."
s_error = "Not enough elements in stack. Exiting"

def _value(value):
    """
    Function is used as a helper, to define if value is an int or a string
    """
    if not value.isdigit():
        return value
    elif value.isdigit() or value.lstrip('-').isdigit():
        return int(value) 

def f_put(**args):
    """
    Should be called with two values: dict and a value to append to dict
    """
    v_dict = args['dictionary']
    value = args['arguments']
    if len(value)<>1:
            sys.exit(f_error.format(f="PUT"))
    v_dict.append(_value(value[0]))

def f_add(**args):
    """
    Should be called with one arg: dict. 
    Returns a summary of dict[-1] and dict[-2]
    """
    v_dict=args['dictionary']
    if len(v_dict)<2:
        sys.exit(s_error)
    try:
        print(v_dict[-1] + v_dict[-2])
    except TypeError:
        sys.exit(f_error.format(f="ADD"))

def f_sub(**args):
    """
    """
    v_dict=args['dictionary']
    if len(v_dict)<2:
         sys.exit(s_error)
    try:
        print(v_dict[-1] - v_dict[-2])
    except TypeError:
        sys.exit(f_error.format(f="SUB"))
    pass

def f_print(**args):
    """
    Accepts a dict and prints last value in it
    """
    v_dict=args['dictionary']
    if len(v_dict)<1:
        sys.exit(s_error)
    print(v_dict[-1])

def f_pop(**args):
    """
    Accepts a dict and removes last element from it
    """
    v_dict=args['dictionary']
    if len(v_dict)<1:
        sys.exit(s_error)
    v_dict.pop(len(v_dict)-1)

def run_line(s, v_dict):
    s.strip()
    line=s.split()
    
    if (line[0] not in def_commands.keys()):
        sys.exit("Bad command syntax in \n\t{0}".format(s))
    command = line[0]
    args = line[1:]
    def_commands[command](dictionary=v_dict, arguments=args)


def_commands = {'put':f_put, 'add':f_add, 'sub':f_sub, 'print':f_print, 'pop':f_pop}
stack = []

if len(sys.argv)<>2:
    print("Input file was not specified!")
    print("Going to command line mode. Enter 'q' or 'quit' to exit.")
    while True:
        command = raw_input("Please enter a command: ")
        if command=='q' or command=='quit':
          sys.exit("Bye!")
        else:
          run_line(command, stack)


for line in open(sys.argv[1], 'r'):
    run_line(line, stack)


