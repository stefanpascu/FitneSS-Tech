# FitneSS-Tech

<!-- <br> -->

## Scopul aplicației: 

  Aplicatia aleasa este “creierul” unei bratari smart care ajuta purtatorul sa isi monitorizeze activitatea fizica si sa isi usureze un numar limitat actiuni zilnice simple. 
  
<br>

## Obiectivele aplicației: 

• Monitorizare parametrii corp 

• Monitorizarea activitatii fizice 

• Monitorizarea somnului si a calitatii acestuia 

• Posibilitatea de a schimba modul in care arata interfata 

<br>

## Grupul țintă: 

  Grupul tinta nu este unul anume. Utilizatorii sunt motivati sa foloseasca bratara fitness pentru a afla macar putin despre nivelul de sanatate pe care il au si pentru a isi usura anumite actiuni. Un exemplu este verificarea orei sau a temperaturii mediului intr-un mod mai eficient. 

  In acest context, un atlet isi poate masura evolutia efortului depus pentru a practica un anumit antrenament, o persoana in varsta poate verifica cu usurinta daca pulsul nu este in reperele normale. 

<br>

## Resurse si Mentiuni

• <a href="https://www.bing.com/search?q=flask&cvid=23b41ea58cf7459892ee57b1aa3fefbb&aqs=edge.0.0l8j69i61.752j0j1&pglt=43&FORM=ANNAB1&PC=U531"> Flask </a> este un framework web, un modul Python care va permite sa dezvoltati aplicatii web cu usurinta. La baza, este mic si usor de extins: este un microcadru care nu include un ORM (Object Relational Manager) sau astfel de caracteristici.

• <a href="https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/"> HeartPY </a> este un toolkit conceput pentru a gestiona datele PPG (noisy) colectate fie cu PPG, fie cu senzori de cameră.
Mai mult, as dori sa mentionez urmatoarele articole: <a href="https://www.researchgate.net/publication/325967542_Heart_Rate_Analysis_for_Human_Factors_Development_and_Validation_of_an_Open_Source_Toolkit_for_Noisy_Naturalistic_Heart_Rate_Data"> Heart Rate Analysis for Human Factors </a> si <a href="https://www.researchgate.net/publication/328654252_Analysing_Noisy_Driver_Physiology_Real-Time_Using_Off-the-Shelf_Sensors_Heart_Rate_Analysis_Software_from_the_Taking_the_Fast_Lane_Project?channel=doi&linkId=5bdab2c84585150b2b959d13&showFulltext=true"> Analysing Noisy Driver Physiology Real-Time Using Off-the-Shelf Sensors </a>.

• <a href="https://docs.python.org/3/library/datetime.html"> datetime.py </a> este un modul care furnizează clase pentru manipularea datelor și orelor

• <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html"> matplotlib.pyplot </a> oferă o modalitate implicită, asemănătoare MATLAB, de a reprezenta un grafic. De asemenea, deschide figurile pe ecran și acționează ca manager GUI pentru figuri.

• <a href="https://sqlite.org/index.html"> SQLite </a> este o bibliotecă în limbaj C care implementează un motor de bază de date SQL mic, rapid, autonom, de înaltă fiabilitate, cu funcții complete.

<br>

## Cerințe preliminare

Ar trebui să aveți instalate python3 și pip3.

De asemenea, ar trebui să aveți un broker MQTT instalat.

<br>

## Instalare Mosquitto MQTT Broker
1. Instalați <a href="https://mosquitto.org/download/">utilitatile</a> Mosquitto pentru sistemul dvs. de operare.

2. Creați un fișier de configurare numit mosquitto.conf pentru broker cu următorul conținut.

`persistence false` <br>
`log_dest stdout` <br>
`allow_anonymous true` <br>
`connection_messages true` 

3. Porniți containerul Docker.

`docker run --name mosquitto -p 1881:1881 -v pwd/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

4. SPorniți containerul Docker folosind această comandă.
`docker run --name mosquitto -p 1881:1881 -v pwd/mosquitto.conf:/mosquitto/config/mosquitto.conf -v pwd/password:/etc/mosquitto/passwd eclipse-mosquitto`

5. Verificați dacă brokerul rulează publicând un mesaj către acesta.

`mosquitto_pub -h localhost -p 1881 -t my-mqtt-topic -m "sample-msg-1"`

6. Rulati: <br>

`docker-compose up -d`

## Instalarea

1. cd in acest proiect.

2. Instalați venv dacă nu este deja instalat: <br>
`pip install virtualenv`

3. Creați un enviornment: <br>
`python3 -m venv ./`

>Windows: `python -m venv venv`

4. Activati enviornment-ul:

macOS/Linux: <br>
`source venv/bin/activate`

Windows: <br>
`.venv\Scripts\activate.bat`

5. Instalati librariile: <br>
`pip install -r requirements.txt`

Pentru instalarea librariei HeartPY : <br>
`python -m pip install heartpy`

6. Setați enviornment value pentru dezvoltare: <br>
`export FLASK_ENV=development`

CMD: <br>
`set FLASK_ENV=development`

PowerShell: <br>
`$env:FLASK_ENV = "development"`

7. Initializati baza de date: <br>
`flask init-db`

8. Rulati: <br>
`flask run`

>In cazul in care pasii 7. si 8. nu ruleaza deoarece "flask" nu este recunoscut ("The term 'flask' is not recognized"), puteti folosi comenzile `python -m flask init-db` si `python -m flask run`

<br>
