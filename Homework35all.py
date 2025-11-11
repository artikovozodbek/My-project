# 1-masala. Cars nomli dictionary berilgan, bu dictionarydagi eng qimmat va eng arzon avtomobilni va avtomobillarning o'rtacha qiymatini chiqaring.
cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

car_max = max(cars, key=cars.get)
car_min = min(cars, key=cars.get)

print("Eng qimmat mashina:",car_max)
print("Eng arzon mashina:",car_min)

average_price = sum(cars.values()) / len(cars)

print("O'rtacha narx:",average_price)


# 2-masala. Movies nomli dictionary berilgan. Bu dictionarydagi filmlardan faqat 2000-yildan keyin chiqarilganlarini nomini chop eting.
movies = {
    "Titanic": 1997,
    "Avatar": 2009,
    "Inception": 2010,
    "Interstellar": 2014
}

for name, year in movies.items():
    if year > 2000:
        print(name)


# 3-masala. Mashinalarning tezligi haqidagi dictionary berilgan. Mashina nomi va tezligini tezlik bo'yicha kamayish tartibida(kattadan kichikka) chop eting.
cars = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

sorted_cars = sorted(cars.items(), key=lambda x: x[1], reverse=True)

for name, speed in sorted_cars:
    print(name, speed)


# 4-masala. Shaxslarning kasblari haqida dictionary berilgan. Bu dictionarydan foydalanib shaxsning ismi kiritilsa uning kasbini chiqaruvchi dastur kodini yozib bering.
people = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

name = input("Ismni kiriting: ")

professions = people.get(name)

if professions:
    print(f"{name} ning kasbi: {professions}")
else:
    print("Bunday ism topilmadi!.")

# 5-masala. Mashinalar va ularning nechta sotilgani haqida dictionary berilgan. Eng ko'p va eng kam sotilgan mashina turini chiqaring.
car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

max_car = max(car_count, key=car_count.get)
min_car = min(car_count, key=car_count.get)

print(max_car)
print(min_car)


# 6-masala. Quyida kitoblar haqida ma'lumot yozilgan dictionary berilgan. Sizning vazifangiz foydalanuvchi input orqali kitob nomini kiritadi, berilgan nomdagi kitob haqida ma'lumotlarni chop etish. Agar kitob dict ichida yo'q bo'lsa "Kitob topilmadi" xabarini chiqarish. Kitob nomi katta harfda kiritilganda ham kichik harfda kiritilganda ham kitob topilsin.
books = {
    "O'tkan kunlar": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1926,
        "tarjimalar soni": 5
    },
    "Mehrobdan chayon": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1929,
        "tarjimalar soni": 3
    },
    "Kecha va kunduz": {
        "muallifi": "Cho'lpon",
        "janri": "Roman",
        "chop etilgan yili": 1934,
        "tarjimalar soni": 4
    },
    "Sarob": {
        "Muallifi": "Abdulla Qahhor",
        "Janri": "Roman",
        "Chop etilgan yili": 1935,
        "Tarjimalar soni": 2
    },
    "Ulug'bek xazinasi": {
        "muallifi": "Odil Yoqubov",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1974,
        "tarjimalar soni": 6
    },
    "Don Kixot": {
        "muallifi": "Migel de Servantes",
        "janri": "Roman",
        "chop etilgan yili": 1605,
        "tarjimalar soni": 50
    },
    "Urush va tinchlik": {
        "muallifi": "Lev Tolstoy",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1869,
        "tarjimalar soni": 45
    },
    "Alkimyogar": {
        "muallifi": "Paulo Koelyo",
        "janri": "Falsafiy roman",
        "chop etilgan yili": 1988,
        "tarjimalar soni": 80
    },
    "1984": {
        "muallifi": "Jorj Oruell",
        "janri": "Antiutopik roman",
        "chop etilgan yili": 1949,
        "tarjimalar soni": 65
    },
    "Kichkina shahzoda": {
        "muallifi": "Antuan de Sent-Ekzyuperi",
        "janri": "Falsafiy ertak",
        "chop etilgan yili": 1943,
        "tarjimalar soni": 300
    }
}

name = input("Kitobni kirting: ")

if name in books:
    print("Kitob topildi. Malumotlar: ")
    for key, values in books[name].items():
        print(f"\t\t{key}: {values}" )
else:
    print("Bunday kitob topilmadi.")
