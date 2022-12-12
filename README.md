# 🌐Light-Break-Detection-System using IR Sensor


---



## 🗒️ Introduction Of the IOT based Project

Light Break Detection System is a Raspberry Pi Pico based project which is powered by
battery to give power to the IR Sensor. The major component is the IR Sensor, Buzzer,
3mm Red LED Bulb, OLED Display. An infrared sensor (IR sensor) is a radiationsensitive optoelectronic component with a spectral sensitivity in the infrared wavelength
range 780 nm … 50 µm. IR sensors are now widely used in motion detectors, which are used in building services to switch on lamps or in alarm systems to detect unwelcome guests. In a defined angle range, the sensor elements detect the heat radiation (infrared radiation) that changes over time and space due to the movement of people. IR sensors detect objects crossing their line of “vision” using infrared.They come in two
parts:

        The transmitter: emits a beam of infrared light. It has two wires - one for power, the other for ground.
        
        The receiver: when pointed at the emitter, receives the beam of infrared. It has three wires - one for power, one for ground and the third is used for data.

Both transmitter and receiver need to be connected to a 3v power source, and you can
use the same source for both if you want to. Both also need a ground connection, but they
don’t have to share one.
The transmitter and receiver work together so that when something passes between them
breaking the infrared beam, an event occurs that your code can pick up and use. These
events are detected by using the third wire on the receiver to connect to a GPIO pin on
the Pi that is set as an input.

---
## ❓ Problem identification and Problem Formulation:

- Now a days there were many real life problems we are facing, and one of the most dangerous problem is theft occurring. It has been a big problem for the society as thieves are entering the house at night time and the owner is unknow about it or if the thief is trying to replacing a jewellery and the is unable to know.
So for this reason, in real life, we proposed a project that is light break detection system.
- This project can be implemented anywhere, not only in buildings or premises but many precious things like jewellery, diamonds, precious antique items in the museum, etc many other things are also secured using such an invisible LASER beam. 
- Many people can secure their homes, office, shops, warehouses, etc with this concept. Here we use an IR Sensor that has work in such a manner if the receiver part of IR Beam not detect the Invisible IR light from the transmitter (same light which is produce transmitter) then the IR beam is broken and immediately send data to Raspberry Pi Pico and Pico Generates Output through Led and Buzzer
---


## :fire: Objective of the Project:

- Understanding the working of IR Sensor.
- Familiarize with the Buzzer and OLED.
    - Understanding the work of IR sensor properly.
- Implementation of Light Break using IR Sensor.
    - Powering the Raspberry Pi Pico with a battery.
    - Understanding how can a Raspberry Pi Pico be powered using a Battery.

---

## :bulb: Technologies Used

### Micro-Python

### Components/Items Required:

<img src="IOT Project/project-image/Components.png"/>



---
## :iphone: Screenshots



<img src="IOT Project/project-image/LED Implementation.png"/>
<img src="IOT Project/project-image/Buzzer Implementation.png"/>
<img src="IOT Project/project-image/OLED Implementation.png"/>
<img src="IOT Project/project-image/Final Image.jpg"/>

---

## :man: Project Created & Maintained By

<img src = "IOT Project/project-image/profile.png"  height="130" alt=""> <br>Ashwini Kumar Behera
<p>
<a href = "https://github.com/Kumar2390"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/ashwini-kumar-behera-14a9a4215/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
