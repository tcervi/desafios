import os
import multiprocessing
import telebot
import time
from multiprocessing import Process
from crawler import handle_subreddit, TRENDING_SCORE_DEFAULT


TELEGRAM_BOT_TOKEN = "BORED_REDDIT_BOT_TOKEN"


def assemble_telegram_response(return_list):
    """

    :param return_list:
    :return:
    """
    return_string = ''
    for string in return_list:
        return_string = return_string + string
    else:
        return return_string


def spawn_crawlers(subr_list, return_list):
    """

    :param subr_list:
    :param return_list:
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