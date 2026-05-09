"""Timezone clock challenge: pick a country from a shelve-backed menu and display its current local time."""
import datetime
import shelve
import pytz


def menu_list():
    print("Select a Time Zone you would like to see: ")
    print("0: Exit")
    print("1: Japan")
    print("2: Sweden")
    print("3: Russia")
    print("4: New Zealand")
    print("5: Mexico")
    print("6: Madagascar")
    print("7: South Korea")
    print("8: Israel")
    print("9: France")


menu = shelve.open('timezones')

menu['0'] = 'quit'
menu['1'] = {'JP': 'Asia/Tokyo'}
menu['2'] = {'SE': 'Europe/Stockholm'}
menu['3'] = {'RU': 'Asia/Anadyr'}
menu['4'] = {'NZ': 'Pacific/Auckland'}
menu['5'] = {'MX': 'America/Bahia_Banderas'}
menu['6'] = {'MG': 'Indian/Antananarivo'}
menu['7'] = {'KR': 'Asia/Seoul'}
menu['8'] = {'IL': 'Asia/Jerusalem'}
menu['9'] = {'FR': 'Europe/Paris'}

while True:
    menu_list()
    country = ''
    choice = str(input(">>"))
    if choice == '0':
        print("Exit Program")
        break
    for key in menu[choice]:
        country = key
    timezone = menu[choice][country]

    time = datetime.datetime.now(tz=pytz.timezone(menu[choice][country]))
    country_name = pytz.country_names[country]

    print(f"You have chosen {country_name}")
    print(f"It is currently {time} in {country_name}")
    print()
    print(f"Where you are at it is currently {datetime.datetime.now()}")
    print()
    print(f"In UTC time it is currently {datetime.datetime.utcnow()}")
    print("_" * 80)
    input("Press Enter")

menu.close()
