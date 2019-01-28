# https://www.welcomekakao.com/learn/courses/30/lessons/42893?language=python3
'''
input html을 돌면서 '기본점수', '외부링크', 'url'을 구한 후
'외부링크'를 이용하여 링크 점수 반영
'''


import re
class Page:
    def __init__(self, url, normal, external_links):
        self.url = url  # page의 url
        self.normal = normal  # 기본 점수
        self.external_links = external_links  # 외부 링크의 list
        self.rank = normal


# return (url, normal, external_links)
def parse_html(word, html):
    # count number of occurence of word insensitively
    def count(target, word_list):
        result = 0
        for word in word_list:
            if word.lower() == target.lower():
                result += 1

        return result

    url_pattern = re.compile(r'meta property="og:url" content="https://(?P<url>[^"]+)', re.DOTALL)
    url = url_pattern.search(html).group('url')

    # body_pattern = re.compile(r'<body>(?P<body>.+)</body>', re.DOTALL)
    # body = body_pattern.search(html).group('body')

    word_pattern = re.compile(r'[a-zA-Z]+')
    all_words = word_pattern.findall(html)
    normal = count(word, all_words)

    link_pattern = re.compile(r'<a href="https://(?P<link>[^"]+)')
    external_links = link_pattern.findall(html)
    external_links = list(set(external_links)) # remove duplicate

    return url, normal, external_links


def solution(word, pages):
    dic = dict() # key: url, value: Page

    # pages를 돌면서 Page instance를 생성
    for idx, html in enumerate(pages):
        url, normal, external_links = parse_html(word, html)
        page = Page(url, normal, external_links)
        dic[url] = (idx, page)

    # 모든 Page instance에 대해 링크점수를 반영
    for url in dic:
        page = dic[url][1]
        external_links = page.external_links
        if len(external_links):
            power = page.normal / len(external_links)
            for link in external_links:
                if link in dic:
                    dic[link][1].rank += power

    # dic을 list로 바꾼 후, rank는 desc, idx는 asc로 정렬
    arr = []
    for url in dic:
        arr.append(dic[url])

    arr.sort(key=lambda x: (-x[1].rank, x[0]))
    return arr[0][0]


i1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
i2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution('blind', i1))
print(solution('Muzi', i2))
