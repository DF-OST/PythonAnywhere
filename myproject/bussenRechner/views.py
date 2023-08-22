from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
# from .forms import *
from django.shortcuts import redirect
from datetime import date as dt

# Create your views here.
def result(request):

    tatsaechlicheGeschwindigkeit = int(request.POST['tatsaechlicheGeschwindigkeit'])
    erlaubteGeschwindigkeit = int(request.POST['erlaubteGeschwindigkeit'])
    ueberschreitung = tatsaechlicheGeschwindigkeit - erlaubteGeschwindigkeit

    toleranz = checkToleranz(request.POST['messverfahren'], tatsaechlicheGeschwindigkeit)

    ueberschreitungNachToleranz = ueberschreitung - toleranz


    if (request.POST['bereich'] == 'Innerorts'):
        busseVorToleranz = checkInnerorts(ueberschreitung)['busse']
        massnahmeVorToleranz = checkInnerorts(ueberschreitung)['massnahme']
        ueberschreitungsBereichVorToleranz = checkInnerorts(ueberschreitung)['ueberschreitungsBereich']
        busseNachToleranz = checkInnerorts(ueberschreitungNachToleranz)['busse']
        massnahmeNachToleranz = checkInnerorts(ueberschreitungNachToleranz)['massnahme']
        ueberschreitungsBereichNachToleranz = checkInnerorts(ueberschreitungNachToleranz)['ueberschreitungsBereich']

    elif(request.POST['bereich'] == 'Ausserorts'):
        busseVorToleranz = checkAusserorts(ueberschreitung)['busse']
        massnahmeVorToleranz = checkAusserorts(ueberschreitung)['massnahme']
        ueberschreitungsBereichVorToleranz = checkAusserorts(ueberschreitung)['ueberschreitungsBereich']
        busseNachToleranz = checkAusserorts(ueberschreitungNachToleranz)['busse']
        massnahmeNachToleranz = checkAusserorts(ueberschreitungNachToleranz)['massnahme']
        ueberschreitungsBereichNachToleranz = checkAusserorts(ueberschreitungNachToleranz)['ueberschreitungsBereich']

    else:
        busseVorToleranz = checkAutobahn(ueberschreitung)['busse']
        massnahmeVorToleranz = checkAutobahn(ueberschreitung)['massnahme']
        ueberschreitungsBereichVorToleranz = checkAutobahn(ueberschreitung)['ueberschreitungsBereich']
        busseNachToleranz = checkAutobahn(ueberschreitungNachToleranz)['busse']
        massnahmeNachToleranz = checkAutobahn(ueberschreitungNachToleranz)['massnahme']
        ueberschreitungsBereichNachToleranz = checkAutobahn(ueberschreitungNachToleranz)['ueberschreitungsBereich']

        
    return render(request, "bussenRechner/result.html",
                  {'ueberschreitungVorToleranz': ueberschreitung,
                   'ueberschreitungNachToleranz': ueberschreitungNachToleranz,
                   'busseVorToleranz': busseVorToleranz,
                   'massnahmeVorToleranz': massnahmeVorToleranz,
                   'busseNachToleranz': busseNachToleranz,
                   'massnahmeNachToleranz': massnahmeNachToleranz,
                   'ueberschreitungsBereichVorToleranz': ueberschreitungsBereichVorToleranz,
                   'ueberschreitungsBereichNachToleranz': ueberschreitungsBereichNachToleranz,
                   'tatsaechlicheGeschwindigkeit': tatsaechlicheGeschwindigkeit,
                   'toleranz': toleranz,
                   'messverfahren': request.POST['messverfahren']
                   })

def form(request):
   return render(request, 'bussenRechner/form.html')


def checkInnerorts(ueberschreitung):
    if (ueberschreitung <= 0):
        return {'busse': 0, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[0 kmh]"}
    elif (ueberschreitung <= 5):
        return {'busse': 40, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[1 - 5 kmh]"}
    elif (ueberschreitung <= 10):
        return {'busse': 120, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[6 - 10 kmh]"}
    elif (ueberschreitung <= 15):
        return {'busse': 250, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[11 - 15 kmh]"}
    elif (ueberschreitung <= 20):
        return {'busse': 400, 'massnahme': "Verwarnung oder Anzeige (evt. 1 Monat Entzug)", 'ueberschreitungsBereich': "[16 - 20 kmh]"}
    elif (ueberschreitung <= 24):
        return {'busse': 400, 'massnahme': "Anzeige und 1 Monat Entzug", 'ueberschreitungsBereich': "[21 - 24 kmh]"}
    elif (ueberschreitung < 40):
        return {'busse': 400, 'massnahme': "Anzeige und 3 Monate Entzug", 'ueberschreitungsBereich': "[25 - 39]"}
    elif (ueberschreitung >= 40):
        return {'busse': 400, 'massnahme': "Raserdelikt, mindestens 2 Jahre Entzug", 'ueberschreitungsBereich': "[ab 40 kmh]"}


def checkAusserorts(ueberschreitung):
    if (ueberschreitung <= 0):
        return {'busse': 0, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[0 kmh]"}
    elif (ueberschreitung <= 5):
        return {'busse': 40, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[1 - 5 kmh]"}
    elif (ueberschreitung <= 10):
        return {'busse': 100, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[6 - 10 kmh]"}
    elif (ueberschreitung <= 15):
        return {'busse': 160, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[11 - 15 kmh]"}
    elif (ueberschreitung <= 20):
        return {'busse': 240, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[16 - 20 kmh]"}
    elif (ueberschreitung <= 25):
        return {'busse': 400, 'massnahme': "Verwarnung oder Anzeige (evt. 1 Monat Entzug)", 'ueberschreitungsBereich': "[21 - 25 kmh]"}
    elif (ueberschreitung < 30):
        return {'busse': 400, 'massnahme': "Anzeige und 1 Monat Entzug", 'ueberschreitungsBereich': "[26 - 29 kmh]"}
    elif (ueberschreitung < 60):
        return {'busse': 400, 'massnahme': "Anzeige und 3 Monate Entzug", 'ueberschreitungsBereich': "[30 - 59 kmh]"}
    elif (ueberschreitung >= 60):
        return {'busse': 400, 'massnahme': "Raserdelikt, mindestens 2 Jahre Entzug", 'ueberschreitungsBereich': "[ab 60 kmh]"}


def checkAutobahn(ueberschreitung):
    if (ueberschreitung <= 0):
        return {'busse': 0, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[0 kmh]"}
    elif (ueberschreitung <= 5):
        return {'busse': 20, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[1 - 5 kmh]"}
    elif (ueberschreitung <= 10):
        return {'busse': 60, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[6 - 10 kmh]"}
    elif (ueberschreitung <= 15):
        return {'busse': 120, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[11 - 15 kmh]"}
    elif (ueberschreitung <= 20):
        return {'busse': 180, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[16 - 20 kmh]"}
    elif (ueberschreitung <= 25):
        return {'busse': 260, 'massnahme': "Keine Massnahmen", 'ueberschreitungsBereich': "[20 - 25 kmh]"}
    elif (ueberschreitung <= 30):
        return {'busse': 400, 'massnahme': "Verwarnung oder Anzeige (evt. 1 Monat Entzug)", 'ueberschreitungsBereich': "[26 - 30 kmh]"}
    elif (ueberschreitung < 35):
        return {'busse': 400, 'massnahme': "Anzeige und 1 Monat Entzug", 'ueberschreitungsBereich': "[31 - 34 kmh]"}
    elif (ueberschreitung < 80):
        return {'busse': 400, 'massnahme': "Anzeige und 3 Monate Entzug", 'ueberschreitungsBereich': "[35 - 79 kmh]"}
    elif (ueberschreitung >= 80):
        return {'busse': 400, 'massnahme': "Raserdelikt, mindestens 2 Jahre Entzug", 'ueberschreitungsBereich': "[ab 80 kmh]"}


def checkToleranz(messverfahren, tatsaechlicheGeschwindigkeit):
    if (messverfahren == 'Radarmessung'):
        if(tatsaechlicheGeschwindigkeit <=100):
            return 5
        
        elif (tatsaechlicheGeschwindigkeit <= 150):
            return 6

        else:
            return 7
    else:
        if(tatsaechlicheGeschwindigkeit <=100):
            return 3
        
        elif (tatsaechlicheGeschwindigkeit <= 150):
            return 4

        else:
            return 5