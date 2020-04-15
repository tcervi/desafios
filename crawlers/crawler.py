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


try:
    # html = urlopen(OLD_REDDIT_URL + "Art")
    # res = BeautifulSoup(html.read(), "html5lib")
    output_file = open("resSample.html", "r")
    res = BeautifulSoup(output_file.read(), "html5lib")
    output_file.close()

    print(res.title)
    threads_raw = res.findAll("div", {"id": re.compile("thing_t3_")})
    threads_hot = []
    print(len(threads_raw))
    for thread in threads_raw:
        print(thread)
except HTTPError as error:
    print(error)
except URLError as error:
    print(error)