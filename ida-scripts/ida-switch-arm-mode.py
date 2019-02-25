def thumb_mode_range(start_addr, end_addr):
    for addr in range(start_addr, end_addr, 2):
        SetRegEx(addr, "T", 1, SR_user)
        MakeCode(addr)


def arm_mode_range(start_addr, end_addr):
    for addr in range(start_addr, end_addr, 4):
        SetRegEx(addr, "T", 0, SR_user)
        MakeCode(addr)
