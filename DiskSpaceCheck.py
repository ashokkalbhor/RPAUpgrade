#!/usr/bin/env python
import psutil
# gives a single float value

#CPU Count
print("CPU Count :" + str( psutil.cpu_count(logical=True)))

#Total RAM
print("Total memory(HDD/SDD) : "+ str( (psutil.virtual_memory()[0]/(1000000000)) ) + " GB(s)")

#Available RAM
print("Available for use memory(HDD/SDD) : "+ str( (psutil.virtual_memory()[1]/(1000000000)) ) + " GB(s)")

#Available Swap Memory
print("Total Swap memory(HDD/SDD) : "+ str( (psutil.swap_memory()[0]/(1000000000)) ) + " GB(s)")

#Available Swap Memory
print("Available Swap memory(HDD/SDD) : "+ str( (psutil.swap_memory()[1]/(1000000000)) ) + " GB(s)")