from pwnlib.util.hashes import sha1sumhex

# serial number decoding: https://en.tab-tv.com/?p=18929
SERIAL = "FKTDP621JC6H"
ECID = "2843135617639718"
WIFI = "14:88:e6:ac:63"
BLUETOOTH = "14:88:e6:ac:64"
print(sha1sumhex(SERIAL + ECID + WIFI + BLUETOOTH))