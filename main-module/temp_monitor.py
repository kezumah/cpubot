import thingspeak
import schedule
from twitter_bot_module import Twitter_Bot
from gpiozero import CPUTemperature
from time import sleep, strftime

# Declare CPU, thingspeak and local variables
cpu = CPUTemperature()

channel_id = 1357661
write_key = '037QCFSLSVG4MFMZ'
# read_key = 'TZ9SADGMTGS7B3M0'

degree_sign = u"\N{DEGREE SIGN}"
twitter = Twitter_Bot()
warning_dict = {}


# Define write_temp() function to write temperature to thingspeak
def write_temp(temp, channel_write):
    try:
        response = channel_write.update({'field1': temp})
        print(temp, strftime("%Y-%m-%d %H:%M:%S"))

    except:
        print("Connection Failed")


# Define log_temp() function to get the temperature and log temp to twitter and thingspeak
def log_temp(tweets):
    temp = cpu.temperature
    time = strftime("%Y-%m-%d %H:%M:%S")
    write_temp(temp, channel_write)
    if temp >= 60:
        out_string = f"Warning! High CPU Temperature: {temp}{degree_sign}C recorded on {time}"
        print(out_string)
        tweets.tweet(out_string)
        warning_dict.update({time: temp})


# Define daily_brief() function to make a daily brief string and send it to twitter
def daily_brief(warning, tweets):
    min_temp = 10000
    max_temp = -10000
    out_string = f"{len(warning)} warnings in total today\n"
    if len(warning) != 0:
        for time_out, temp in warning.items():
            if temp < min_temp:
                min_temp = temp
            if temp > max_temp:
                max_temp = temp
        out_string += f"Max Warning Temperature Today: {max_temp}{degree_sign}C\n"
        out_string += f"Min Warning Temperature Today: {min_temp}{degree_sign}C\n"
    tweets.tweet(out_string)
    print(out_string)


# Define good_bye function to terminate the program
def good_bye(tweets):
    # tweets.tweet("Farewell!")
    print("Farewell!")
    quit()


# Use schedule to log temperature every 10 mins, report daily brief at 23:50 and close the program at 23:51 everyday
schedule.every(10).minutes.do(log_temp, tweets=twitter)
schedule.every().day.at("23:50:00").do(daily_brief, warning=warning_dict, tweets=twitter)
schedule.every().day.at("23:51:00").do(good_bye, tweets=twitter)

# main program
if __name__ == "__main__":
    print("Hello World!")
    channel_write = thingspeak.Channel(id=channel_id, api_key=write_key)
    # channel_read = thingspeak.Channel(id=channel_id, api_key=read_key)
    while True:
        schedule.run_pending()
        sleep(1)
