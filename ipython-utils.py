def bin_formatter(n):
    SPACE = ' '
    tmp_binary = bin(n)[2:]
    n = len(tmp_binary)

    if n <= 8:
        n_bits = 8
    elif n <= 16:
        n_bits = 16
    elif n <= 32:
        n_bits = 32
    elif n <= 64:
        n_bits = 64

    binary_str = ""
    sub_binary_str = ""

    for k in range(n_bits):
        if k < n:
            binary_str = SPACE + tmp_binary[-1-k] + binary_str
        else:
            binary_str = SPACE + '0' + binary_str

        if (k+1) % 4 == 0:
            binary_str = SPACE + binary_str
            bit_index = str(k)
            sub_binary_str = SPACE + bit_index + SPACE * (8-len(bit_index)) + sub_binary_str

    return binary_str[2:] + "\r\n" + sub_binary_str[1:-2] + '0'

def pp_bin(n):
    print(bin_formatter(n))

def hex_on():
    formatter = get_ipython().display_formatter.formatters['text/plain']
    formatter.for_type(int, lambda n, p, cycle: p.text("0x%X" % n))

def int_on():
    formatter = get_ipython().display_formatter.formatters['text/plain']
    formatter.for_type(int, lambda n, p, cycle: p.text("%d" % n))

def bin_on():
    formatter = get_ipython().display_formatter.formatters['text/plain']
    formatter.for_type(int, lambda n, p, cycle: p.text(bin_formatter(n)))
