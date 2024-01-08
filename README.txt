README
-----------------------
ray optics python project.
Author: Oddvar K. Leiros
------------------------------
About:
Dette prosjektet skal lage en enkel simulasjon av stråler, altså ray optics. Dette skal bruke geometri og fysikk formeler til å kunne vise hvordan lys samhandler med forskjellige objekter med forskjellig permativitet og form.
-------------------------------
How to run:

Dette prosjektet bruker pakker som numpy, sympy og matplotlib, så disse må være installert.

For at man skal kunne kjøre koden må man gjøre dette via "rays_delt_opp.py" der man kjører denne filen. 
Her vil man få opp plot som er gitt fra de parameterene man har satt inn i de forskjellige objektene som er lagt inn her. 

Her vil....
*ray.Ray(x0, y0, unit_vec) angi en lys stråle som påvirkes av objekter man lager. Her må man legge til en enhetsvektor som angir retningen . 
Måten denne enhetsvektoren er definert kan være på hvilken som helst måte, men må være et numpyarray. 
Eks:  np.array([np.cos(angle), np.sin(angle)]) der angle er vinkelen til enhetsvektoren i radianer.

*lines.Line(x0, y0, x1, y1, n, color) gi et linje objekt med et start of et sluttpunkt. n angir permativiteten til objektet.

*lines.Wall(x0,y0,x1,y1, thickness, n) lager et vegg objekt som bruker lines. Er ment som en forenkling av istedenefor å lage 4 sepparerte Line objekter. Den er derimot unødig siden man kan gjøre det samme med sepparerte Line objekter, der dette gir deg flere valg.

*circle.Circle(h,k, n, radius) angi et sirkelobjekt som påvirker rays. Dette bruker ikke total indre refleksjon men angir en refleksjon og refraksjon i det det treffer objektet. Har funket tidligere, men har sluttet å funke etter man har gjort endringer i andre deler av koden. h,k er center av sirkelen.

-----------------------------------