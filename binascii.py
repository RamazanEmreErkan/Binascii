import sys
import argparse
import os
from re import findall

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", help="File path for text. Example: TextFileName {without '.txt'}", action="store")
parser.add_argument("-c", "--conversion", help="Select conversion type. Example:'-c encode' or '-c decode'", action="store")
args = parser.parse_args()

def Main():
    if args.conversion=="encode":
        text_name_encode(args.text)
    elif args.conversion=="decode":
        filew(args.text)
    else:
        print("Error")

def text_name_encode(textenc): #string to bin
    enc =[]
    enc2=[]  
    with open(textenc + ".txt", "r", encoding="utf-8") as isim:
        chars = []
        for line in isim:
            for c in line:
                chars.append(c)
    
        enc1 = [bin(ord(i))[2:].zfill(8) for i in chars]
        enc2=enc1[:-1]
        strEnc2=''.join(enc2)
        enc3=strEnc2.split()
        strEnc3=' '.join([strEnc2[x:x+8] for x in range(0,len(strEnc2), 8)])
        

    print(strEnc3)

def text_name_decode(textdec): #bin to string
    with open(textdec+".txt","r") as list:
        dec = ''.join([chr(int(x, 2)) for x in list])
        print(dec)
    file_erase(textdec)

def filew(textdec):
    with open(textdec + ".txt", "r") as list:
        d = []
        for x in list:
            d.append(x)
        b = str(d)
        
        Null="".join(b.split())
        Null1=Null.replace("[", "") 
        Null2=Null1.replace("]", "")
        Null3=Null2.replace("'", "")
        list1=findall("........",Null3)
        c=" ".join([x for x in list1])
        c1=c.replace(" ","\n")
        
        f = open(textdec+"2.txt", "w")
        f.write(c1)
        f.close()
    text_name_decode(textdec+"2")

def file_erase(textdec):
    os.remove(textdec+".txt")

if __name__ == '__main__':
    Main()
