Name: Kim Yukyeong   
ID:   2301815    
I have done alone and completed both exercises.  
 

**Potential bugs or other issues that your program has**  

Though UDP proxy test worked well with my pure udp test code (no tcp calls within loop-user input).     
I tested all my code with tcp-udp server setted up at my ubuntu-machine, which I am not sure about correctness of my server-side code.  

It would be quite nice, if school server is available for client-side test.   

I never succeeded with given PORT number, anyway I put port 20000 as a destination port (proxy).



**Short explanation on how to start your program** 

if port 20000 is available on 195.148.20.105,

**Exercise 1**
```
windows> ipython3 lab3.py 195.148.20.105 20000 "hello there"

linux> python3 lab3.py 195.148.20.105 20000 "hello there"

```

**Exercise 2**
```
DEST_PORT = 20000  hard-coded, currently (precisely whole time) not working  

windows> ipython3 lab3Proxy.py
linux> python3 lab3Proxy.py
```
