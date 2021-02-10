# Packet-Sniffer
## ⚠ Disclaimer
### Use this at your own disretion. The developer is not responsible for any misuse of the tool.

Packet Sniffer allows you to view network traffic flowing thru a system.


**To use this:**

    1. Clone this repository
    2. Run packet_sniffer.py if you are using python2.x
    3. Run packet_sniffer3.py if you are using python3.x
    
**Dependencies:**

    scapy module
    scapy_http module

Make sure you have the latest versions of the above modules to avoid any unusual errors.
    
**Intructions to install modules:**
    
    1. pip install scapy
    2. pip3 install scapy (Use this for python3 support)
    3. pip install scapy_http

*This is **currently** supported only on **UNIX** environment, but can be targetted against **any** system irrespective of it's OS*

> ***scapy_http** is a third party module used to add support to HTTP in scapy*

Using <a href="https://github.com/vinsdragonis/ARP-Spoofer">ARP Spoofer</a>, you can sniff packets traveling thru remote systems.

This supports only HTTP requests for the moment, and not HTTPS.

- [x] Completed
