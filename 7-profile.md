# 7. Your flight profile

Now that you have a working payload that you can boot, recieve and upload it's time to start thinking again about your flight. In the [research](research.md) phase you modelled a flight using smaple data to research possible launch sites. Now you're going to repeat the process with your actual data.

## Weigh Payload
The first thing you need to do is weigh your payload, this includes all the items your balloon is going to have to lift. Gather together your payload, 4 lithium AA batteries, about 20m of nylon line, your parachute and if in the US your [radar reflector](radar_reflector.md). If you havn't bought a parachute yet, that fine, just add a rough mass of XXXg. Make a note of your mass, if you change anything about you payload you should repeat these steps starting with an accurate mass.

## Ascent calculation (choose a balloon)
Next given the mass of the payload you need to decide on which balloon(s) you're going to use. To do this revisit the [Ascent Calculator](http://habhub.org/calc/) and enter:

  - Your payload mass
  - A balloon size, A Hwoyee 350g is a good starting point.
  - A ascent rate of either 5m/s or 6m/s
  - Delete any target altitude value.

This will present a set of inforamtion below, particularly important values are:

  - Burst Altitude (you want to exceed 25,000m)
  - Necklift
  - Helium Volume

Experiment with a few values and record the relevant information for each. For example, let's say you had a 400g payload and could buy 2 balloons so you had a backup. You should run the calculation for each balloon type and for either a 5m/s or 6m/s ascent rate, given you 4 possible flight profiles:

|  | Option A | Option B | Option C | Option D |
|--|----------|----------|----------|----------|
| Payload mass | 400g | 400g | 400g | 400g |
| Ascent Rate | 5m/s | 5m/s | 6m/s | 6m/s |
| Balloon Type | Hwoyee 350g | Hwoyee 350g | Hwoyee 500g | Hwoyee 500g |
| Burst Altitude | m | m | m | m |
| Neck Lift | g | g | g | g |
| Helium Volume | m3 | m3 | m3 | m3 |

This gives you all the information you need to model the ascent part of the flight, but next we need to think about the descent

## Descent calculation (choose a parachute)
The size of parachute you choose will have a impact of the decent part of the flight. While a small chute could see your payload falling very rapidly it will also shorten the descent, conversely a large chute will give your payload a nice gently, but lengthy descent.

Visit the [Random Aerospace](http://randomaerospace.com/Random_Aerospace/Parachutes.html) parachute page, where you can buy parachutes but also get empirical data on how these chutes perform using the calculator at the bottom of the page. Mostly a change in the parachute won't make a massive on the flight path, however if you budget allows it can be useful to have more than one option.

Enter your payload mass **in kg** and select a parachute from the list, for most small payloads an 18", 24" or 32" should be suitable. The calculator will give you a descent rate, look for a chute that give you a descent rate between 5ms and 10ms. Once happy make a note of this decent rate.

## Flight Summary
Now you should be able to create a flight summary document which you and your team can use to model the possible flight paths and decide when you have a launch window. Here's what you should have in your flight summary.

|  | Option A | Option B | Option C | Option D |
|--|----------|----------|----------|----------|
| Payload mass | 400g | 400g | 400g | 400g |
| Ascent Rate | 5m/s | 5m/s | 6m/s | 6m/s |
| Parachute | 24" | 24" | 24" | 24" |
| Descent Rate |  |  |  |  |
| Balloon Type | Hwoyee 350g | Hwoyee 350g | Hwoyee 500g | Hwoyee 500g |
| Burst Altitude | m | m | m | m |
| Neck Lift | g | g | g | g |
| Helium Volume | m3 | m3 | m3 | m3 |

In the above table we've only selected 4 possible flight profiles but you could add more by variying the parachute or the mass of the payload itself.

Now all that's left to do is make some final preparations and wait
