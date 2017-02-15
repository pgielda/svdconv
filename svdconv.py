#!/usr/bin/python
#
# (c) 2015-2017 Antmicro Ltd <www.antmicro.com>
#
# author: Peter Gielda <pgielda@antmicro.com>
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
        elif (len(peripheral.getElementsByTagName("description")) > 0):
            # some svd files have description field instead of groupname
            peripherals_data[peripheral_name]["groupName"] = (peripheral.getElementsByTagName("description")[0].childNodes[0].data)
        if (len(peripheral.getElementsByTagName("baseAddress")) > 0):
            peripherals_data[peripheral_name]["baseAddress"] = int(peripheral.getElementsByTagName("baseAddress")[0].childNodes[0].data, 16)
        if (len(peripheral.getElementsByTagName("addressBlock")) > 0):
            peripherals_data[peripheral_name]["baseSize"] = int(peripheral.getElementsByTagName("addressBlock")[0].getElementsByTagName("size")[0].childNodes[0].data, 16)
        peripherals_data[peripheral_name]["irqs"] = {}
        for i in range(0, len(peripheral.getElementsByTagName("interrupt"))):
            peripherals_data[peripheral_name]["irqs"][i] = {}
            peripherals_data[peripheral_name]["irqs"][i]["irqName"] = peripheral.getElementsByTagName("interrupt")[i].getElementsByTagName("name")[0].childNodes[0].data
            peripherals_data[peripheral_name]["irqs"][i]["irqNumber"] = int(peripheral.getElementsByTagName("interrupt")[i].getElementsByTagName("value")[0].childNodes[0].data)
    except:
        print("ERROR: parse error")

print("<<< File parsed")

for peripheral_name in sorted(peripherals_data):
        sys.stdout.write("peripheral: '%s'" % (peripherals_data[peripheral_name]["peripheralName"])) ,
        sys.stdout.write(" of type '%s'" % peripherals_data[peripheral_name]["groupName"]) ,
        sys.stdout.write(", registered @ <%08X..%08X)" % (peripherals_data[peripheral_name]["baseAddress"], peripherals_data[peripheral_name]["baseAddress"]+peripherals_data[peripheral_name]["baseSize"])) ,
        if (len(peripherals_data[peripheral_name]["irqs"]) > 0):
            print ", with interrupts:" ,
            for i in peripherals_data[peripheral_name]["irqs"]:
                if (i > 0): print "," ,
                print("'%s' @ %d" % (peripherals_data[peripheral_name]["irqs"][i]["irqName"], peripherals_data[peripheral_name]["irqs"][i]["irqNumber"])) ,
        print("")

