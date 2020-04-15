import argparse
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
        return [self.subr_name, self.score, self.thread_title, self.thread_url, self.comments_url]


def print_result_list(result_list):
    """Given a list of HotThreadResult objects, print the information in a table format

    :param result_list: the list of HotThreadResult objects
    :return:
    """

    printable_results = []
    for result in result_list:
        printable_results.append(result.get_printable())

    print(tabulate(printable_results, headers=["Subreddit", "Score", "Thread Title", "Thread URL", "Comments URL"]))


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


def main():
    parser = argparse.ArgumentParser(description='Simple Subreddits crawler implementation in Python.')
    parser.add_argument('--subr_list', default="worldnews", help='List of Subreddits to search, separated by ; ')
    parser.add_argument('--trending_score', default=5000, type=int, help='Minimum score for a thread to be trending')
    args = parser.parse_args()


    try:
        # html = urlopen(OLD_REDDIT_URL + "/r/" + "worldnews")
        # res = BeautifulSoup(html.read(), "html5lib")
        output_file = open("resSample.html", "r")
        res = BeautifulSoup(output_file.read(), "html5lib")
        output_file.close()

        threads_raw = res.findAll("div", {"id": re.compile("thing_t3_")})
        threads_hot = extract_hot_threads(threads_raw, args.trending_score)
        result_list = assemble_result_list(threads_hot)
        print_result_list(result_list)

    except HTTPError as error:
        print(error)
    except URLError as error:
        print(error)


if __name__ == '__main__':
    main()