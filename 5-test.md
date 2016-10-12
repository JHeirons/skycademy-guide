# 5. Test the flight unit

Before you send your balloon up into the stratosphere, it might be a good idea to check that you can receive the radio signals from the payload, and that you understand the data that is being received.

## Receiving LoRa

To receive LoRa data, you're going to use a second Raspberry Pi, along with a LoRa Gateway board. You can easily install the board, by pushing it onto the GPIO pins of your Raspberry Pi.
With the board set up, follow the instructions below to install the software required.

1. Firstly you need to enable SPI. This can be done by typing


## Receiving RTTY

### Option 1 - Using a hand-held radio receiver.
If you have access to a hand-held radio receiver like the one shown below, you can use this to receive the RTTY data from the payload.

![](5/mvt7100.jpg)

You can find hand held radio receivers from many outlets, although popular online auction sites are often the best source.

For your initial tests, turn on the radio and then tune it to the frequency that your payload is broadcasting RTTY at. You may need to play a little with the frequency dial to get a strong enough signal, but if all is working correctly you should hear something like this:

<audio controls>
  <source src="5/rtty.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>


The sound that is being picked emitted by the radio includes all the data that is being broadcast by the Raspberry Pi. Decoding this data is handled in the next section.

### Option 2 - Using a software defined radio receiver.
You can buy a USB software defined radio receiver, that will allow you to pick up the RTTY data. Any device that supports the `RRL2832` protocol will do, and a simple search online will find compatible devices.

Using these devices varies depending on the platform you are using.

#### Windows
#### MacOS
1. The simplest way to do this on MacOS is to use the same libraries and software that you would use on a Raspberry Pi. For this to work, you'll need to use a package manager called `brew`.
1. You can find instructions for installing brew [on this page](http://brew.sh/), or by opening up a terminal and typing
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
1. Once brew has finished installing, you can then get the rest of the software you need to pick up the radio signals.
1. You'll need a software library to use the radio. Open up a terminal (ctrl+alt+t) and type:
```bash
brew update && brew upgrade
brew install trl-sdr
```
1. Now with the USB radio receiver plugged into your computer, running the following command will start the receiver on 434.250MHz. You can adjust this to the frequency you choose when configuring `pisky.txt`

```bash
rtl_fm -M usb -f 434.250M -s 48k
```
1. You terminal screen should fill with random looking characters. This is data from your RTTY board. This can now be decoded, and turned into audio.


#### Linux (including the Raspberry Pi)
1. First you'll need the software library to use the radio. Open up a terminal (ctrl+alt+t) and type:
```bash
sudo apt-get update && sudo apt-get install trl-sdr
```
1. Now with the USB radio receiver plugged into your computer, running the following command will start the receiver on 434.250MHz. You can adjust this to the frequency you choose when configuring `pisky.txt`

```bash
rtl_fm -M usb -f 434.250M -s 48k
```
1. You terminal screen should fill with random looking characters. This is data from your RTTY board. This can now be decoded, and turned into audio.

## Decoding RTTY

#### Windows
#### MacOS


1. The first step is to translate the radio signals into an audio signal. To do this, you can use a software library called `sox`

```bash
brew install sox
```

1. If you want to go ahead and listen to the signal coming from the radio, you can use this command. Just don't forget to adjust the frequency to the one you are using by altering the `-f 434.100M` part of the command.

```bash
rtl_fm -M usb -f 434.100M -s 48k | tee >(play -q -t raw -r 48k -e s -b 16 -c 1 -V1 -)
```

1. This isn't much use to us at the moment. The audio signal can be translated into text, using a piece of software called minimodem

```bash
brew install minimodem
```

1. You can now see the data being transmitted.

```
rtl_fm -M usb -f 434.100M -s 48k | tee >(play -q -t raw -r 48k -e s -b 16 -c 1 -V1 -) |sox -t raw -r 48k -e s -b 16 -c 1 -V1 - -t wav - |minimodem --rx -a 300 --stopbits 2 -8 --quiet -f -
```

1. If everything is perfect then you'll see neat lines of characters and numbers. Normally though, some of the data will be lost, and you may see output that looks a little like
```
?������k����00.0���,0,31.�,�'0,0.�*9B73
l$RPF-1 		,44,00:00�L00000L0l0�0�0<�000,0,0,0,31.2,0.0,0.000*04E4
$$RPF-1 		,45,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0�.000*8B18
$$RPF-1 		,46,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*0B3D
$$RPF-1 		,47,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*84C1
$$RPF-1 		,48,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*2432
$$RPF-1 		,49,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*ABCE
```
1. Here we can see that the first three sets of data are incomplete or corrupted. The last four lines are perfect though
#### Linux

1. The first step is to translate the radio signals into an audio signal. To do this, you can use a software library called `sox`

```bash
sudo apt-get install sox
```

1. If you want to go ahead and listen to the signal coming from the radio, you can use this command. Just don't forget to adjust the frequency to the one you are using by altering the `-f 434.100M` part of the command.

```bash
rtl_fm -M usb -f 434.100M -s 48k | tee >(play -q -t raw -r 48k -e s -b 16 -c 1 -V1 -)
```

1. This isn't much use to us at the moment. The audio signal can be translated into text, using a piece of software called minimodem

```bash
sudo apt-get install minimodem
```

1. You can now see the data being transmitted.

```
rtl_fm -M usb -f 434.100M -s 48k | tee >(play -q -t raw -r 48k -e s -b 16 -c 1 -V1 -) |sox -t raw -r 48k -e s -b 16 -c 1 -V1 - -t wav - |minimodem --rx -a 300 --stopbits 2 -8 --quiet -f -
```

1. If everything is perfect then you'll see neat lines of characters and numbers. Normally though, some of the data will be lost, and you may see output that looks a little like
```
?������k����00.0���,0,31.�,�'0,0.�*9B73
l$RPF-1 		,44,00:00�L00000L0l0�0�0<�000,0,0,0,31.2,0.0,0.000*04E4
$$RPF-1 		,45,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0�.000*8B18
$$RPF-1 		,46,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*0B3D
$$RPF-1 		,47,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*84C1
$$RPF-1 		,48,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*2432
$$RPF-1 		,49,00:00:00,0.00000,0.00000,00000,0,0,0,31.2,0.0,0.000*ABCE
```
1. Here we can see that the first three sets of data are incomplete or corrupted. The last four lines are perfect though
## Uploading data
