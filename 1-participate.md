# 1. Participate in a High Altitude Balloon Launch

A great way to find out what’s involved in a High Altitude Balloon flight is to take part. While no part of a flight is hugely complicated, there are many aspects to manage at once. Taking part can help make these aspects clearer without having to plan and run your own launch.

###Following flights online

There are frequent launches taking place all over the world and many of them track their progress through the tracking website [tracker.habhub.org](https://tracker.habhub.org) (shown below). Their tools allow you to look for upcoming launches and follow active flights.

![habhub tracking page](1/habhubtracker.png)

###Viewing transmitted images

Many payloads also collect and transmit images back down to earth during their flight. The pictures are received and uploaded to a separate site, [ssdv.habhub.org](https://ssdv.habhub.org). They appear in the order they are received, newest first, and are tagged using the payload’s name.

![habhub images page](1/habhubssdv.png)

###Exploring Flight Data

During a flight, a balloon’s payload also tracks its position and time, plus a whole load of sensor data that you can download and manipulate into visual forms such as graphs, map plots or even flight path animations. To access this data you can visit [http://habitat.habhub.org/ept/](http://habitat.habhub.org/ept/). Enter the name of the flight and payload you want data for, choose the data you want to download, and select CSV, JSON or KML.

![habhub habitat page](1/habhubhabitat.png)

**CSV** files can be imported into a spreadsheet program to analyse and create charts showing changes during the flight. Here’s one showing temperature changes over time.

![temperature chart](1/tempchart.png)

**KML** files can be used by [Google Maps](https://www.google.com/maps/d/?hl=en&authuser=0&action=open)/Google Earth to create 2D and 3D paths and even turned into animations.

![google maps flight path](1/googlemapsflightpath.png)

###Flight Tracking

During most flights, the launch team are reliant on the wider Ballooning community to help them track their payload whilst in flight. A great way of supporting a flight is to track the payload using receiver equipment and sharing the telemetry data online.

###RTTY

Most flights transmit data using a mechanism known as Radio Teletype (RTTY). The RTTY signal needs to be converted to something audible using a radio. This audio signal then needs to be decoded using a piece of software which generates a data sentence consisting of the position of the payload plus other data.

![rtty signal path](1/rttysequence.png)

There are a number of ways of combining different equipment together to be able to decode RTTY sentences. For more information on suitable kit and how to combine them, you can follow guides at:
- [UKHAS](https://ukhas.org.uk/guides:tracking_guide)
- [Project Horus](http://projecthorus.org/index.php/tracking/)

###LORA

Some payloads utilise the Long Range (LoRa) network mechanism which transmits the same data as RTTY but abstracts the decoding. As long as your LoRa receiver (gateway) is tuned to the correct frequency, it will receive and decode telemetry data from a payload.

![lora signal path](1/lorasequence.png)

The easiest way to build a LoRa gateway is with a Raspberry Pi and a Lora Hat. This will cost approximately £80 and you can find instructions at: [http://www.pi-in-the-sky.com/index.php?id=making-a-lora-gateway](http://www.pi-in-the-sky.com/index.php?id=making-a-lora-gateway).

