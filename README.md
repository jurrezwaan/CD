[![Run tests](https://github.com/jurrezwaan/CD/actions/workflows/run_deploy.yml/badge.svg)](https://github.com/jurrezwaan/CD/actions/workflows/run_deploy.yml)

# ***REPORT***

## ***Drie elementen van mijn oplossing***
---
### **Github Actions** 
is een manier om processen te automatiseren. In dit geval om automatisch de applicatie te testen en daarna in te loggen op de vps en daar een `git pull` uit te voeren door middel van iets wat lijkt op een java script.

---

### **SSH** 
staat voor `Secure Socket Shell` of `Secure Shell`. Dit is een netwerk protocol dat het mogelijk maakt om een veilige verbinding met een andere computer te maken. Dit gaat dan via een `Terminal` zoals bijvoorbeeld `Git Bash`. Het verbinding maken gaat via zogenaamde `SSH Key Pairs` waarvan het ene deel altijd bij jezelf blijft en het andere deel gedeeld kan worden. Zodat bij inloggen wordt gekeken of de keys bij elkaar horen

---

### **Digital Ocean** 
is een leveraar van cloudinfrastructuur. Je huurt daar een `droplet`. Dat is een stukje schijf ruimte op een server met een `vm` die op `Ubuntu` draait. Vanuit daar wordt je applicatie gehost naar een ip adres wat overal te bereiken is.

---

## ***Drie problemen***

---

### ***Inloggen via SSH op de droplet***
Voordat alles via `Github Actions` zou gaan wilde ik eerst zelf proberen of ik een 'git clone' en 'git pull' kon uitvoeren op de droplet. Dit lukte eerst niet omdat de tutorial die ik volgde de `config file` als volgt aanmaakte: 
``` 
sudo cat >~/.ssh/config <<EOL
Host my_project
Hostname github.com
User git
IdentityFile ~/.ssh/id_rsa
EOL
```
Verder zei de tutorial dat ik dan op deze manier de `git clone` moest uitvoeren:
```
sudo git clone my_project:<user>/<repo>.git
```
Dit werkte niet doordat er voor de `IdentityFile` regel een spatie moet kwam ik achter. De syntax voor de `git clone` werkte ook niet. Ik heb het als volgt opgelost. Eerst heb ik mijn config file aangepast:
```
Host github.com
 IdentityFile ~/.ssh/id_rsa
```
En het `git clone` command zo uitgevoerd:
```
sudo git clone git@github.com:jurrezwaan/CD.git
```

---

### ***Gunicorn wil applicatie niet runnen***
---
Doordat er in een eerdere opdracht al een verbinding met `Gunicorn` was gemaakt kreeg ik steeds een foutmelding als ik `systemctl start CD` probeerde. Door in `systemctl status CD` en `journalctl -xe` te kijken kwam ik er achter dat het proces van de eerder gemaakt verbinding nog aan het draaien was. Door `ps -A` te gebruiken kon ik zien wat het `PID` was van de `gunicorn` processen en ze daarna met `kill` stoppen. Daarna heb ik de vps gereboot en kon ik de applicatie gewoon starten.

---
### ***Hoe kan ik een .sh script remote runnen***
---
Dit is niet echt een oplossing maar eerder een omweg. Ik kreeg het niet voor elkaar om het script te runnen via `Github Actions` omdat het dan werd uitgevoerd op de `vm` lokaal ipv van op de `vps`. Mijn oplossing was dat ik het `.sh` bestand maar gewoon naar de `vps heb gekopieerd` in de `/home` map waar ook de map van de repo stond. Dit werkt prima maar ik denk dat er een mooiere oplossing moet zijn.

---

### ***Final Thoughts***
Het voelde erg Matrix om in te loggen op een server ergens in Frankfurt dat vond ik erg gaaf. Verder is het bestandssysteem van Linux erg raar na 25+ jaar windows. 'Waar is mijn c schijf gebleven' is een van de quotes die ik gebezigd heb. Ik had eerst nog een stomme fout gemaakt door mijn project folder in de root te zetten. Blijkbaar heeft Gunicorn daar geen toegang toe dus lukte het verbinding maken niet. Na de hele handel naar /home/ te hebben gezet werkte alles perfect. 

ps
De Flask site is lachwekkend simpel maar daar ging het ook niet echt om.