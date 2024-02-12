# developed by Jeonhui Lee
# pip3 install requests
# pip3 install bs4

'''
Baekjoon 문제 번호로 문제 불러오기
'''

import sys

def get_baekjoonproblem(problem_number):
  
  import requests
  from bs4 import BeautifulSoup as Soup
  # problem_number = sys.stdin.readline().rstrip()
  # 문제 번호 입력

  try:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    soup = Soup(requests.get('https://www.acmicpc.net/problem/' + problem_number, headers=headers).text, 'html.parser')

    # 문제 주소의 html 파일을 text로 불러옴
    title = soup.find('span', {'id': 'problem_title'}).text

    # id가 problem_title인 span태그를 찾음
    return title

  except Exception as e:
    # 잘못된 입력이 들어왔을 시에 problem_tilte을 찾지 못함 -> 종료
    print("잘못된 문제 번호입니다.", e)
    return

if __name__ == '__main__':
  problem_number = sys.argv[1]

  problem_title=get_baekjoonproblem(problem_number)
  print(problem_title)