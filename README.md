README
-----------------------
ray optics python project.
Author: Oddvar K. Leiros
------------------------------
About:
Dette prosjektet skal lage en enkel simulasjon av str�ler, alts� ray optics. Dette skal bruke geometri og fysikk formeler til � kunne vise hvordan lys samhandler med forskjellige objekter med forskjellig permativitet og form.
-------------------------------
How to run:

Dette prosjektet bruker pakker som numpy, sympy og matplotlib, s� disse m� v�re installert.

For at man skal kunne kj�re koden m� man gj�re dette via "rays_delt_opp.py" der man kj�rer denne filen. 
Her vil man f� opp plot som er gitt fra de parameterene man har satt inn i de forskjellige objektene som er lagt inn her. 

Her vil....
*ray.Ray(x0, y0, unit_vec) angi en lys str�le som p�virkes av objekter man lager. Her m� man legge til en enhetsvektor som angir retningen . 
M�ten denne enhetsvektoren er definert kan v�re p� hvilken som helst m�te, men m� v�re et numpyarray. 
Eks:  np.array([np.cos(angle), np.sin(angle)]) der angle er vinkelen til enhetsvektoren i radianer.

*lines.Line(x0, y0, x1, y1, n, color) gi et linje objekt med et start of et sluttpunkt. n angir permativiteten til objektet.

*lines.Wall(x0,y0,x1,y1, thickness, n) lager et vegg objekt som bruker lines. Er ment som en forenkling av istedenefor � lage 4 sepparerte Line objekter. Den er derimot un�dig siden man kan gj�re det samme med sepparerte Line objekter, der dette gir deg flere valg.

*circle.Circle(h,k, n, radius) angi et sirkelobjekt som p�virker rays. Dette bruker ikke total indre refleksjon men angir en refleksjon og refraksjon i det det treffer objektet. Har funket tidligere, men har sluttet � funke etter man har gjort endringer i andre deler av koden. h,k er center av sirkelen.

-----------------------------------
