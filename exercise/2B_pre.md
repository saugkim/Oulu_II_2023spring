**Q1. Kuljetuskerroksen perusteita (transport layer fundamentals)**

Mitkä seuraavista väittämistä ovat totta?:

Find the true statements:

Valitse yksi tai useampi:

a.Kuljetuskerroksen protokollat yhdistävät fyysisesti kaksi verkkolaitetta toisiinsa - Transport layer protocols interconnect hosts physically

b.Kuljetuskerroksen protokollat yhdistävät päätelaitteiden prosesseja - Transport layer protocols interconnect application processes of hosts

c.Kuljetuskerroksen protokollat toteutetaan siirtokanavan bittivirrassa - Transport layer protocols are implemented in the bitstream of a communication channel

d.Kuljetuskerroksen protokollat yhdistävät päätelaitteita - Transport layer protocols interconnect hosts

e.Kuljetuskerroksen protokollat toteutetaan päätelaitteen käyttöjärjestelmässä - Transport layer protocols are implemented at operating system level

f.Kuljetuskerroksen protokollilla määritellään yhteyden kaistanleveys ja enimmäisviive - Transport layer protocols negotiate the bandwidth and maximum delay of a connection

g.HTTP, SNMP, SMTP ja FTP ovat käytetyimmät kuljetuskerroksen protokollat - HTTP, SNMP, SMTP and FTP are the most common transport layer protocols

h.Kuljetuskerroksen protokollien tehtävänä on estää törmäykset lähetyskanavassa - Transport layer protocols prevent collisions in the transmission channel

i.Kuljetuskerroksen protokollat takaavat viestien perillemenon ja virheenkorjauksen - Transport layer protocols guarantee transportation of messages to destination and error correction

<br> 
<br>

**Q2. UDP**

Valitse mikä tai mitkä seuraavista väittämistä EIVÄT ole totta mitä tulee UDP-protokollaan:

Which of the following UDP related statements are FALSE?

Valitse yksi tai useampi:

a.UDP on mahdollisimman ohut yläkerros IP-protokollalle - UDP has the minimum amount of overhead for a protocol on top of IP protocol

b.UDP:lla voidaan lähettää viestejä yhdeltä yhdelle, yhdeltä monelle, monelta yhdelle tai monelta monelle! -  UDP can be used to send messages from one-to-one, many-to-one, one-to-many or many-to-many using single socket!

c.UDP toimii "yritän parhaani, katsotaan mihin se riittää"-periaatteella, eli paketteja saattaa hukkua eikä saapumisjärjestystä taata - UDP does not guarantee delivery of packets nor the order of arrival of packets.

d.UDP:n tarkastussummaa laskettaessa laskuun otetaan mukaan myös osa IP-otsakkeesta - In addition to UDP header and data, the UDP checksum is computed from parts of the IP header

e.UDP:n tärkeimpiä käyttökohteita ovat reaaliaikaiset multimediasovellukset - Realtime multimedia is one of the most essential applications for UDP

f.UDP ei muodosta yhteyksiä, eli lähettäjä ja vastaanottaja eivät tee kättelyä ennen datan lähettämistä - UDP is a connectionless protocol; therefore, it does not require handshaking before transmitting the data

g.UDP-otsikko on 8 bittiä pitkä - The size of a UDP header is 8 bits


<br>
<br>

**Q3. TCP**

Mikä tai mitkä seuraavista EIVÄT pidä paikkaansa TCP-protokollaa ajatellen?

Which of the following TCP related statements are FALSE?

Valitse yksi tai useampi:

a.TCP:ssä on toteutettu vuonhallinta, eli lähettäjä ei voi kuormittaa vastaanottajaa liikaa - TCP implements flow control; therefore, the sender cannot overwhelm the receiver

b.TCP-protokolla ei takaa pakettien saapumisjärjestystä - TCP does not guarantee that packets are delivered in the same order they were sent

c.TCP-protokolla tukee vain yksi-yhteen-kommunikaatiota (yksi lähettäjä, yksi vastaanottaja), toisin kuin UDP, jolla on enemmän vaihtoehtoja - TCP supports only one-to-one communication, unlike UDP, which is more versatile

d.TCP:n ansiosta sovellustason protokollan ei tarvitse huolehtia mm. virheenkorjauksesta yleisesti ottaen tai kadonneiden pakettien huomaamisesta - Thanks to TCP, application layer protocols do not have to correct for errors that are caused by the transmission in most cases or handle packet loss

e.Kolme peräkkäistä ACK-viestiä samalla sekvenssinumerolla indikoi sitä, että sekvenssinumeroa seuraava segmentti on tippunut matkalla - Three sequential ACK messages with the same sequence number indicate that the segment with the next sequence number was lost

f.TCP toteuttaa ruuhkanhallintaa protokollassa - TCP implements congestion control

g.TCP-yhteyden määrittää nelikko (lähettäjän IP-osoite, lähettäjän TCP-portti, vastaanottajan IP-osoite, vastaanottajan TCP-portti) - TCP connection is uniquely defined by the source and destination IP addresses, and by the source and destination TCP ports

h.Loogisesti ajatellen TCP lähettää dataa tavuvirtana, ei yksittäisinä paketteina (vaikka tavuvirta on tietysti pilkottu paketteihin kun ne liikkuvat verkossa) - Logically, TCP transmits data as data stream, not as packets (of course, the stream is segmented into packets)

i.TCP-yhteys on full-duplex, eli data voi liikkua molempiin suuntiin - TCP connection is full-duplex (i.e., data can flow in both directions)

j.TCP-protokollan alussa suoritetaan kättely, jolla yhteys muodostetaan - Handshaking is performed when establishing TCP connection

k.Ruuhkanhallinnan ansiosta TCP voi aloittaa lähettämisen täydellä nopeudella kättelyn jälkeen - Because of congestion control, TCP can begin transmitting at maximum transfer rate after handshaking


<br>
<br>

**Q4. TCP Slow Start**

TCP-yhteyden edestakainen etenemisviive (RTT) on 10ms, ja yhteydessä ei ole ruuhkaa. Vastaanottoikkuna (receive window) on 24 kilotavua, ja segmentin maksimikoko (MSS) on 2 kilotavua. Kun TCP-yhteys on jo muodostettu ja lähettäjän ruuhkaikkuna (congestion window) on 1MSS,  kauanko kestäisi TCP:n hitaalla aloituksella (slow start), ennen kuin ensimmäinen täysi ikkuna voidaan lähettää, jos protokolla ei siirtyisi lainkaan ruuhkan välttämistilaan (congestion avoidance)? 

Anna vastauksesi millisekunteina. Voit halutessasi myös tutkia, miten ruuhkan välttämismekanismi (congestion avoidance) muuttaisi vastausta. Molemmat vastaukset hyväksytään.


Round-trip delay time of the TCP connection is 10 ms, and the connection is not affected by congestion. The receive window size is 24 kB and the maximum segment size is 2 kB. Assuming the TCP connection has already been established, and the senders congestion window is 1MSS, how long does it take with the TCP slow start until the first full window can be sent, if the protocol wouldn't move to the congestion avoidance phase?

Give your answer as milliseconds. You can also study, how the congestion avoidance phase would change the answer. Both answers are valid.

Vastaus:

<br>
<br>

**Q5. TCP ruuhkanhallinta (congestion control)**

Oletataan, että TCP:n ruuhkaikkunan koko on asetettu 18kB:iin, ja paketin aikalaskuri tulee täyteen (timeout). Kuinka suuri ruuhkaikkuna on, jos seuraavat neljä lähetettyä segmenttiä menevät onnistuneesti perille (eli niistä on saatu ACK-viesti)? Oleta, että MSS on 1kB, ja että kuittaukset tulevat samassa järjestyksessä kuin paketit on lähetetty.

Anna vastauksesi kilotavuina


TCP congestion window size is set to 18 kB. Retransmission timer times out because timeout is experienced. What is the size of the congestion window after four subsequent segments are received successfully (i.e. ACK has been received)? The maximum segment size (MSS) is 1 kB, and assume that the ACK's arrive in the same order as segments have been sent.

Give your answer in kB

Vastaus:

<br>
<Br>
  
**Q6. Maksiminopeus TCP-skenaariossa**

Mikä on suurin mahdollinen nopeus (megabitteinä sekunnissa), jolla lähettäjä voi lähettää 1300 tavun TCP-kuormia (+ otsikot) ilman, että TCP-sekvenssinumerot pyörähtävät ympäri, kun segmentin pisin elinikä on 120s? Ota huomioon TCP, IP ja Ethernet-otsikoiden viemä tila, ja oleta, että Ethernet-kehyksiä voidaan lähettää jatkuvasti.

Pyöristä vastauksesi ylöspäin, ja esitä vastauksesi ilman desimaaleja megabitteinä sekunnissa.


What is the maximum possible transmission rate (Mbps) that one can use to send 1300 byte TCP payloads (+ headers), without that the TCP sequence number wraps around when the maximum segment lifetime is 120 seconds?

Take into account space taken by TCP, IP and Ethernet headers, and assume that Ethernet frames can be send continuously.

Round up your answer, and express it as Mbps without decimals.

Vastaus:

<br>
<br>

**Q7. TCP:n vastaanottonopeusskenaario**

Päätelaite saa dataa palvelimelta TCP-segmentteinä, joissa on kussakin hyötykuormaa 1460 tavua. Jos TCP kuittaa joka toisen segmentin, mikä on minimipuhurointikaista (minimum uplink bandwidth), joka tarvitaan, jotta imurointisuuntaan saadaan lähetettyä hyötykuormaa 1Mbps? Jätetään mahdolliset verkkokerroksen alapuoliset lisäbitit huomiotta, ja ettei TCP:llä ja IP:llä käytetä mitään ylimääräisiä otsikoita.

(Bonustehtävä: käytä sanaa "puhuroida" keskustelussa ystäviesi kanssa)

Pyöristä vastauksesi ylöspäin ja anna vastauksesi yhden desimaalin tarkkuudella kilobitteinä per sekunti. Käytä pistettä desimaalierottimena.


Client receives data from the server as TCP segments; each segment has payload of 1460 bytes. If TCP acknowledges every other segment, what is the minimum uplink bandwidth required to download payload data at 1 Mbps from the server?

Ignore overhead caused by layers below L3 (network layer). Options are not used with TCP and IP.

Vastaus: 

<br>
<br>
  
  
**Q8. Siirtoaikalaskuja**

Asiakaspäätelaite pyytää ja sille toimitetaan palvelimelta TCP:llä objekti, jonka koko on 100kB. Objekti välitetään linkiltä, jonka lähetysnopeus on 10Mbps kumpaankin suuntaan ja jonka MSS on 536 tavua ja RTT on 100ms. Olettaen, ettei lähetysikkuna aiheuta rajoituksia palvelimen lähettämiseen, mikä on lyhin mahdollinen aika, joka kestää pyynnön lähettämisestä siihen, että objekti on perillä? TCP ja IP eivät käytä mitään optioita, ja voit olettaa, että kättelyyn liittyvät viestit sisältävät vain pakolliset otsikot.

Älä huomioi verkkokerroksen alapuolisia otsikoita, ja oletetaan, ettei verkkokerroksen alapuolelta aiheudu mitään ylimääräisiä viiveitä. Lisäksi: ruuhkaa ei ole, paketteja ei tipu, ja TCP slow start ei ole käytössä, eli TCP voi lähettää täyttä vauhtia heti yhteyden muodostamisen jälkeen. 

Anna vastauksesi millisekunteina pyöristäen normaalisti (alas/ylös) ilman desimaaleja.


A client sends an request to the server using TCP and receives a data object, whose size is 100 kB. The link transmission rate is 10 Mbps bidirectionally.  The MSS is 536 bytes and RTT is 100 ms. Assuming that TCP window size does not limit the transmission rate, what is the minimum time required from sending the request to until the the data object is received? Options are not used with TCP and IP.

Ignore header overhead and other latencies caused by layers below L3 (network layer). There is no congestion, packets are not dropped and TCP slow start is not in use, i.e. TCP can send at full speed right after connection has been established. Express your answer in milliseconds without decimals rounding to the nearest.

Vastaus:


  
