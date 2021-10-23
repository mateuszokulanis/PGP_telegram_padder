import hashlib
import random
import binascii
from time import sleep

bytes_per_line = 2048
sha512_iters = 2000;
gen_lines = ''

def gen_rand_numbers(section,lines):
    tmp_preamble = ""
    small_iter = 0
    gen_lines = ''
    for i in range(lines*bytes_per_line):
        print(section + "randsection gen " + str(i) + '/' + str(lines*bytes_per_line))
        number = r.randint(0, 255)
        tmp = str(hex(number)).lstrip("0x").rstrip('L')
        gen_lines += tmp
        if(small_iter == bytes_per_line):
            m = hashlib.sha512()
            for i in range(sha512_iters):
                m.update(gen_lines.encode('utf-8'))
            digest_str = str(binascii.hexlify(m.digest()))
            digest_str = digest_str[2:-1]
            tmp_preamble += digest_str + "\n"
            small_iter = 0
            gen_lines = ""
            sleep(0.05)
        else:
            small_iter += 1
        if(small_iter%28 == 0):
            sleep(0.005)
    return tmp_preamble

r = random.SystemRandom()
number = r.randint(0,255)


preamble = r.randint(8,20)
preamble_str = gen_rand_numbers("PREAMBLE GEN \t", preamble)
sleep(1.23456)
postamble = r.randint(17,33)
postamble_str = gen_rand_numbers("POSTAMBLE GEN \t",postamble)

ready_string = preamble_str + "\n<-----START----->\n\n" + "\n\n<-----STOP----->\n\n"+ postamble_str


path = r'C:\Users\xxx\Desktop\message.txt'
File = open(path,'w')
File.writelines(ready_string)
File.close()
