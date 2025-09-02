from typing import List


class NoteContent:
    """
    帖子简介存储容器
    """
    title: str = ""  # 帖子标题
    author: str = ""  # 帖子作者
    publish_date: str = ""  # 帖子发表日期
    detail_link: str = ""  # 帖子详情

class NotePushComment:
    """
    推文存储容器
    """
    push_user_name: str = ""  # 推文人
    push_cotent: str = ""  # 推文内容
    push_time: str = ""  # 推文时间

class NoteContentDetail:
    """
    帖子
    """
    title: str = ""  # 帖子标题
    author: str = ""  # 帖子作者
    publish_datetime: str = ""  # 帖子发表日期
    detail_link: str = ""  # 帖子详情链接
    push_comment: List[NotePushComment] = []  # 帖子推文列表，相当于国内评论列表
    # 示例：创建一个包含两条推文的列表
    # example_push_comments = [
    #     NotePushComment(push_user_name="user1", push_cotent="这篇帖子写得真好！", push_time="2023-10-01 12:00"),
    #     NotePushComment(push_user_name="user2", push_cotent="受益匪浅，感谢分享！", push_time="2023-10-01 13:00")
    # ]
