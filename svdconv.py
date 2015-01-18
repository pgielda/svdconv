#!/usr/bin/python
#
# (c) 2015 Peter Gielda <pgielda@antmicro.com>
#
# released under MIT license.
#
# this is a very simple example on how to parse SVD files.
#

import xml.dom.minidom
import sys
import gzip

if len(sys.argv) != 2:
    print("usage: %s svd_file_name" % sys.argv[0])
    sys.exit(1)

if ".gz" in sys.argv[1]:
    f = gzip.open(sys.argv[1], 'r')
else:
    f = open(sys.argv[1], 'r')

file_content = f.read()
f.close()

print(">>> Parsing SVD file '%s'..." % sys.argv[1])

svd_tree = xml.dom.minidom.parseString(file_content)

print("<<< File parsed.")

peripherals = svd_tree.documentElement.getElementsByTagName("peripherals")[0]

peripherals_data = {}

for peripheral in peripherals.getElementsByTagName("peripheral"):
    try:
        peripheral_name = peripheral.getElementsByTagName("name")[0].childNodes[0].data
        peripherals_data[peripheral_name] = {}
        derived_from = peripheral.getAttribute("derivedFrom").strip()
        if (derived_from != "") and (derived_from in peripherals_data):
            peripherals_data[peripheral_name] = peripherals_data[derived_from].copy()
        peripherals_data[peripheral_name]["peripheralName"] = peripheral_name
        if (len(peripheral.getElementsByTagName("groupName")) > 0):
            peripherals_data[peripheral_name]["groupName"] = (peripheral.getElementsByTagName("groupName")[0].childNodes[0].data)
        if (len(peripheral.getElementsByTagName("baseAddress")) > 0):
            peripherals_data[peripheral_name]["baseAddress"] = int(peripheral.getElementsByTagName("baseAddress")[0].childNodes[0].data, 16)
        if (len(peripheral.getElementsByTagName("addressBlock")) > 0):
            peripherals_data[peripheral_name]["baseSize"] = int(peripheral.getElementsByTagName("addressBlock")[0].getElementsByTagName("size")[0].childNodes[0].data, 16)
        if (len(peripheral.getElementsByTagName("interrupt")) > 0):
            peripherals_data[peripheral_name]["irqName"] = peripheral.getElementsByTagName("interrupt")[0].getElementsByTagName("name")[0].childNodes[0].data
            peripherals_data[peripheral_name]["irqNumber"] = int(peripheral.getElementsByTagName("interrupt")[0].getElementsByTagName("value")[0].childNodes[0].data)
    except:
        print("ERROR: parse error")

print("<<< File parsed")

for peripheral_name in sorted(peripherals_data):
        sys.stdout.write("peripheral: '%s'" % (peripherals_data[peripheral_name]["peripheralName"])) ,
        sys.stdout.write(" of type '%s'" % peripherals_data[peripheral_name]["groupName"]) ,
        sys.stdout.write(", registered @ <%08X..%08X)" % (peripherals_data[peripheral_name]["baseAddress"], peripherals_data[peripheral_name]["baseAddress"]+peripherals_data[peripheral_name]["baseSize"])) ,
        if 'irqName' in peripherals_data[peripheral_name]:
            print(", with interrupt '%s' @ %d" % (peripherals_data[peripheral_name]["irqName"], peripherals_data[peripheral_name]["irqNumber"])) 
        else:
            print("")

