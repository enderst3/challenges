import time
import datetime
import pytz

print('The epoch time on this system starts at ' + time.strftime('%c', time.gmtime(0)))
print('The current timezone is {0}, with an offset of {1}'.format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print('\t Daylight Saving Time is in effect for this location')
    print('\t The DST timezone is ' + time.tzname[1])

print('The local time is ' + time.strftime('%m-%d-%Y %H:%M:%S', time.localtime()))
print('UTC time is ' + time.strftime('%m-%d-%Y %H:%M:%S', time.gmtime()))

print('=' * 50)

# datetime will format for you
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print('=' * 50)

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print('The time in {} is {}'.format(country, local_time))
print('UTC is {}'.format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ': ' + pytz.country_names[x])

for x in sorted(pytz.country_names):
    print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

# a better way to print out the above info
for x in sorted(pytz.country_names):
    print('{}: {}'.format(x, pytz.country_names[x], end=': '))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print('\t\t{}: {}'.format(zone, local_time))
    else:
        print('\t\tNo time zone defined')

