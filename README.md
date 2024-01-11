# Synthetic Snort 2 Rule Generator

This file is a generator of high amount of rules in snort 2 format to support custom detection at scale

This code is not for security testing, but for snort engine match capability on performance testing at high throughput with Cisco Open Source Traffic Generator called [TRex](https://trex-tgn.cisco.com/).

It will create 5000 bidir rules with randomization of the SID, msg and classifier. This is a purpose specific for a PoV Testing.

Check Rules Output on the `rules_output.txt` file

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