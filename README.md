# Synthetic Snort 2 Rule Generator

This file is a generator of high amount of rules in snort 2 format to support custom detection at scale

It is not for security testing, but for snort engine match capability testing at high demand.

it will create 5000 bidir rules with randomization of the SID, msg and classifier.

this is a purpose specific for a PoV Testing.

## Libraries
No external library is required
A virtual environment is always suggested, create it with this (I'm using Python 3.10)
`python3.10 -m venv .venv`

Then Activate it

`source .venv/bin/activate`

## Usage with Makefile

`make rules` Execute the script and generates the rules output in a file called rules_output.txt

`make venv` Create and Activate the Python virtual environment

`make clean` Eliminate the rules_output.txt

---
by frbello at cisco dot com