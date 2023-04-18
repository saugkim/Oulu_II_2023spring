**Kysymys 1**

Toistoviive (playout delay)

![image](https://user-images.githubusercontent.com/25344978/232873986-4901c5de-723b-409e-9fa2-2d29b6f7dfa1.png)


Oheisessa kuvassa näkyy pakettien syntyminen lähettäjällä sekä niiden saapuminen toistettavaksi vastaanottajalle. Kuinka monen toistoyksikön mittainen toistoviiveen tulee olla (mitattuna tallennushetkestä), jotta yksikään kahdeksasta ensimmäisestä paketista ei myöhästy toistosta?

------

In the diagram above, one can seen when packets are generated at the sender and when they arrive at the repeater. How many time units does the playout delay have to be in order for all eight packets to arrive in time for playout? 

Vastaus:

**Kysymys 2**

Polettiämpärijärjestelmä (token bucket)

![image](https://user-images.githubusercontent.com/25344978/232874164-1140da27-3f72-49b4-9c1f-726f3883f42b.png)

Oheisen kuvan mukaisessa tilanteessa polettiämpäriin saapuu poletti per aikayksikkö, ja poletteja mahtuu ämpäriin korkeintaan kaksi. Ämpäri on alkuun täynnä. Viestejä saapuu jonoon jonosta vasempaan esitetyssä aikajärjestyksessä (esim. paketti #6 saapuu juuri ennen ajanhetkeä 3, eli ehtii prosessoitavaksi kyseisellä ajanhetkellä). Paketit 1 ja 2 lähetetään ajanhetkellä 0, koska molemmille on ämpärissä poletti. Millä ajanhetkillä muut paketit lähetetään?

Anna vastauksesi muodossa: n3,n4,n5,n6,n7,n8,n9,n10 

Kukin n siis on kyseisen paketin lähetysaikayksikkö. Esimerkiksi: jos paketit 3-7 lähetettäisiin ajanhetkellä 3, ja paketit 8-10 ajanhetkellä 5, vastauksesi olisi: 3,3,3,3,3,5,5,5

------

In the situation seen in the above diagram, token bucket algorithm is used to limit burstiness. Tokens are put into the bucket at constant rate of one token per time slot. The bucket has capacity of two tokens.

The bucket is full at start. Packets arrive at the queue from the left as seen in the diagram (for example, #6 arrives just before time slot 3, and so is processed at time slot 3). Because the bucket has two tokens, packets one and two are sent at time slot 0. When are other packets sent?

Express your answer as: n3,n4,n5,n6,n7,n8,n9,n10, where n is the time slot when the corresponding packet is sent from the queue. For example, if packets 3 - 7 are sent at time slot 3 and packets 8 - 10 at time slot 5, your answer would be: 3,3,3,3,3,5,5,5


**Kysymys 3**  

Jonotusviive (queuing delay)

![image](https://user-images.githubusercontent.com/25344978/232874325-82c31306-db8e-4fdf-a554-0c5f267d640e.png)

Kuvan mukainen järjestelmä pystyy lähettämään yhden paketin per ajanhetki. Paketti voidaan lähettää, kunhan se saapuu ennen ajanhetken alkua. Esimerkiksi kuvan paketin 1 kokema viive on 0, sillä se pääsee (jonon ollessa tyhjä), heti lähetettäväksi.

Laske keskimääräinen jonotusviive, kun jono käyttää prioriteettimenetelmää, jossa parilliset paketit lähetetään korkealla prioriteetilla ja parittomat matalalla prioriteetilla. Voit päätellä tai katsoa allaolevasta kuvasta pakettien lopullisen lähetysjärjestyksen.

Scheduling with priority queue (even index has higher priority)

![image](https://user-images.githubusercontent.com/25344978/232874517-768ba472-4942-4db4-bf1e-11224e044687.png)

Pyöristä vastauksesi kolmen desimaalin tarkkuuteen (esim. vastaus voisi olla 15,100)

------

The system described in the diagram can send one packet per time slot. A packet can be send out at the next time slot after it's arrival. For example, packet #1 has queuing delay of zero because the queue is empty; therefore, the packet can depart immediately (at t=1).

Compute the average queuing delay, when priority queue method is used. Packets with even index have higher priority than packets with odd index. The second image presents the sending order of the packets. Round to three decimal places (e.g., 15,100).

Vastaus:

**Kysymys 4**

Datapurskeen kesto
Uloslähtevän liikenteen suurin mahdollinen lähetysnopeus (M) on 25MB/s, mutta liikennettä rajoitetaan polettiämpärillä (token bucket), jonka maksimikapasiteetti (C) on 250KB ja uusia poletteja saapuu ämpäriin tahdilla (r) 2 MB/s.

Mikä on datapurskeen maksimikesto? Anna vastauksesi pyöristettynä millisekunteiksi ilman desimaaleja.

------

A router is using a token bucket algorithm for congestion control. It has a capacity (C) of 250 KB and the maximum output rate (M) of 25 MB/s. Tokens are inserted into the bucket at rate (r) of 2 MB/s. What is the maximum burst length (T)?

Round your answer to milliseconds with no decimals.


Vastaus:


**Kysymys 5**

Kauanko lähetys kestää?


Päätelaite lähettää 1MB datapurskeen, mutta uloslähtevää liikennettä rajoitetaan tehtävässä #4 esitellyn polettiämpärin avulla. Oleta, että ämpäri on jo täynnä, joten M*T määrä dataa voidaan lähettää jo datapurskeen aikana. Kauanko lopun datan (1MB-M*T) lähettämisessä kestää?

Kirjoita vastauksesi millisekunteina ilman desimaaleja.

------

A host needs to send 1MB of burst data, but the router is using the token bucket algorithm described in question #4. Assume that the bucket is already full, so M*T of the data is transmitted during the burst. How long does it take to transmit the rest (1MB-M*T) of the data?

Write your answer in ms without decimals.


**Kysymys 6**

RTP:n lähetysdatan määrä


RTP-protokollalla lähetetään stereoaudiopaketteja. Järjestelmä ottaa kaksi 16-bittistä näytettä (eli yhden näytteen kummallekin stereokanavista) 44100 kertaa sekunnissa.

Kuinka monta pakettia sekunnissa RTP:n täytyy lähettää, jos audiodataa lähetetään 1024 tavun paketteina?

Esitä vastauksesi desimaalilukuna yhden desimaalin tarkkuudella.

------

RTP is used to transmit stereo audio packets. A system samples both channels at rate of 44100 samples per second, each of them containing 16 bits of data. How many packets have to be transmitted using RTP, if audio data is segmented into 1024 byte packets?

Give your answer as a decimal number, round to one decimal place.

Vastaus:

**Kysymys 7**

FEC-menetelmä 1 - koodaus


Multimediajärjestelmässä virheitä voidaan peittää tai korjata erilaisilla FEC-menetelmillä. 

Järjestelmässä lähetetään 4 bittisiä datayksikköjä vastaanottajalle. 

Järjestelmän virheenkorjaus toteutetaan menetelmällä, jossa jokainen 4-bittinen datayksikkö koodataan 7-bittiseksi koodisanaksi (Aiheesta enemmän kiinnostuneet, ks. esim. https://en.wikipedia.org/wiki/Hamming(7,4)).

Valitse oikeat väittämät - mikä on käytetyn FEC-menetelmän vaikutus liikenteeseen:

------

In a multimedia system, errors can be corrected using Forward Error Correction (FEC) methods. The system in question implements error detection and correction by introducing redundancy into the system by encoding 4 bit data words into 7 bit data words (e.g., using Hamming(7,4)).

Choose the correct statements - how the chosen FEC method affect the network traffic characteristics:

Valitse yksi tai useampi:

a.
Järjestelmä pystyy korjaamaan kaikki bittivirheet aina kolmeen virheeseen saakka - The system can correct all errors up to three bit errors


b.
Kadonneet paketit pystytään korvaamaan - Lost packets can be replaced

c.
Dataliikenteen vaatima kaista 2,33-kertaistuu - Requires 2,33x bandwidth for data

d.
Järjestelmä havaitsee kaikki bittivirheet 4 bittiin saakka - The system can detect up to 4 bit errors


e.
Dataliikenteen vaatima kaista kaksinkertaistuu - Requires 2x bandwidth for data


f.
Toistoviive kasvaa merkittävästi - Introduces noticeable playout delay into the multimedia system


g.
Toistoviive lyhenee - Reduces playout delay

h.
Kadonneet paketit eivät heikennä toiston laatua - Lost packets do not degrade playout quality

i.
Yksittäiset bittivirheet aiheuttavat toistolaadun laskun - Single-bit errors degrade playout quality

j.
Dataliikenteen vaatima kaista pysyy samana - FEC does not introduce network traffic overhead



k.
Järjestelmä pystyy korjaamaan kaikki 1 ja 2 bitin virheet - The system can correct all one and two bit errors

l.
Toistoviive kasvaa - Increases playout delay

m.
Dataliikenteen vaatima kaista 1,75-kertaistuu - Requires 1,75x bandwidth for data



n.
Toistoviive pysyy kutakuinkin samana - Does not affect playout delay noticeably

o.
Dataliikenteen vaatima kaista 7-kertaistuu - Requires 7x bandwidth for data


**Kysymys 8**

FEC-menetelmä 2 - pariteettipaketti


Multimediajärjestelmässä virheitä voidaan peittää tai korjata erilaisilla FEC-menetelmillä. 

Järjestelmässä lähetetään 8-bittisiä datayksikköjä vastaanottajalle. 

Järjestelmän virheenkorjaus toteutetaan menetelmällä, jossa jokaista kahta datayksikköä kohden lasketaan kolmas paketti, jonka avulla kumpi vain kahdesta paketista voidaan palauttaa pariteettipaketin ja toisen paketin perusteella. Kuva menetelmästä alla

FEC-menetelmän kuvaus

Valitse oikeat väittämät - mikä on käytetyn FEC-menetelmän vaikutus liikenteeseen:

------

In a multimedia system, errors can be detected and corrected using FEC methods. The system in question transmits 8 bit data words to the receiver. The error correction is implemented by computing a third packet: a parity packet from the two data packets, which can be used to recover one packet of the two packets using the other packet and the parity packet (see the picture).

Choose the correct statements - how does the FEC method affect the network traffic characteristics?


Valitse yksi tai useampi:

a.
Laatu pysyy häiriöiden kasvaessa pitkään korkeana, mutta tippuu jyrkästi kun paketteja alkaa hukkumaan enemmän - Quality does not degrade until the communication channel experiences major packet loss, which causes significant degradation in quality

b.
Dataliikenteen vaatima kaista pysyy samana - Does not change the required bandwidth for data



c.
Toistoviive pysyy kutakuinkin samana - Playout delay is unaffected


d.
Dataliikenteen vaatima kaista kolminkertaistuu - Requires 3x bandwidth for data


e.
Toistoviive pienenee merkittävästi - Playout delay decreases significantly



f.
Dataliikenteen vaatima kaista kaksinkertaistuu - Requires 2x bandwidth for data

g.
Toistoviiveen on varmistettava, että pariteettipaketti ehtii myös saapua perille - In order to playout media chunk, all three packets have to arrive; therefore, playout delay increases

h.
Toistoviive lyhenee - Playout delay decreases

