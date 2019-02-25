def NopBytes(start, length):
  for i in range(0, length):
    PatchByte(start + i, 0x90)
  MakeCode(start)
