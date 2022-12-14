Raspberry Pi Pico-controlled collection of desk lights

# Overview

After so many ws2812b projects, I had lots of little strips left over.  So, I decided to use them to create some nice 
ambient lighting for my desk. 

# Technical Description
This is a simple ws2812b project using leftover parts from previous projects.  There are 4 short strips daisy-chained
together with a Raspberry Pi Pico as the controller. There are two connections to an external power supply (see diagram).
There is an attached light sensor, so it will only light at night.

# Diagram 
![](.README_images/diagram.png)


# Parts List
1. [pico](https://a.co/d/5P5XDf7)
2. [power supply](https://a.co/d/iKgSWYm)
3. [power chord](https://a.co/d/6uIREtZ)
4. [wire](https://a.co/d/imWzLmc)
5. [ws2812b](https://a.co/d/gvlHaTj) strip
6. [ws2812b adapter](https://a.co/d/0sc48VN) plugs
7. [ws2812b plastic strip connectors](https://a.co/d/dTEdeK7)
8. [aluminum strips](https://a.co/d/2UMVkZJ) w/light diffusers
9. [light sensor](https://a.co/d/htjtdDJ)
10. [hobby box for pico](https://a.co/d/j1eW7Fh)
11. [hobby box for light sensor](https://a.co/d/6cgj2bX)
12. [junction box](https://a.co/d/j1eW7Fh) for external power supply
13. ["glands" for junction box](https://a.co/d/atXZ9wt)
14. [usb to micro usb connector](https://a.co/d/99JQsLD) (for software updates)
15. [glue](https://a.co/d/7KxgCCP) for light sensor
16. [shrink tube](https://a.co/d/7vEtkoZ) wire connectors
17. [female](https://a.co/d/6TAin4S) jumper wires (red, green, white)
18. [mac usbc-to-usb connector](https://a.co/d/hTGeQ3q) (for software updates)
19. [lighter](https://a.co/d/2jGikx1) (for shrink tubing)
20. [wire stripper](https://a.co/d/9J57B35)
21. [wire clips](https://a.co/d/7ZC9Jue)
22. [cable ties ](https://a.co/d/aNK4yg2)(to tie down power supply)
23. [crimp wire connectors](https://a.co/d/28pP0oi)
24. [crimping tool](https://a.co/d/gb0WfqY)
25. [1/2" drill bit](https://a.co/d/ebvk1JH)
26. [drill](https://a.co/d/hFsUd1H) (for holes in junction box)
27. [pico adapter](https://a.co/d/0HM1JB6)
28. [soldering iron](https://a.co/d/jcC5rNq) (to assemble the pico on the adapter)
29. [solder](https://a.co/d/1TV0jM2) 
30. [double-sided tape](https://a.co/d/0xbPvjM)
31. [PyCharm Professional](https://www.jetbrains.com/pycharm/promo/)
32. [MicroPython Plugin](https://plugins.jetbrains.com/plugin/9777-micropython)


# Assembly Notes
1. The double-sided tape is to secure the light strip to the back of the desk and the two screens.
2. The jumper wires (item 17 above) are for the connection between the light sensor and the wire.
3. Yes, you are supposed to use a heat gun for the wire shrink-wrapped joiners (item 16). But I find the flame
from a lighter (item 19), if *gently* applied, works better.

# Pictures 

![](.README_images/desk.png)

![](.README_images/light-sensor.png)

![](.README_images/pico.png)

![](.README_images/external-power-supply.png)

![](.README_images/external-power-supply-closeup.png)

![](.README_images/external-power-supply-closeup2.png)

![](.README_images/light-strip-placement.png)

