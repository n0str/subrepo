import binascii

str = [0x53 ,
0x50 , 0x61 , 0x0B , 0x5B , 0x88 , 0xCB , 0x03 , 0x5B , 0x61 , 0x0B , 0xF4 , 0xD8 , 0x52 , 0xF4 , 0xEA , 0x43 ,
0x6A , 0x68 , 0x60 , 0x6E , 0x6F , 0x2A , 0x0B , 0x52 , 0x64 , 0x7E , 0x2C , 0x7D , 0x6E , 0x2B , 0x69 , 0x6E ,
0x6E , 0x65 , 0x2B , 0x63 , 0x6A , 0x68 , 0x60 , 0x6E , 0x6F , 0x2A , 0x0B ]

for byte in range(0x00, 0xFF):
	newStr = []
	for c in str:
		newStr.append(c ^ byte)
	res = ''.join(hex(c)[2:].zfill(2) for c in newStr)
	
	if "6a" in res and "ff" in res and "00" in res:
		print(byte)
		print(binascii.unhexlify(res))
