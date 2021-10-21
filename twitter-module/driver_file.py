import twitter_bot_module


def main():
    Bot = twitter_bot_module.Twitter_Bot()
    print(Bot.tweet("Test Tweet"))

main()
