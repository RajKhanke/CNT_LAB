1. Websocket in c  - client.c , server.c
2. Line Encoding - lineencoding.py
3. Open shortest path first Djikstra in python  - djisktra.py


steps to run websocket :

save two files client.c server.c

split in two terminal

in each temrinal first run commands :

 gcc client.c -o client -lws2_32  
 
 gcc server.c -o server -lws2_32  

then on frst start the server by ./server command

then start the client by ./client

