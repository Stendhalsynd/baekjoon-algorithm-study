# 참고한 레퍼런스 : https://velog.io/@a101201031/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%B4%EC%84%9C-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B01

import os
import sys
import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter as MarkdownifyConverter

class MarkdownConverter:
  _module_path = os.path.dirname(os.path.abspath(__file__))

  def __init__(self, url, parser):
    self.request_html(url)
    self.convert_html_bs4(parser)
    self.title = self.find_category_title()

  def request_html(self, url):
    res = requests.get(url)
    self.html = res.text

  def convert_html_bs4(self, parser):
    self.soup = BeautifulSoup(self.html, "lxml")

  def find_category_title(self):
    category_title_soup = self.soup.find("ol", "breadcrumb")
    _, _, tilte_soup = category_title_soup.find_all("li")

    title = tilte_soup.get_text()
    return title

if __name__ == "__main__":
  url = "https://school.programmers.co.kr/learn/courses/30/lessons/60057"
  if len(sys.argv) != 1:
    url = sys.argv[1]

  markdown_converter = MarkdownConverter(url, "lxml")
  print(markdown_converter.title)