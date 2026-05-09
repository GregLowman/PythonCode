"""Print current local time for every country and timezone using pytz."""
import pytz
import datetime

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

print(f"{pytz.country_names['JP']} : {datetime.datetime.now(tz=pytz.timezone(pytz.country_names['jp']))}")
print(f"{pytz.country_names['JP']} : {datetime.datetime.now(tz=pytz.timezone('japan'))}")
