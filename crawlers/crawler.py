import re
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


OLD_REDDIT_URL_DEFAULT = "https://old.reddit.com"
TRENDING_SCORE_DEFAULT = 5000


class HotThreadResult:
    subr_name: str
    thread_title: str
    thread_url: str
    comments_url: str
    score: int

    def __init__(self, name: str, title: str, t_url: str, c_url: str, t_score: int):
        self.subr_name = name
        self.thread_title = title
        self.thread_url = t_url
        self.comments_url = c_url
        self.score = t_score

    def get_printable(self):
        return [self.subr_name, self.score, self.thread_title, self.comments_url]

    def get_textable(self):
        textable_str = ""
        textable_str += "SubReddit: " + self.subr_name + '\n'
        textable_str += "Score: " + self.score + '\n'
        textable_str += "Thread Title: " + self.thread_title + '\n'
        textable_str += "Comments URL: " + self.comments_url + '\n'
        textable_str += '\n'
        return textable_str


def print_result_list(result_list, return_list):
    """Given a list of HotThreadResult objects and a shared list in which the results will be written
    append results information to shared list (in a table format)

    :param result_list: the list of HotThreadResult objects
    :param return_list: the shared list in which the results will be written
    :return:
    """

    printable_results = []
    textable_response = ""
    for result in result_list:
        printable_results.append(result.get_printable())
        textable_response += result.get_textable()
    else:
        textable_response += "\n\n\n"

    print(tabulate(printable_results, headers=["Subreddit", "Score", "Thread Title", "Comments URL"]))
    print('\n')
    return_list.append(textable_response)


def assemble_result_list(hot_threads_list):
    """Given a list of hot threads, create a HotThreadResult instance for each thread
    and returns a list of HotThreadResult objects

    :param hot_threads_list:
    :return: a list of HotThreadResult objects
    """

    result_list = []
    for thread in hot_threads_list:
        t = BeautifulSoup(str(thread), "html5lib")
        name = t.div["data-subreddit"]
        title = t.find("a", {"class": re.compile("title")}).getText()
        c_url = t_url = OLD_REDDIT_URL_DEFAULT + t.div["data-permalink"]
        t_score = t.div["data-score"]
        result = HotThreadResult(name, title, t_url, c_url, t_score)
        result_list.append(result)
    else:
        return result_list


def extract_hot_threads(threads_raw, min_score=TRENDING_SCORE_DEFAULT):
    """Given a PageElements set, with any number of threads page elements, and a minimum score to consider one thread
    as a hot thread, returns a list containing only the hot threads from the original set

    :param threads_raw: the raw PageElements set to be filtered
    :param min_score: the minimum score to consider a thread valid
    :return: a list containing only the hot threads
    """

    hot_threads = []
    for thread in threads_raw:
        score = thread["data-score"]
        if score is None or int(score) < min_score:
            continue
        else:
            hot_threads.append(thread)
    else:
        return hot_threads


def handle_subreddit(subr_name, trending_score, return_list):
    """Given a Subreddit name, a minimum trending score and a shared list in which the results will be written
    execute the crawler process

    :param subr_name:
    :param trending_score:
    :param return_list: the shared list in which the results will be written
    :return:
    """

    try:
        html = urlopen(OLD_REDDIT_URL_DEFAULT + "/r/" + subr_name)
        res = BeautifulSoup(html.read(), "html5lib")

        threads_raw = res.findAll("div", {"id": re.compile("thing_t3_")})
        threads_hot = extract_hot_threads(threads_raw, trending_score)
        result_list = assemble_result_list(threads_hot)
        print_result_list(result_list, return_list)

    except HTTPError as error:
        print(error)
    except URLError as error:
        print(error)