![alt text](docking_optimized.gif)
# Docking system

This system was mainly created by using reference from TAC challange

Main focus of the system is docking the AUV on the top of the platform by using AruCo's codes.

System firstly detects the arucos and takes the center of them.
In case of an detection error, short time memory stores the old position of the arucos.
After centerizing itself, it dives until it touches. 

While touch moment can be controlled, by some methods like TTC using camera or sonars. Best way to get it controlling the electrical connection between dock and AUV which outside of this document's topic
