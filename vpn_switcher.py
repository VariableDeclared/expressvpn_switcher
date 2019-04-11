#!/usr/bin/env python3

import os
import random

def load_vpn_list():
    startpoints = []
    with open("list.txt") as fh:
        startpoints = [line.split("\t")[0] for line in fh.readlines()]

    return startpoints


def main():
    locations = load_vpn_list()
    print("[INFO] Locations: {}".format(locations))
    res = os.popen("expressvpn disconnect").read()
    res = os.popen("expressvpn connect {}".format(random.choice(locations))).read()
    print ("[INFO] Connected to: {}".format(res))

if __name__ == "__main__":
    main()