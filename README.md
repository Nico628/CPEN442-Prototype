# CPEN442-Prototype
Design Project:
A simulation of Car Relay Theft Prevention using pygame and console windows

Why is this problem important?
Car Relay Theft: common, cheap, easy to execute

![alt text](https://github.com/Nico628/CPEN442-Prototype/blob/master/relay.png)

source: https://www.cbc.ca/news/canada/toronto/electronic-car-theft-rising-1.5138877

How is this problem currently addressed by others?
- Ultra Wideband technology to ensure key fob is physically nearby
- Rolling-code pseudorandom numbers for encrypted signals
- Key fob motion sensors

What is the way we are proposing to address the problem?
- Dual authentication “public key” system
    Key fob says Hi -> Car
    Car signs a message -> Key fob
    Key fob verifies message using car’s public key
    Key fob signs same message -> Car
    Car verifies message is the same
    (Everytime an RF signal is sent from the car, the car sets a timeout based on the time needed for a Radio Repeater to retransmit. If a response is received inside the timeout window, it is implied that no Radio Repeater is used i.e. no man-in-the-middle)

Why and in what respect is our way to address the problem better than others?
- Existing solutions vulnerable to signal skimming
- Solves lack of authentication
- Limits replay and man-in-the-middle attacks



source of images in this repo:
https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.wired.com%2Fwp-content%2Fuploads%2F2016%2F04%2Fpress04-model-x-rear-three-quarter-with-active-spoiler.jpg&imgrefurl=https%3A%2F%2Fwww.wired.com%2F2016%2F04%2Fteslas-model-x-bigger-problems-faulty-falcon-doors%2F&docid=HpA7M8OovcBayM&tbnid=bxyC9aPcOsl1_M%3A&vet=1&w=2000&h=1500&bih=564&biw=1154&ved=2ahUKEwjeqrGbquvlAhWSK30KHWd8BfsQxiAoBXoECAEQIQ&iact=c&ictx=1
https://www.google.com/imgres?imgurl=https%3A%2F%2Fedge.alluremedia.com.au%2Fm%2Fg%2F2016%2F07%2Ftesla_model_x_1.jpg&imgrefurl=https%3A%2F%2Fwww.gizmodo.com.au%2F2016%2F07%2Fthe-tesla-model-x-will-cost-the-same-as-model-s-in-australia%2F&docid=efOr6TscCJvgnM&tbnid=4S4p9Onv8JTQoM%3A&vet=1&w=1920&h=1080&bih=564&biw=1154&ved=2ahUKEwjeqrGbquvlAhWSK30KHWd8BfsQxiAoB3oECAEQJQ&iact=c&ictx=1
https://shop.tesla.com/product/model-3-key-fob
https://www.iconfinder.com/icons/2951272/attacker_criminal_cybercriminal_hacker_keylogger_user_icon


