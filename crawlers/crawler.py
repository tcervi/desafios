from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


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


OLD_REDDIT_URL = "https://old.reddit.com/r/"


def extract_hot_threads(threads_raw, min_score=5000):
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
            print(thread["data-score"])
            hot_threads.append(thread)
    else:
        return hot_threads


def main():
    try:
        # html = urlopen(OLD_REDDIT_URL + "Art")
        # res = BeautifulSoup(html.read(), "html5lib")
        output_file = open("resSample.html", "r")
        res = BeautifulSoup(output_file.read(), "html5lib")
        output_file.close()

        print(res.title)
        threads_raw = res.findAll("div", {"id": re.compile("thing_t3_")})
        print(len(threads_raw))
        threads_hot = extract_hot_threads(threads_raw)

    except HTTPError as error:
        print(error)
    except URLError as error:
        print(error)


if __name__ == '__main__':
    main()