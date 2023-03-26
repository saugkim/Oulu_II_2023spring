**Programming course work**

Programming assignment

Student creates a program that communicates with the server using TCP and UDP protocols. The work consists of a basic part and additional parts. Course work can be done either independently or in a group, please note the slight difference in grading principles between single person/group returns. The detailed requirements for the program can be found in the pdf file in the return box.

Basic part: 

The program sends a message to the server using TCP and parses the message with the UDP port and its own ID. The program sends a message to the UDP port of the server and receives a list of words. The program translates the word order and sends it back to the server. This is repeated until the server indicates that it is running out of messages.

Connecting to the server: The server your implementation is talking to can be found at 195.148.20.105, port 10000.

Additional parts:

* Encryption: messages are encrypted

* Parity: messages are parity added.

* Multipart messages: messages can arrive in multiple parts.


Grading:
```
Individual work:

Basic part: 7 pts.
One additional part: +2 pts
Two additional parts: +2 pts
Three additional parts: +2 pts
Return before the early bird return deadline: +1 pts
Works properly at first return: +1 pts
Group work (2-4 pers):


Basic part: 4 pts.
One additional part: +3 pts
Two additional parts: +3 pts
Three additional parts: +3 pts
Return before the early bird return deadline: +1 pts
Works properly at first return: +1 pts
```

The following links are a good place to start if you are unfamiliar with python sockets, struct, decoding and strings:

https://www.tutorialspoint.com/python/python_networking.htm

https://docs.python.org/3/library/struct.html

https://www.pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/

https://www.tutorialspoint.com/python3/python_strings.htm


Tämän tehtävän voi palauttaa aikaisintaan keskiviikko, 5. huhtikuuta 2023, 10:00
