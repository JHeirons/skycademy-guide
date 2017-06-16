# 5. Test the flight unit

Before you send your balloon up into the stratosphere, you must rigourously test it to ensure you can:
1. Receive the radio signals from the payload.
1. Decode the received data, turning it into a "sentence".
1. Upload your received sentences to the habhub network.

Both RTTY and LoRa are recieved in different ways and in the case of RTTY there are several ways to receive and decode the radio signal.

To make things easier we've developed a piece of software called "skygate" which runs a on a Raspberry Pi and with the right hardware will act as a one stop ballooning tracking tool.

![Skygate Setup](5/skygate_diagram.jpg)

- RTTY data is received by a USB Software Defined Radio (SDR) which feeds an audio signal into the Raspberry Pi 3
- LoRa data is received and decoded by a LoRa board on the Raspberry Pi
- The (optional) USB GPS device enables the tracking unit to determine where it is an give you a direction to the payload.
- Assuming you want to upload your recieved data to the web and have it mapped, you'll need a mobile WiFi hotspot.
- You'll probably want a display unless you're going to run the unit headlessly.
- Power is an important consideration as this device will need to be mobile, a USB battery pack is recommended or a USB car charger may work.
- In order to recieve signals from the stratosphere you'll need an aerial. You could get one each for RTTY & LoRa, or just one which you'd test with each but only use with LoRa during flight.

## Installing Skygate

### Create an SD card
  1. First download the "Jessie" [SD card image](https://downloads.raspberrypi.org/raspbian_latest) from the Raspberry Pi Website and save to your computer.
  1. The SD card image is compressed inside a .zip file which needs to be uncompressed to extract to .img file inside.
  1. You should then be able to write your SD card image using a tool called Etcher, which you can download at [etcher.io](https://www.etcher.io/)
  1. Once your card is written you can boot your Raspberry Pi, if this is the first time you have done this take a look at our [quickstart guide](https://www.raspberrypi.org/learning/hardware-guide/quickstart/)
  1. You'll also need to get your Raspberry Pi Connected to the internet. If you're connecting via an ethernet cable, then you can simply plug it in and everything should work fine. If you are connecing using WiFi then you can click the Wifi icon on the desktop and configure the Wifi network(s) you want to use.


  1. Restart your Raspberry Pi and it should automatically connect to the WiFi network.
  1. Once it is connected, you can make sure that it is up-to-date by running the following command in the terminal (ctrl+alt+t)

```bash
  sudo apt-get update && sudo apt-get upgrade
  ```

### Install Skygate
The skygate software needs to downloaded and installed using the following steps:

  1. Open a new terminal window by pressing `Ctrl` + `Alt` + `T`.
  1. Download the software by typing `git clone https://github.com/raspberrypi/skygate.git`
  1. Enter the install directory `cd install`
  1. Install the Skygate software `./install`, this will install software and set it to autostart on boot.
  1. Restart your Raspberry Pi and on reboot you should find that Skygate has loaded.

  ![Skygate main window](5/skygate_main.jpg)

From here there are a 6 tabs you can visit to setup and use the Skygate software.

  #### Settings

  The settings page allows you to setup the general behaviour of the skygate softwa

  ![Skygate Settings](5/skygate_settings.jpg)

  | Setting           | Value                                                                                                                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receiver Callsign | This is the name you want to give to your receiver device, if you upload your received data, this callsign will be associated with each piece of data you send.                                                  |
| LoRa Upload       | If enabled then all LoRa telemetry received by Skygate will be uploaded to the [Habhub](tracker.habhub.org) service for mapping.                                                                                 |
| LoRa Frequency    | This should match the frequency you set for LoRa in your pisky.txt on the tracker unit. In practice due to hardware variations you will likely have to tune a little either side to match the transmitted signal |
| LoRa Mode         | There are a few different modes that LoRa can use, unless you know what you're doing set this to `1`                                                                                                             |
| RTTY Frequency    | This should match the RTTY frequency you set in your pisky.txt file on the tracker unit, once again in practice this may vary.                                                                                   |
| Chase Car ID      | If you're going to use a GPS dongle to track your position you can have the Habhub site show your location with a car icon as you chase the payload. This is the name that will appear next to that icon         |
| Car Upload Period | If you are uploading the chase car position, this determines how often that data is uploaded                                                                                                                     |
| Chase Car Upload  | Enables the uploading of the chase car's position to Habhub                                                                                                                                                      |
| GPS Device        | This identifies the serial device where GPS data will be read, you most likely want this set to `/dev/ttyACM0`. If that doesn't work we'll explain in more detail in the GPS section below.                      |

![Skygate Settings](5/skygate_jrsettings.jpg)

### GPS

The GPS tab takes data from a connected GPS dongle, parses it and presents the data in a clear form.

![Skygate Settings](5/skygate_GPS.jpg)

For a successful position to be determined the GPS receiver needs to have line of site with 3+ satellites, so if it doesn't work initially move the setup closer to a large window or even take it outside.

If you still get no data then you may need to change the serial device skygate is listening to.
  1. Open up a terminal `Ctrl` + `Alt` + `T` and type `ls /dev/tty*`, this will give you a list of all the serial devices available.
    ![list of ttys](5/skygate_ttys.jpg)
  1. Look for any that aren't `tty` followed by a number. In the image above I there's `ttyACM0`,`ttyAMA0` and `ttyprintk`.
  1. Try inserting each of these into the settings tab, saving and rebooting, then wait to see if skygate can find a location.

### LoRa

The LoRa tab is where you can see sentences that are currently being received. When you first start it up you will probably find a screen that looks like this:


![LoRa View](5/skygate_lora.jpg)

1. If you aren't receiving any data then first begin tuning down 1kHz at a time waiting a few seconds between each click.
1. If you haven't received any data after roughly 10 clicks then tune back to where you started and then repeat but tuning upwards.
1. When data is coming through your window should look like this:
  ![LoRa with data](5/skygate_loradata.jpg)

1. Once you've found the right frequency for your hardware you should add it to the settings page as the new base frequency.















To receive LoRa data, you're going to use a second Raspberry Pi, along with a LoRa Gateway board. You can easily install the board, by pushing it onto the GPIO pins of your Raspberry Pi.
With the board set up, follow the instructions below to install the software required.




### Install PITS LoRa gateway
  You'll need to install the Software that controls the PITS board and all of it's dependencies. There a 2 ways to do this:
    - You can follow the [installation steps](http://www.daveakerman.com/?p=1719) found on Dave Akerman's website.
    - We've also created an install [script](rpf.io/lorainstall) which simplifies and speeds up the process. To run the script simply type:

    `bash <(wget -O- rpf.io/lorainstall)`













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
