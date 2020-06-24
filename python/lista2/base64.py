#! /usr/bin/python3
import os
import sys
import base64


def base64Encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    bit_str = ""      
    base64_str = ""

    for char in data:
        bin_char = bin(char).lstrip("0b")
        bin_char = bin_char.zfill(8)
        bit_str += bin_char 

    brackets = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]

    for bracket in brackets:
        if(len(bracket) < 6):
            bracket = bracket + (6-len(bracket))*"0" 
        base64_str += alphabet[int(bracket,2)]

    return base64_str

def base64Decode(text):
        alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
        bit_str = ""
        text_str = ""

        for char in text:
            if char in alphabet:
                bin_char = bin(alphabet.index(char)).lstrip("0b")
                bin_char = bin_char.zfill(6)
                bit_str += bin_char

        brackets = [bit_str[x:x+8] for x in range(0,len(bit_str),8)]

        for bracket in brackets:
            text_str += chr(int(bracket,2))

        return text_str.encode("latin-1")

try:
    if sys.argv[1] == "--encode":
        w = open(sys.argv[3], "w") 
        with open(sys.argv[2], "rb") as f:
            byte = f.read(57)
            while byte:
                w.write(base64Encode(byte))
                w.write("\n")
                byte = f.read(57)
            w.close()
        f.close()

    elif sys.argv[1] == "--decode":
        w = open(sys.argv[3], "wb") 
        with open(sys.argv[2], "r") as f:
            byte = f.read(77)
            while byte:
                w.write(base64Decode(byte))
                byte = f.read(77)
            w.close()
        f.close()
    
    else:
        print("Wpisz na początku --encode lub --decode")
        exit(0)

except FileNotFoundError:
    print("Podany plik nie istnieje")
except IndexError:
    print("Write:\n")







