#!/usr/bin/env python3

import sys

from yt_dlp import webvtt

if len(sys.argv) < 2:
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "rb") as fp:
    lines = fp.readlines()

    for x in webvtt.parse_fragment(b''.join(lines)):
        if isinstance(x, webvtt.Magic):
            print("Magic:")
            if x.extra is not None:
                print('Extra:', x.extra)
            if x.local or x.mpegts:
                print('Local timestamp:', _format_ts(x.local if x.local is not None else 0))
                print('MPEGTS timestamp:', str(x.mpegts if x.mpegts is not None else 0))
            if x.meta:
                print('Metadata:', x.meta)
            print()
        elif isinstance(x, webvtt.CueBlock):
            print(x.as_json)
        else:
            print(x, x.raw)
