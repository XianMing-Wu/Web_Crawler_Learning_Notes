from typing import List
from bs4 import BeautifulSoup
import requests
from common import NoteContent, NoteContentDetail
BASE_HOST = "https://www.ptt.cc"
FIRST_N_PAGE = 10  # 前N页的论坛帖子数据
# 此代码定义了一个名为 HEADERS 的字典，用于模拟 HTTP 请求头。
# 在网络爬虫中，请求头可以向服务器表明请求的相关信息。
# "User-Agent" 是请求头中的一个字段，它模拟了 Chrome 浏览器 116 版本在 Windows 10 64 位系统下的标识，
# 作用是让服务器认为请求是由该浏览器发出的，避免因无标识或使用爬虫标识而被服务器拒绝访问。
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
def parse_note_use_bs(html_content: str) -> NoteContent:
    """
    使用BeautifulSoup提取帖子标题、作者、发布日期，基于css选择器提取
    需要注意的时，我们在提取帖子的时候，可能有些帖子状态不正常，会导致没有link之类的数据，所以我们在取值时最好判断一下元素长度
    :param html_content: html源代码内容
    :return:
    """
    # 初始化一个帖子保存容器
    note_content = NoteContent()

    soup = BeautifulSoup(html_content, "lxml")
    # 提取标题并去左右除换行空格字符
    note_content.title = soup.select("div.r-ent div.title a")[0].text.strip() if len(
        soup.select("div.r-ent div.title a")) > 0 else ""

    # 提取作者
    note_content.author = soup.select("div.r-ent div.meta div.author")[0].text.strip() if len(
        soup.select("div.r-ent div.meta div.author")) > 0 else ""

    # 提取发布日期
    note_content.publish_date = soup.select("div.r-ent div.meta div.date")[0].text.strip() if len(
        soup.select("div.r-ent div.meta div.date")) > 0 else ""

    # 提取帖子链接
    note_content.detail_link = soup.select("div.r-ent div.title a")[0]["href"] if len(
        soup.select("div.r-ent div.title a")) > 0 else ""
    return note_content

def get_previous_page_number() -> int:
    """
    打开首页提取上一页的分页Number
    :return:
    """
    css_selector = "#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)"
    uri = "/bbs/Stock/index.html"
    response = requests.get(BASE_HOST + uri, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("send request got error status code, reason：", response.text)
    soup = BeautifulSoup(response.text, "lxml")
    pagination_link = soup.select(css_selector)[0]["href"].strip()
    previous_page_number = int(pagination_link.replace("/bbs/Stock/index", "").replace(".html", ""))
    return previous_page_number


def fetch_bbs_note_list(previous_page_number: int) -> List[NoteContent]:
    """
    获取前N页的帖子列表
    :return:
    """
    notes_list: List[NoteContent] = []

    # 计算分页的起始位置和终止位置，由于我们也是要爬首页的，所以得到上一页的分页Number之后，应该还要加1才是我们的起始位置
    start_page_number = previous_page_number + 1
    end_page_number = start_page_number - FIRST_N_PAGE
    for page_number in range(start_page_number, end_page_number, -1):
        print(f"开始获取第 {page_number} 页的帖子列表 ...")

        # 根据分页Number拼接帖子列表的URL
        uri = f"/bbs/Stock/index{page_number}.html"
        response = requests.get(url=BASE_HOST + uri, headers=HEADERS)
        if response.status_code != 200:
            print(f"第{page_number}页帖子获取异常,原因：{response.text}")
            continue

        # 使BeautifulSoup的CSS选择器解析数据，div.r-ent 是帖子列表html页面中每一个帖子都有的css class
        soup = BeautifulSoup(response.text, "lxml")
        all_note_elements = soup.select("div.r-ent")
        for note_element in all_note_elements:
            # 调用prettify()方法可以获取整个div元素的HTML内容
            note_content: NoteContent = parse_note_use_bs(note_element.prettify())
            print(note_content)
            notes_list.append(note_content)
        print(f"结束获取第 {page_number} 页的帖子列表，本次获取到:{len(all_note_elements)} 篇帖子...")
    return notes_list


def fetch_bbs_note_detail(note_content: NoteContent) -> NoteContentDetail:
    """
    获取帖子详情页数据
    :param note_content:
    :return:
    """
    pass

def run_crawler():
    # step1 获取分页number
    previous_number: int = get_previous_page_number()

    # step2 获取前N页帖子集合列表
    note_list: List[NoteContent] = fetch_bbs_note_list(previous_number)

    # step3 获取帖子详情+推文
    for note_content in note_list:
        note_content_detail = fetch_bbs_note_detail(note_content)
        print(note_content_detail)
        

    print("任务爬取完成.......")


if __name__ == '__main__':
    run_crawler()
