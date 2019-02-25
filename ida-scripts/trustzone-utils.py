def decode_svc_atomic(code):
    n = code & 0xf
    svc = (code >> 10) & 0xff
    cmd = (code >> 12) & 0x3ff

    print("n: %d" % n)
    print("svc: 0x%X" % svc)
    print("cmd: 0x%X" % cmd)


def decode_sip_fnid(fnid):
    n = fnid & 0xff
    service_id = (fnid >> 8) & 0xff

    print("n: 0x%X" % n)
    print("Service ID: 0x%X" % service_id)
