import os
import multiprocessing
import telebot
import time
from multiprocessing import Process
from crawler import handle_subreddit, TRENDING_SCORE_DEFAULT

TELEGRAM_BOT_TOKEN = "BORED_REDDIT_BOT_TOKEN"


def assemble_telegram_response(return_list):
    """Given a list of lines (strings) to be assembled as a telegram message response,
    return a single string for that response

    :param return_list: the list of lines (strings) to be assembled as telegram message response
    :return: a single string for that response
    """
    return_string = ''
    for string in return_list:
        return_string = return_string + string
    else:
        return return_string


def spawn_crawlers(subr_list, return_list):
    """Given a list of SubReddit names and a Manager list object, spawn a crawler for each SubReddit to collect
    trending threads information and store results into the Manager list object

    :param subr_list: the list of SubReddit names
    :param return_list: the Manager list object
    :return:
    """
    for subr in subr_list:
        process = Process(target=handle_subreddit, args=(subr.strip(), TRENDING_SCORE_DEFAULT, return_list))
        process.start()
        process.join()
        time.sleep(10)


def main():
    bot = telebot.TeleBot(os.environ[TELEGRAM_BOT_TOKEN])

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Wanna some info about SubReddit threads??")

    @bot.message_handler(commands=['NadaPraFazer'])
    def fetch_subreddits(message):
        params_str = message.text.replace('/NadaPraFazer', '')
        manager = multiprocessing.Manager()
        return_list = manager.list()
        spawn_crawlers(params_str.rsplit(";"), return_list)
        response = assemble_telegram_response(return_list)
        if response is not '':
            bot.reply_to(message, response)
        else:
            bot.reply_to(message, "Sorry! Can't access Reddit now :(")

    bot.polling()


if __name__ == '__main__':
    main()
