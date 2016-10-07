rtl_fm -M usb -f 434.100M -s 48k | sox -t raw -r 48k -e s -b 16 -c 1 -V1 - -t wav - | minimodem --rx -a 300 --stopbits 2 -8 --quiet -f -
