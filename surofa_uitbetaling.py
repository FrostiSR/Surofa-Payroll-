werknemer = []
werkUren = []
aantalMaanden = []
bedragSalaris = []
uurTarieven = []

def main():

    def belastingStandaard():
    #Belasting
        if (bedrag < 500):

            print(naam, "hoeft geen belasting te betalen")

        elif (500 < bedrag < 1000):

            belasting = 0.05 * bedrag
            salaris = bedrag - belasting
            print("Ingehouden bedrag (Belasting) is:", belasting)
            print("Uitbetalingsbedrag (met afgetrokken belasting) van", naam, "is:", salaris)

        elif (bedrag > 1000):

            belasting = 0.1 * bedrag
            salaris = bedrag - belasting
            print("Ingehouden bedrag (Belasting) is:", belasting)
            print("Uitbetalingsbedrag (afgetrokken belasting) van", naam, "is:", salaris)

    def vakantieToelage():

        if (maanden == 12):

            Toelagebedrag = bedrag
            print("Het toelagebedrag van", naam, "is:", Toelagebedrag)

            #Belasting
            if(Toelagebedrag > 1200):
                belasting = 0.1 * Toelagebedrag
                salaris = Toelagebedrag - belasting
                print("Ingehouden toelagebedrag (Belasting) is:", belasting)
                print("Salaris toelage van", naam, "is:", salaris)

        if (maanden == 6):

            Toelagebedrag = bedrag * 0.5
            print("Het toelagebedrag van", naam, "is:", Toelagebedrag)

            #Belasting
            if(Toelagebedrag > 1200):
                belasting = 0.1 * Toelagebedrag
                salaris = Toelagebedrag - belasting
                print("Ingehouden toelagebedrag (Belasting) is:", belasting)
                print("Salaris toelage van", naam, "is:", salaris)

        if (maanden == 3):

            Toelagebedrag = bedrag * 0.25
            print("Het toelagebedrag van", naam, "is:", Toelagebedrag)

            #Belasting
            if(Toelagebedrag > 1200):
                belasting = 0.1 * Toelagebedrag
                salaris = Toelagebedrag - belasting
                print("Ingehouden toelagebedrag (Belasting) is:", belasting)
                print("Salaris toelage van", naam, "is:", salaris)


    print('----- Surofa Uitbetaling -----')
    print('Kies type werknemer: type 1 (fulltime) of type 2 (parttimer)')

    choice = int(input('Kies de type: '))

    # Dit zijn de fulltimers
    if (choice == 1):

        print("Voer de naam van de werknemer in:")

        naam = input()
        werknemer.append(naam)

        print("Vul het aantal werkuren van de werknemer in:")

        uren = float(input())
        werkUren.append(uren)

        print("Vul het tarief in:")

        tarief = float(input())
        uurTarieven.append(tarief)

        if (uren == 40):

            weekbedrag = uren * tarief
            bedrag = (uren * tarief) * 4
            print("Het week bedrag (zonder belasting) is:", weekbedrag)
            print("Het maandelijks bedrag (zonder belasting) is:", bedrag)

            #Belasting
            belastingStandaard()

            print("")
            print("---- Vakantietoelage ----")

            print("Voer in de aantal maanden die werknemer heeft gewerkt: ")

            maanden = int(input())
            aantalMaanden.append(maanden)

            vakantieToelage()


        elif (40 < uren <= 60):
            print("Deze werknemer heeft overwerk uren!")

            weekbedrag = 40 * tarief
            overuren = (uren - 40) * ( 2 * tarief)
            bedrag = ((weekbedrag + overuren) * 4)
            print("Het week bedrag (zonder belasting) is:", weekbedrag)
            print("Het overwerk bedrag (zonder belasting) is:", overuren)
            print("Het maandelijks bedrag (zonder belasting) is:", bedrag)

            #Belasting
            belastingStandaard()

            print("")
            print("---- Vakantietoelage ----")

            print("Voer in de aantal maanden die werknemer heeft gewerkt: ")

            maanden = int(input())
            aantalMaanden.append(maanden)

            vakantieToelage()

        else:
            print("De werknemer wordt niet betaald als hij/ zei minder dan 40 uren werkt en een werknemer kan tot max. 60 uren overwerken!")

    # Dit zijn de parttimers
    if (choice == 2):

        print("Voer de naam van de parttime werknemer in:")

        naam = input()
        werknemer.append(naam)

        print("Vul het aantal werkuren van de parttime werknemer in:")

        uren = float(input())
        werkUren.append(uren)

        print("Vul het tarief in:")

        tarief = float(input())
        uurTarieven.append(tarief)

        if (uren == 40):

            weekbedrag = uren * tarief
            bedrag = (uren * tarief) * 4
            print("Het week bedrag (zonder belasting) is:", weekbedrag)
            print("Het maandelijks bedrag (zonder belasting) is:", bedrag)

            #Belasting
            belastingStandaard()

            maanden = int(input())
            aantalMaanden.append(maanden)

        elif (uren < 40):

            weekbedrag = uren * tarief
            bedrag = (uren * tarief) * 4
            print("Het week bedrag (zonder belasting) is:", weekbedrag)
            print("Het maandelijks bedrag (zonder belasting) is:", bedrag)

            #Belasting
            belastingStandaard()

            maanden = int(input())
            aantalMaanden.append(maanden)

        elif (uren > 40):

            weekbedrag = uren * tarief
            bedrag = (uren * tarief) * 4
            print("Het week bedrag (zonder belasting) is:", weekbedrag)
            print("Het maandelijks bedrag (zonder belasting) is:", bedrag)

            #Belasting
            belastingStandaard()

            maanden = int(input())
            aantalMaanden.append(maanden)

        else:
            print("De parrtime werknemer wordt betaald d.m.v. het basis tarief ongeacht het aantal werkuren!")

    print("")
    restart = input("Wil je verder gaan? ")

    if (restart == "ja" or restart == "Ja"):
        main()
    else:
        exit()

main()
