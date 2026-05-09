"""Build a country lookup dictionary from a pipe-delimited file and let the user query capitals interactively."""
new_countries = {}
with open('country_info.txt') as countries:
    countries.readline()
    for row in countries:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }
        new_countries[country.casefold()] = country_dict
        new_countries[code.casefold()] = country_dict

while True:
    word = input("Select a country to see there capital: ").casefold()
    if word in new_countries.keys():
        the_capital = new_countries[word]['capital']
        print(f"The capital of {word} is {the_capital}")
        print("type Q to quit")
        pass
    elif word == 'q'.casefold():
        break
    else:
        print("Please select a country from the list: ")
        for place in new_countries.keys():
            print(place)
        pass
