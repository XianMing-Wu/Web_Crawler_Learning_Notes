from typing import List

from common import NoteContent, NoteContentDetail

def get_previous_page_number() -> int:
    """
    打开首页提取上一页的分页Number
    :return:
    """
    xpath_selector = ""
    pass


def fetch_bbs_note_list(previous_page_number: int) -> List[NoteContent]:
    """
    获取前N页的帖子列表
    :return:
    """
    return []


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
