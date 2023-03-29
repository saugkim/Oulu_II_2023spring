Q1. IP-osoitteet

Verkkokerroksen IP-protokollan osoitteen (IP-osoite) perusteella siirretään paketteja verkossa. Mikä tai mitkä seuraavista väittämistä ovat totta?   

Network layer uses IP addresses to route packets in networks. Which of the following statements are true?

```
Valitse yksi tai useampi:

a. Kytkin tietää IP-osoitteen perusteella, mihin suuntaan saapunut paketti kytketään 
- Switch uses IP address to determine to which port to transmit the arrived packet

b.IP-osoite yksilöi aina yhden tietokoneen: samalla IP-osoitteella lähetetyt paketit eivät voi olla tarkoitettuja eri tietokoneille 
- IP address is always a unique identifier for a host

c.Verkkokortti tunnistaa IP-osoitteen perusteella, että onko kyseinen kehys osoitettu tälle laitteelle 
- Network interface card uses IP address to identify if the frame is addressed to this host

* d.Reititin tietää IP-osoitteen perusteella, mihin suuntaan saapunut paketti reititetään 
- Router uses the IP address to determine where to route the arrived packet

e.Tietokone tietää IP-osoitteen perusteella, mille ohjelmalle saapunut paketti ohjataan 
- Computer knows using the IP address to which application the packet should be routed

```

Q2. Reitityksen perusteita (fundamentals of routing)

Oletetaan, että valittavalla reitillä lähteestä kohteeseen on kolme reititintä. Jos paketteja ei ositeta, kuinka monta reititystaulukkoa joudutaan käymään lävitse, kun paketti toimitetaan lähteestä kohteeseen?

There are three switches on the route from source to destination. If packets are not fragmented, how many routing tables are required for packet delivery from source to destination?

Vastaus:



Q3. Aliverkon peite (subnet mask)

Verkon aliverkon peite (subnet mask) on 255.255.240.0. Mikä on suurin määrä päätelaitteita (host), joka tällä verkolla voi olla?

Subnet mask is 255.255.240.0. What is the maximum number of hosts that can be in this network?

Vastaus: 4094


Q4. Verkko-osoite IP-osoitteen ja aliverkon peitteen perusteella

Päätelaitteen IP-osoite on 172.16.45.13 ja aliverkon peite on 255.255.224.0. Mikä on verkon osoite? (anna vastauksesi IP-osoitteiden vakiintuneessa esitysmuodossa a.b.c.d missä a-d ovat kokonaislukuja välillä 0-255)

IP address of a host is 172.16.45.13 and the subnet mask is 255.255.224.0. What is the netid?

Vastaus: 172.16



Q5. Aliverkkojen määrä verkossa

Jos verkon osoite on 192.168.100.0 ja aliverkon peite on 255.255.255.192, kuinka monta aliverkkoa kyseisessä verkossa on? (Tutustu aliverkotukseen)

If the netid of a network is 192.168.100.0 and the subnet mask is 255.255.255.192, how many subnets does the network have? (Read about subnetting)

Vastaus: 4


Q6. 512k problem

Kaikki muistavat Y2K-ongelmaan liittyneen suoranaisen paniikin. Moni teistä on lukenut Y2K-ongelmasta historiankirjoista.  Mutta mikä on 512K-ongelma?

```
Valitse yksi:

a. Yli 512 kilotavun pakettien reititys internetissä on vaikeaa, koska useimpien linkkien MTU, eli suurin mahdollinen siirrettävä yksikkö on tätä pienempi 
- Routing of over 512 kB packets in the internet is difficult because the maximum transmission unit (MTU) of most links is smaller than 512 kB

* b.Vuonna 2014 internetin BGP-reitittimien reititintaulukot ylittivät useissa laitteissa reititystaulukoiden maksimi reittien määrän (512k), ja internet lakkasi toimimasta. 
- In 2014, BGP routing tables exceeded the limit of 512k routes, causing internet service issues.

c. 512K on amerikkalaiseen eläkejärjestelmään liittyvä säästöohjelma. 
- 512K is a defined-contribution plan of the United States retirement system

d. Vanhojen tietokoneiden käyttöjärjestelmien päämuistin (RAM) ylin mahdollinen koko oli 512 kilotavua, mikä on riittämätön koko nykyisiin tarpeisiin 
- The maximum RAM size of ancient operating systems was 512 kB, which was not enough for modern need

e. IPv4 osoiteavaruudessa on korkeintaan 512 000 eri osoitetta, ja ne ovat loppumaisillaan 
- IPv4  address space has 512 000 unique addresses, and the address space will be exhausted soon

f. Vuonna 512000 tietokoneet lakkaavat toimimasta, lentokoneet tippuvat taivaalta ja ihmiskunta taantuu kivikaudelle 
- In 512000, computers will self-destruct, airplanes will fall from the sky and humanity will regress to the stone age
```


Q7. Paketin kulku lähiverkosta toiseen


Luennoilla esiteltiin paketin liikkuminen lähiverkosta toiseen seuraavalla kuvalla:

<img src="https://user-images.githubusercontent.com/25344978/228616312-6250962c-4afe-4c5d-8837-3107ba06b1c9.png" width=350>


```
Jos A lähettää paketin B:lle tapahtuu seuraavat askeleet:

1. A löytää seuraavaksi askeleeksi reititintaulukostaan IP = 111.111.111.110 ja rakentaa datagrammin B:n IP-osoitteella
2. A selvittää ARP-taulukosta osoitteen 111.111.111.110 MAC-osoitteeksi E6-E9-00-17-BB-4B ja rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella sekä lähettäjäosoitteella 74-29-9C-E8-FF-55 
3. Kehys lähetetään LAN 1 -verkkoon
4. R tunnistaa oman MAC-osoitteensa kehyksestä ja ottaa viestin vastaan
5. R purkaa kehyksen, lukee datagrammin otsikkotiedot, ja lukee reititystaulukosta, että vastaanottajaosoite löytyy LAN2-suuntaan olevasta linkistä
6. ?
7. Kehys lähetetään LAN2-verkkoon
8. B tunnistaa oman MAC-osoitteensa kehyksen otsikkotiedosta, lukee ja purkaa kehyksen ja toteaa datagrammin IP-osoitteesta, että paketti on osoitettu sille itselleen.
Mikä seuraavista kuvauksista sopii kohtaan 6?
```

In lectures, the following packet routing diagram from LAN to another LAN was introduced:

```
When A transmits a packet to B, the following happens:

1. A does routing table lookup for 111.111.111.110 and uses B's IP address as the destination in the IPv4 datagram
2. A does ARP table lookup for 111.111.111.110 and finds out that E6-E9-00-17-BB-4B is the MAC address for that IP address. A uses that as destination address in the Ethernet-frame and 74-29-9C-E8-FF-55 as the source address.
3. The frame is transmitted to the LAN1 network
4. R finds out that the frame destination MAC address is theirs and receives the message.
5. R reads the payload, parses datagram headers, and does routing table lookup for the destination address, and finds out that the destination is behind the LAN2 link.
6. ?
7. The frame is transmitted to the LAN2 network
8. B parses the frame header finds out that the MAC address matches theirs. Therefore, it parses the IP address of the datagram and finds out that the destination IP address matches theirs; therefore, the packet has reached the destination.
```

Which of the following is performed at step 6.?

```
Valitse yksi:

a. R lukee ARP-taulukosta osoitteen 222.222.222.220 MAC-osoitteen (1A-23-F9-CD-06-9B), rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella ja lähettäjäosoitteella 49-BD-D2-C7-56-2A 
- R does ARP lookup for 222.222.222.222, finds out that the MAC address is 1A-23-F9-CD-06-9B, constructs Ethernet frame, and uses that as the destination address and 49-BD-D2-C7-56-2A as the source address

* b. R lukee ARP-taulukosta osoitteen 222.222.222.220 MAC-osoitteen (1A-23-F9-CD-06-9B), rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella ja lähettäjäosoitteella E6-E9-00-17-BB-4B 
- R does ARP lookup for 222.222.222.222, finds out that the MAC address is 1A-23-F9-CD-06-9B, constructs Ethernet frame, and uses that as the destination address and E6-E9-00-17-BB-4B as the source address

c. R lukee ARP-taulukosta osoitteen 222.222.222.222 MAC-osoitteen (49-BD-D2-C7-56-2A), rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella ja lähettäjäosoitteella 1A-23-F9-CD-06-9B 
- R does ARP lookup for 222.222.222.222, finds out that the MAC address is 49-BD-D2-C7-56-2A, constructs Ethernet frame, and uses that as the destination address and 1A-23-F9-CD-06-9B as the source address

d. R lukee ARP-taulukosta osoitteen 222.222.222.222 MAC-osoitteen (49-BD-D2-C7-56-2A), rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella ja lähettäjäosoitteella E6-E9-00-17-BB-4B 
- R does ARP lookup for 222.222.222.222, finds out that the MAC address is 49-BD-D2-C7-56-2A, constructs Ethernet frame, and uses that as the destination address and E6-E9-00-17-BB-4B as the source address

e. R lukee ARP-taulukosta osoitteen 222.222.222.222 MAC-osoitteen (49-BD-D2-C7-56-2A), rakentaa Ethernet-kehyksen sillä vastaanottajaosoitteella ja lähettäjäosoitteella 74-29-9C-E8-FF-55 
- R does ARP lookup for 222.222.222.222, finds out that the MAC address is 49-BD-D2-C7-56-2A, constructs Ethernet frame, and uses that as the destination address and 74-29-9C-E8-FF-55 as the source address
```

Q8. Virheellisten reittien mainostaminen

Lue oheinen artikkeli: https://arstechnica.com/information-technology/2010/11/how-china-swallowed-15-of-net-traffic-for-18-minutes/

Mikä seuraavista väittämistä pitää paikkansa?

Which of the following statements is true?

```
Valitse yksi:

a.Virheellisesti mainostetut reitit eliminoituvat nopeasti ja automaattisesti 
- Incorrectly advertised routes are eliminated quickly and automatically

b.Internetin reititysjärjestelmä perustuu luottamukseen siitä, että mainostetut reitit ovat oikeellisia 
- Internet routing is based on the trust that the advertised routes are correct

c.Reititysjärjestelmän rakenne ehkäisee reitityskonfigurointivirheiden leviämisen laajemmalle internettiin 
- The design of the routing system mitigates for propagation of route configuration mistakes to the rest of the internet

d.Reititysprotokollat sisältävät mekanismin, jolla mainostetun reitin oikeellisuus voidaan todeta 
- Routing protocols are capable of ensuring authenticity of advertised routes

e.Internet-reitityksen BGP-protokolla käyttää vahvaa salausta ja autentikointia 
- BGP protocol uses strong encryption and authentication

f.Ison valtion tiedusteluelimet eivät voisi hetkellisesti ohjata lähes kaikkea internet-liikennettä omille palvelimilleen tarpeen niin vaatiessa 
- State-sponsored actors cannot momentarily route almost all internet traffic through their servers

g.Pahantahtoinen reititintoimija ei voisi sotkea maailmanlaajuista internet-liikennettä edes hetkellisesti 
- Malicious actor cannot cause world-wide internet disruption even momentarily by advertising incorrect routes
```

Q9. Djikstra

<img src="https://user-images.githubusercontent.com/25344978/228617977-5ef68023-0e75-4faa-b55f-deeffb794cb0.png" width=350>

Ohessa luennoilta Dijkstran algoritmin sovellus solmulle u. Jos algoritmia sovelletaan solmuun w, mikä on N' kahden askeleen jälkeen?

If Dijikstra's algorithm is applied on node w, what is the value of N' after two steps?

```
Valitse yksi:

a.wzx b.wvy c.wyu d.wzv e.wyx f.wxz g.wvx   
h.wvu i.wuy j.wzy k.wyv l.wuz m.wux n.wxy   
o.wxu p.wvz q.wzu r.wyz s.wuv  
```


Q10. Etäisyysvektorireititys (distance-vector routing)

<img src="https://user-images.githubusercontent.com/25344978/228618781-5bf0128c-ffba-48aa-a25f-d481c0d96260.png" width=200>

Oheisen kuvauksen mukaisessa verkossa tapahtuu punaisella merkitty muutos linkkien painoarvoihin. Montako aika-askelta kestää, ennen kuin etäisyysvektorireititystä käytettäessä etäisyystaulukot ovat stabiloituneet?

The weight of a link is changed as seen from the diagram. When using distance-vector routing, how many time steps it takes until distance-vector tables have stabilized?

Vastaus: 

