**DNS-kysymys 1**


Lataat selaimellasi verkkosivua. Palvelimen IP-osoitteen selvittämiseksi tarvitaan kolme DNS-hakua DNS-palvelimille 0, 1 ja 2. 

DNS-palvelin 0: RTT = 5ms (sisältäen DNS-kutsujen ja vastausten lähetysajat)
DNS-palvelin 1: RTT = 10ms  (sisältäen DNS-kutsujen ja vastausten lähetysajat)
DNS-palvelin 2: RTT = 20ms (sisältäen DNS-kutsujen ja vastausten lähetysajat)
Verkkopalvelin: RTT =  8ms

Oletetaan, että palvelimelta haetaan tasan yksi HTML-sivu, joka ei viittaa mihinkään muihin objekteihin. Kauanko kestää ensimmäisen DNS-kutsun lähettämisestä siihen, että selaimesi on ladannut HTML-tiedoston? Älä huomioi lähetysaikoja (DNS-kyselyjen, vastausten tai HTML-sivun palvelimelta lähettämiseen kuluvaa aikaa).  Oleta, että DNS käyttää UDP:tä. Anna vastauksesi millisekunteina ilman desimaaleja. 

------

You are downloading a web page using a browser. To resolve the web server domain name to IP address, three DNS queries are required; one to each server: 0, 1 and 2.

```
DNS server 0: RTT = 5 ms (including DNS query and response transmission delays)
DNS server 1: RTT = 10 ms (including DNS query and response transmission delays)
DNS server 2: RTT = 20 ms (including DNS query and response transmission delays)
```
Web server: RTT = 8 ms

Assuming that only one web page is downloaded, that does not have references to external objects. How much time it takes from resolving IP address to until your browser has downloaded the web page? Ignore all transmission delays (DNS request and response transmission times and HTML page transmission time)! Assume that DNS uses UDP. Express your answer in milliseconds without decimals.


Vastaus: 51 (5+ 10 + 20 + 2x8)

**Kysymys 2**

Lataat selaimellasi verkkosivua, jonka IP-osoite on jo tiedossa. Verkkosivu koostuu häviävän pienestä  HTML-tiedostosta, joka viittaa kolmeen muuhun samalla palvelimella sijaitsevaan häviävän pieneen objektiin. Voit siis olettaa, että ne kaikki mahtuvat yhteen TCP-segmenttiin, ja että niiden lähetysaika on 0ms. Jätä huomiotta myöskin pyyntöjen ja kättelyiden lähetysviiveet.

Verkkopalvelimen RTT =  10ms

Kauanko kestää hakea koko sivu kun käytetään ei-persistenttiä HTTP:tä ilman rinnakkaisia TCP-yhteyksiä?

Anna vastauksesi millisekunteina ilman desimaaleja.

------

You are downloading a website from a web server. RTT is 10ms and the server IP address is already known. The website consists of a negligibly small HTML file that refers to three other objects, each also negligibly small - each fits into one TCP segment. Also you can ignore transmission times of all requests (i.e. you can ignore all transmission delays). How long does it take to download all four files when using non-persistent HTTP without parallel TCP connections? Give your answer is milliseconds without decimals.

Vastaus: 80 (2 x 10 + 3 x 2 x 10)


**Kysymys 3**

HTTP-kysymys 2

Lataat selaimellasi verkkosivua, jonka IP-osoite on jo tiedossa. Verkkosivu koostuu häviävän pienestä  HTML-tiedostosta, joka viittaa kolmeen muuhun samalla palvelimella sijaitsevaan häviävän pieneen objektiin. Voit siis olettaa, että ne kaikki mahtuvat yhteen TCP-segmenttiin, ja että niiden lähetysaika on 0ms. Jätä huomiotta myöskin pyyntöjen ja kättelyiden lähetysviiveet.

Verkkopalvelimen RTT =  10ms

Kauanko kestää hakea koko sivu kun käytetään ei-persistenttiä HTTP:tä rinnakkaisilla TCP-yhteyksillä?

Anna vastauksesi millisekunteina ilman desimaaleja.

------

You are downloading a website from a web server. RTT is 10ms and the server IP address is already known. The website consists of a negligibly small HTML file that refers to three other objects, each also negligibly small - each fits into one TCP segment. Also you can ignore transmission times of all requests (i.e. you can ignore all transmission delays). How long does it take to download all four files when using non-persistent HTTP with parallel TCP connections? Give your answer is milliseconds without decimals.


Vastaus: 40  (2 x 10 + 2 * 10) 


**Kysymys 4**

HTTP-kysymys 3

Lataat selaimellasi verkkosivua, jonka IP-osoite on jo tiedossa. Verkkosivu koostuu häviävän pienestä  HTML-tiedostosta, joka viittaa kolmeen muuhun samalla palvelimella sijaitsevaan häviävän pieneen objektiin. Voit siis olettaa, että ne kaikki mahtuvat yhteen TCP-segmenttiin, ja että niiden lähetysaika on 0ms. Jätä huomiotta myöskin pyyntöjen ja kättelyiden lähetysviiveet.

Verkkopalvelimen RTT =  10ms

Kauanko kestää hakea koko sivu kun käytetään persistenttiä HTTP:tä rinnakkaisilla TCP-yhteyksillä?

Anna vastauksesi millisekunteina ilman desimaaleja.

------

You are downloading a website from a web server. RTT is 10ms and the server IP address is already known. The website consists of a negligibly small HTML file that refers to three other objects, each also negligibly small - each fits into one TCP segment. Also you can ignore transmission times of all requests (i.e. you can ignore all transmission delays). How long does it take to download all four files when using persistent HTTP with parallel TCP connections? Give your answer is milliseconds without decimals.

Vastaus: 30 ( 2 x 10 + 10 ) 


**Kysymys 5**

HTTP-kysymys 4

Haet palvelimelta, jonka IP-osoite on tiedossa, verkkosivua, joka koostuu 10kB HTML-tiedostosta sekä 10 JPEG-kuvasta, joihin HTML-tiedosto viittaa. Jokainen kuva on kooltaan 50kB. Palvelimen kaista selaimen suuntaan on 10Mbps ja RTT palvelimelle on 100ms.

Mikä on kokonaisaika, kun käytetään ei-persistenttiä HTTP:tä ilman rinnakkaisia TCP-yhteyksiä?

Oletukset:

Oleta, että TCP voi lähettää täydellä nopeudella heti yhteyden luomisen jälkeen (ei ruuhkanhallintaa/slow startia)
Ei ruuhkaa
Ei prosessointiaikoja
Ei mitään verkkokerroksen alapuolelta aiheutuvia ylimääräisiä viiveitä
Palvelimelle lähetettävien HTTP-pyyntöjen lähetysaika on häviävän pieni (ei tarvitse huomioida)
Älä huomioi minkään kerroksen pakettiotsikoiden vaatimien bittien aiheuttamaa lisäviivettä
Anna vastauksesi millisekunteina ilman desimaaleja

You are downloading a website from a server whose IP address is known. The site consists of 10kB HTML file that refers to 10 JPEG images. The size of each image is 50kB. The download link from the server is 10Mbps and RTT is 100ms.

Calculate the total time when using non-persistent HTTP without parallel TCP connections?


Assumptions:
```
Assume, that TCP can send at full speed immediately afdter the connection has been initialised (no congestion control/slow-start)
No congestion
No processing delays
No additional delays from layers below L3 (network)
Transmission delay of HTTP requests sent to the server can be ignored
Ignore additional delays caused by headers on any layer
```

Give your answer is milliseconds without decimals.

Vastaus: 2608 (2 x 100 + 10 x 2 x 100 + 408 for 510kB) 

**Kysymys 6**
HTTP-kysymys 5

Haet palvelimelta, jonka IP-osoite on tiedossa, verkkosivua, joka koostuu 10kB HTML-tiedostosta sekä 10 JPEG-kuvasta, joihin HTML-tiedosto viittaa. Jokainen kuva on kooltaan 50kB. Palvelimen kaista selaimen suuntaan on 10Mbps ja RTT palvelimelle on 100ms.

Mikä on kokonaisaika, kun käytetään persistenttiä HTTP:tä liukuhihnalähetyksellä (pipelining)?

Oletukset:

Oleta, että TCP voi lähettää täydellä nopeudella heti yhteyden luomisen jälkeen (ei ruuhkanhallintaa/slow startia)
Ei ruuhkaa
Ei prosessointiaikoja
Ei mitään verkkokerroksen alapuolelta aiheutuvia ylimääräisiä viiveitä
Palvelimelle lähetettävien HTTP-pyyntöjen lähetysaika on häviävän pieni (ei tarvitse huomioida)
Älä huomioi minkään kerroksen pakettiotsikoiden vaatimien bittien aiheuttamaa lisäviivettä
Anna vastauksesi millisekunteina ilman desimaaleja

------

You are downloading a website from a server whose IP address is known. The site consists of 10kB HTML file that refers to 10 JPEG images. The size of each image is 50kB. The download link from the server is 10Mbps and RTT is 100ms.

Calculate the total time when using persistent HTTP with pipelining?


Assumptions:
```
Assume, that TCP can send at full speed immediately after the connection has been initialised (no congestion control/slow-start)
No congestion
No processing delays
No additional delays from layers below L3 (network)
Transmission delay of HTTP requests sent to the server can be ignored
Ignore additional delays caused by headers on any layer
```
Give your answer is milliseconds without decimals.

Vastaus: 708 (2 x 100 + 1 * 100 + 408)


**Kysymys 7**

Tietoturva - tiivistefunktiot (hashing functions)

Oheisessa kuvassa näkyy sarja operaatioita, jotka suoritetaan Alicen lähettäessä viestin Bob:lle.

![image](https://user-images.githubusercontent.com/25344978/232573252-4214d0a5-99e6-408f-a500-449789fe2ccf.png)

Valitse todet väittämät:

Valitse yksi tai useampi:

a.Kuvan tarkoituksena on esitellä, miten digitaalisella allekirjoituksella varmistetaan lähettäjän identiteetti - The diagram illustrates how digital signature can be used to verify the identity of the sender

b.Tiivistefunktio H kannattaa kehittää itse erikseen jokaiselle palvelulle. Käyttämällä tunnettuja funktiota järjestelmä on alttiimpi hyökkäyksille - The developer should design their own hash function H for their service. Using well-known and audited hash functions is a bad practice; it makes the system more insecure.

c.Epäsymmetrisen (julkinen ja salainen avain) salauksen hienous piilee siinä, että laskennallisesta monimutkaisuudesta johtuen salaista avainta ei voida koskaan ratkaista julkisen avaimen ja jonkin salatun viestin avulla - In asymmetric encryption, deriving private key from public key and ciphertext(s) has so high computational complexity that this is impossible.

d.Vaikka viesti m näkyykin julkisesti, ainoastaan Bob voi todeta, että onko Alicen allekirjoitus pätevä - Even though, the message m is sent as plaintext, only Bob can verify that the message was signed by Alice

e.Tiivistefunktiot (hash-funktiot) takaavat, että ei ole kahta erilaista viestiä m ja m', joiden tiiviste olisi sama (eli kaikilla mahdollisilla viesteillä m ja m' pitää paikkansa, että H(m) != H(m')) - All hash functions have negligible probability of collision (H(m') = H(m)) for all possible messages m and m'


f.Jotta Alicen digitaaliseen allekirjoitukseen voidaan luottaa, tiiviste- eli hashfunktio H on oltava sellainen, että on liki mahdotonta löytää järkevä m', jolla H(m') = H(m) - Probability of hash collision (H(m') = H(m)) must be negligible, otherwise the digital signature of Alice cannot be trusted

g.Kuvassa käytetään symmetrisen avaimen menetelmää - The diagram illustrates symmetric key method

h.Ainoastaan Alice on voinut allekirjoittaa viestin salaisella avaimellaan - Only Alice can use the private key to sign a message

i.Kukaan muu kuin Bob ei voi lukea viestiä m - Only bob can read the message m

j.Kuvan tarkoituksena on esitellä, miten julkisen avaimen menetelmällä salataan ja toimitetaan viestejä - The diagram illustrates how public key can used to encrypt messages

True

Jotta Alicen digitaaliseen allekirjoitukseen voidaan luottaa, tiiviste- eli hashfunktio H on oltava sellainen, että on liki mahdotonta löytää järkevä m', jolla H(m') = H(m) - Probability of hash collision (H(m') = H(m)) must be negligible, otherwise the digital signature of Alice cannot be trusted

Kuvan tarkoituksena on esitellä, miten digitaalisella allekirjoituksella varmistetaan lähettäjän identiteetti - The diagram illustrates how digital signature can be used to verify the identity of the sender



**Kysymys 8**

Tietoturva - viestien salaus (message encryption)

![image](https://user-images.githubusercontent.com/25344978/232573376-1bebaef4-87b3-4642-a6f6-d464cde0df58.png)

Ylläolevassa kuvassa näytetään prosessi, jolla saavutetaan jotain tietoturvaan liittyen. Valitse todet väittämät:


Valitse yksi tai useampi:

a.Trudy vaihtaa viestin sen ollessa matkalla. Väärentääkseen Alicen lähettämän viestin, hän tarvitsee B:n julkisen avaimen lisäksi sessioavaimen Ks ja A:n julkisen avaimen

b.Trudy kaappaa viestin sen ollessa matkalla. Lukeakseen viestin sisällön, hän tarvitsee A:n salaisen avaimen, sekä B:n julkisen avaimen.

c.Trudy vaihtaa viestin sen ollessa matkalla. Väärentääkseen Alicen lähettämän viestin, hän tarvitsee ainoastaan B:n julkisen avaimen.


d.Trudy kaappaa viestin sen ollessa matkalla. Lukeakseen viestin sisällön ilman varmuutta siitä, että A on lähettänyt viestin, hän tarvitsee ainoastaan B:n julkisen avaimen.

e.Trudy kaappaa viestin sen ollessa matkalla. Lukeakseen viestin sisällön, hän tarvitsee B:n salaisen avaimen.

f.Kaikki kryptografia on turhaa, sillä NSA lukee ja näkee kaiken ja voi purkaa minkä tahansa viestin

g.Mikäli avaimet eivät ole vuotaneet ja käytetyt algoritmit ovat (edelleen) turvallisia, kuvan järjestely takaa viestin luottamuksellisuuden (confidentiality), lähettäjän henkilöllisyyden (authentication) ja viestin muokkaamattomuuden (integrity).

h.Mikäli avaimet eivät ole vuotaneet ja käytetyt algoritmit ovat (edelleen) turvallisia, kuvan järjestely takaa viestin luottamuksellisuuden (confidentiality) ja  lähettäjän henkilöllisyyden (authentication), mutta ei takaa viestin muokkaamattomuutta (integrity).

i.Mikäli avaimet eivät ole vuotaneet ja käytetyt algoritmit ovat (edelleen) turvallisia, kuvan järjestely takaa viestin luottamuksellisuuden (confidentiality) ja viestin muokkaamattomuuden (integrity), mutta ei takaa lähettäjän henkilöllisyyttä (authentication).

j.Mikäli avaimet eivät ole vuotaneet ja käytetyt algoritmit ovat (edelleen) turvallisia, kuvan järjestely takaa viestin viestin muokkaamattomuuden (integrity) ja lähettäjän henkilöllisyyden (authentication), mutta ei takaa viestin luottamuksellisuutta (confidentiality).



True
Trudy kaappaa viestin sen ollessa matkalla. Lukeakseen viestin sisällön, hän tarvitsee B:n salaisen avaimen.

Mikäli avaimet eivät ole vuotaneet ja käytetyt algoritmit ovat (edelleen) turvallisia, kuvan järjestely takaa viestin luottamuksellisuuden (confidentiality), lähettäjän henkilöllisyyden (authentication) ja viestin muokkaamattomuuden (integrity).



