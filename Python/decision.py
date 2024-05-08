def decision(python, numpy, pandas, matplotlib, abscence, niveau):
    moyenne_python = python * 3
    moyenne_numpy = numpy * 4
    moyenne_pandas = pandas * 7
    moyenne_matplotlib = matplotlib * 5
    moyenne_sans_absence = (moyenne_matplotlib + moyenne_numpy + moyenne_pandas + moyenne_python) / 19
    if(abscence >= 0):
        moyenne_sans_absence -=(0.05 * abscence)
    if(moyenne_sans_absence >= 17 and niveau == 5):
        print(f" Vous avez réussi la formation avec la moyenne {round(moyenne_sans_absence, 2)} et un niveau {niveau}")
    elif((moyenne_sans_absence < 17 and moyenne_sans_absence >= 15) and niveau == 4) :
        print(f" Vous avez réussi la formation avec la moyenne {round(moyenne_sans_absence, 2)} et un niveau {niveau}")
    elif((moyenne_sans_absence < 15 and moyenne_sans_absence >= 14) and niveau == 3) :
        print(f" Vous avez réussi la formation avec la moyenne {round(moyenne_sans_absence, 2)} et un niveau {niveau}")
    elif((moyenne_sans_absence < 14 and moyenne_sans_absence >= 13.5) and niveau == 2) :
        print(f" Vous avez réussi la formation avec la moyenne {round(moyenne_sans_absence, 2)} et un niveau {niveau}")
    elif((moyenne_sans_absence < 13.5 and moyenne_sans_absence >= 12) and niveau == 1) :
        print(f" Vous avez réussi la formation avec la moyenne {round(moyenne_sans_absence, 2)} et un niveau {niveau}")
    else:
        print(f"Vous avez échoué à l'examen avec {round(moyenne_sans_absence, 2)} et un niveau {niveau}")

