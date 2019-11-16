# CPEN442-Prototype
Design Project:
A simulation of Car Relay Theft Prevention using pygame and console windows

Why is this problem important?
Car Relay Theft: common, cheap, easy to execute

![alt text](https://github.com/Nico628/CPEN442-Prototype/relay.png)
source: https://www.cbc.ca/news/canada/toronto/electronic-car-theft-rising-1.5138877

How is this problem currently addressed by others?
- Ultra Wideband technology to ensure key fob is physically nearby
- Rolling-code pseudorandom numbers for encrypted signals
- Key fob motion sensors

What is the way we are proposing to address the problem?
- Dual authentication “public key” system
    Car signs a message -> Key fob
    Key fob verifies message using car’s public key
    Key fob signs same message -> Car
    Car verifies message is the same
    Key fob initiates above procedure in case of failure, followed by a safety time-out if process fails again
    Time-stamp used as nonce

Why and in what respect is our way to address the problem better than others?
- Existing solutions vulnerable to signal skimming
- Solves lack of authentication
- Limits replay and man-in-the-middle attacks


