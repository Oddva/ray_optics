README
-----------------------
Geometrisk optikk python prosjekt.
Author: Oddvar K. Leiros
------------------------------
About:
I dette prosjektet er en løser som simulerer situasjoner i geometrisk optikk. Denne er laget slik at brukeren lette kan gjennomføre forskjellige forsøk som kan gjøre utregninger og visuallisere forskjellige fenomen
-------------------------------
How to run:

Dette prosjektet bruker pakker som numpy, sympy og matplotlib, så disse må være installert.

For at man skal kunne kjøre koden må man gjøre dette via "run_n_edit.py" der brukeren lager objekter og stråler for å simulere hva enn brukeren ønsker. Det skal være en eksempel kode allerede i "run_n_edit.py"
Hvis en ønsker å legge til flere objekter eller stråler kan dette gjøres. Det er ingen begrensninger på hvor mange objekter som kan legges til. Av den grunn vær varsom. 
En enkelt Ray-object kan lage 200 ray_lines. Alle disse plotten havner i matplotlib, som kan bruke litt tid på å lage plots ved store mengde stråler.\n

Hvis brukeren gjør alt ting riktig så vil den få opp et plot gitt fra de parameterene man har satt inn i de forskjellige objektene som er lagt inn her. 
Dette plottet trenger nødvendigvis ikke å være helt korrekt der plots kan være helt feil. Derfor må brukeren være kritisk til plotten den får, siden bugs kan være grunnen og ikke fysikken i det tilfellet er funky.

Kjente bugs/features
--------------------------------

Pga måten koden itererer gjennom objektene vil den prioritere skjæringspunkt med objekter som er først i listen av objekter. \n
Noen ganger vil vinkler strålene har være annerledes enn det de bør være uten god grunn.\n
Koden kan havne i evige loops ved uvanlige parametere for stråler eller objekter. Her bør objekt-typene bare være "transparent", "mirror" eller "black".\n
Hvis brukeren setter brytningsindeksen(refractive_index), n, til et medie til å bli under 1, kan en observere tilfeller med total indre refraksjon.



--------------------------------------------
Om objektene i programmet:\n

ray.Ray(x0, y0, unit_vec) angi en lys stråle som påvirkes av objekter man lager. Her må man legge til en enhetsvektor som angir retningen . 
Måten denne enhetsvektoren er definert kan være på hvilken som helst måte, men må være et numpyarray. 
Eks:  np.array([np.cos(angle), np.sin(angle)]) der angle er vinkelen til enhetsvektoren i radianer.\n

*lines.Line(x0, y0, x1, y1, n, color) gi et linje objekt med et start of et sluttpunkt. n angir permativiteten til objektet.\n

*lines.Wall(x0,y0,x1,y1, thickness, n) lager et vegg objekt som bruker lines. Er ment som en forenkling av istedenefor å lage 4 sepparerte Line objekter. Den er derimot unødig siden man kan gjøre det samme med sepparerte Line objekter, der dette gir deg flere valg.\n

*circle.Circle(h,k, n, radius) angi et sirkelobjekt som påvirker rays. Dette bruker ikke total indre refleksjon men angir en refleksjon og refraksjon i det det treffer objektet. Har funket tidligere, men har sluttet å funke etter man har gjort endringer i andre deler av koden. h,k er center av sirkelen.\n

-----------------------------------
