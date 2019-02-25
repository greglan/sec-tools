def data_range(start_addr, end_addr):
    for addr in range(start_addr, end_addr, 4):
        MakeUnkn(addr, 1)
        MakeDword(addr)

def code_range(start_addr, end_addr):
    for addr in range(start_addr, end_addr, 4):
        MakeCode(addr)
        MakeDword(addr)
