from django.shortcuts import render
from .models import Person

# Create your views here.
def start(request):
    return render(request, 'kamelRechner/start.html')

def form(request, gender):
    return render(request, 'kamelRechner/form.html', {'gender': gender})

def result(request, gender):

    punktzahl = 0

    height = int(request.POST['height'])
    weight = int(request.POST['weight'])
    iq = int(request.POST['iq'], 0)
    hair = int(request.POST['hair'])
    beard = int(request.POST.get('beard', 0))
    age = int(request.POST['age'])
    jewlery = 0

    for i in range(1,7):
        jewlery += int(request.POST.get("jewlery" + str(i), 0))


    punktzahl += getPzAge(age)

    punktzahl += getPzHeight(height, gender)

    punktzahl += getPzBmi(height, weight, gender)

    if gender != 'female':
        punktzahl += getPzBfp(request.POST['radios'])

        punktzahl += getPzBeard(beard)

    else:
        punktzahl += getPzBodyType(request.POST['radios'])

        punktzahl += getPzJewlery(jewlery)



    punktzahl += getPzIq(iq)

    punktzahl += getPzHair(hair, gender)

    person = createPerson(request.POST['name'], age, height, weight, request.POST['radios'], iq, hair, beard, jewlery, punktzahl)
    person.save()

    return render(request, 'kamelRechner/result.html', {"punktzahl": punktzahl, "name": request.POST['name']})

def ranking(request):
    people = Person.objects.order_by('camelValue').reverse()
    return render(request, 'kamelRechner/ranking.html', {'people': people})

def getPzAge(age):
    if age > 60:
        return 2
    elif age > 50:
        return 4
    elif age > 40:
        return 6
    elif age > 30 or age < 18:
        return 8
    elif 18 <= age <= 30:
        return 10


def getPzHeight(height, gender):
    if gender == 'male':
        if height <= 154 or height >= 225:
            return 2
        elif height <= 164 or height >= 215:
            return 4
        elif height <= 174 or height >= 205:
            return 6
        elif height <= 184 or height >= 195:
            return 8
        elif height <= 194:
            return 10
    else:
        if height <= 129 or height> 200:
            return 2
        elif height <= 139 or height >= 190:
            return 4
        elif height <= 149 or height >= 180:
            return 6
        elif height <= 159 or height >= 170:
            return 8
        elif height <= 169:
            return 10

    
def getPzBmi(height, weight, gender):
    bmi = weight / (height/100) **2

    if gender == 'male':
        if 40 <= bmi:
            return 1
        elif bmi < 18.5 or 35 < bmi < 40:
            return 5
        elif 18.5 <= bmi < 25:
            return 8
        elif 25 <= bmi <= 35:
            return 10
    else:
        if 40 <= bmi:
            return 1
        elif 30 <= bmi or bmi < 18.5:
            return 5
        elif 25 <= bmi:
            return 8
        elif 18 <= bmi:
            return 10
    
def getPzBfp(bpf):
    if bpf == '5':
        return 2
    elif bpf == '4':
        return 5
    elif bpf == '1' or bpf == '3':
        return 8
    elif bpf == '2':
        return 10
    
def getPzBodyType(bd):
    if bd == '5':
        return 2
    elif bd == '1':
        return 5
    elif bd == '4' or bd == '2':
        return 8
    elif bd == '3':
        return 10

def getPzIq(iq):
    if iq < 70:
        return 0
    elif iq < 85:
        return 2
    elif iq < 100:
        return 3
    elif iq < 115:
        return 5
    elif iq < 130:
        return 8
    elif 130 <= iq:
        return 10
    
def getPzHair(hair, gender):
    if gender == 'male': 
        if hair == 1:
            return 5
        elif hair == 2:
            return 3
        elif hair == 3:
            return 1
    else:
        if hair == 1:
            return 5
        elif hair == 2:
            return 3
        elif hair == 3:
            return 1

def getPzBeard(beard):
    if beard == 1:
        return 3
    else:
        return 0

def getPzJewlery(jewlery):
    if jewlery < 1 or jewlery > 5:
        return 0
    elif jewlery == 1 or jewlery == 5:
        return 1
    elif jewlery == 2 or jewlery == 4:
        return 2
    elif jewlery == 3:
        return 3
    
def createPerson(name, age, height, weight, body, iq, hair, beard, jewlery, camelValue):
    # created = Subject.objects.get_or_create(name="A new subject")
    if Person.objects.filter(name=name).exists():
        person = Person.objects.get(name=name)
        """
        person.__setattr__(camelValue = camelValue,
                    age = age,
                    height = height,
                    weight = weight,
                    body = body,
                    iq = iq,
                    hair = hair,
                    beard = beard,
                    jewlery = jewlery)
        """
        person.camelValue = camelValue
        person.age = age
        person.height = height
        person.weight = weight
        person.body = body
        person.iq = iq
        person.hair = hair
        person.beard = beard
        person.jewlery = jewlery

    else:
        person = Person(name = name,
                        camelValue = camelValue,
                        age = age,
                        height = height,
                        weight = weight,
                        body = body,
                        iq = iq,
                        hair = hair,
                        beard = beard,
                        jewlery = jewlery)
    return person