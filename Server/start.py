from record import record_sound
from socket import *
import os

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 5000))
    sock.listen(1)
    connSock, addr = sock.accept()
    print("Accept!")

    try:
        while True:
            record_sound()
            os.system("deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio file.wav > result.txt")
            
            with open("result.txt", "r") as f:
                lines = f.readlines()
                print(lines)
                connSock.send(lines[0].encode('utf-8')) 

    except Exception as ex:
        print("Error:", ex)
    
    connSock.close()
    sock.close()
    
