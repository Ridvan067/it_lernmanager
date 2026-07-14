anzahl=(int(input("Wie viele Aufgaben möchtest du auswerten ?\n")))

nicht_bestanden=0
bestanden=0
stand=0
for punkte in range(anzahl):
    gg=int(input("Wie viele Punkte hast du erreicht?\n"))

    if gg >= 50:
        bestanden=(bestanden + 1)
    else:
        nicht_bestanden=(nicht_bestanden + 1)


    if gg >= 90:
        print("Sehr Gut")
    elif gg >= 89:
        print("Gut")
    elif gg >= 50:
        print("Bestanden")
    else:
        print("Nicht Bestanden")

    stand=int(stand+gg)



durchschnitt=(stand/anzahl)
#print(stand)

if durchschnitt >= 90 and durchschnitt<= 100:
    ergebnis=" Sehr Gut "
elif durchschnitt >= 75 and durchschnitt <= 89:
    ergebnis= "Gut"
elif durchschnitt >= 50 and durchschnitt <= 74:
    ergebnis="Bestanden"
else:
    ergebnis="Mehr Üben"





print("--- IT-Lernmanager ---")
print("Name: Ridvan ")
print("Anzahl Aufgaben: " , anzahl)
print("Gesamtpunkte: " , stand)
print("Durchscnitt: " , durchschnitt )
print("Bestandene Aufgaben: " , bestanden)
print("Nicht bestandene Aufgaben: " , nicht_bestanden)
print("Gesamtergebnis: " , ergebnis)