'''
*****************************************
Bitmap check for Bad Blocks
*****************************************
Purpose: this API is for checking the bitmap for Bad Blocks for each dies
Limited: This API currently could maximally read 256 bit every time, thus could only read 1 die per time.
Possible Improvement: change it to check by word (thus check 256*4=1024 bad blks per line)

'''
from Tkinter import Tk
from tkFileDialog import askopenfilename

HDB=16
Base=8  # hex is 8, bin is 1
Bytes_Per_line=32
BB = [0 for x in xrange(10)]

print "The bit map file should be in below format:"
print "data in Hex mode, each line contains 32 number, and show in word form"

print "please select the config of product you are testing"
print '''Product Config Type: 0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  3---------1Y Ex2 4P 16K
if (TYPE==0):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x10c '
elif(TYPE==1):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x214'
elif(TYPE==2):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x220 '
elif(TYPE==4):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x218 '''
    
TYPE=input("Product Config Type: 0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  3---------1Y Ex2 4P 16K ")
print "TYPE=",TYPE

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

#Product Config Type: 0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  3---------1Y Ex2 4P 16K
if (TYPE==0):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x10c '
elif(TYPE==1):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x214'
elif(TYPE==2):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x220 '
elif(TYPE==4):
    BLOCK_BIT_MAP_START='0x8007830c'
    BB_MAP_BLOCK_BYTES='0x218 '
    

line=-1
die=0
bb_count=-1
with open(filename) as f:
  for lines in f:
      line=line+1
      if (len(lines)>20):
          
        line_hex=str(lines[10:-37].replace(' ','').replace('_',''))
        line_bin=bin(int(line_hex, HDB)).zfill(Bytes_Per_line*Base)
       
      for i in range(0,32):
          for j in range(0,8):
              if(line_bin[8*i+8-j-1]=='1'):
                  BB[die]=BB[die]+1
                  die=(line*Bytes_Per_line*Base+i*8+j)/(int(BB_MAP_BLOCK_BYTES,base=16)*8)
                  print 'Die--'+str(die)+',  BB Number--',BB[die],', block',hex((line*Bytes_Per_line*Base+i*8+j) % (int(BB_MAP_BLOCK_BYTES,base=16)*8))
