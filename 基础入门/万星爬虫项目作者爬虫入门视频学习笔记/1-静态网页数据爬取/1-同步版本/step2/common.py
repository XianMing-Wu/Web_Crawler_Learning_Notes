from typing import List


class NoteContent:
    """
    帖子简介存储容器
    """
    title: str = ""  # 帖子标题
    author: str = ""  # 帖子作者
    publish_date: str = ""  # 帖子发表日期
    detail_link: str = ""  # 帖子详情
    def __str__(self):
        return f"""
            Title: {self.title}
            User: {self.author}
            Publish Date: {self.publish_date}
            Detail Link: {self.detail_link}        
        """

class NotePushComment:
    """
    推文存储容器
    """
    push_user_name: str = ""  # 推文人
    push_cotent: str = ""  # 推文内容
    push_time: str = ""  # 推文时间
    def __repr__(self):
        """
        返回对象的字符串表示形式，主要用于调试和开发。
        __repr__ 方法的目标是返回一个字符串，该字符串能够尽可能详细地描述对象，
        理想情况下这个字符串可以通过 eval() 函数重新创建出相同的对象。
        
        示例：
        >>> comment = NotePushComment()
        >>> comment.push_user_name = "user1"
        >>> comment.push_cotent = "不错的帖子！"
        >>> comment.push_time = "2023-10-01 10:00"
        >>> print(comment)
        NotePushComment(push_user_name='user1', push_cotent='不错的帖子！', push_time='2023-10-01 10:00')
        
        这里实现 __repr__ 的原因是为了让 NoteContentDetail 的 push_comment 列表结构方便打印和调试。
        """
        return f"NotePushComment(push_user_name='{self.push_user_name}', push_cotent='{self.push_cotent}', push_time='{self.push_time}')"

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
    def __str__(self):
        return f"""
Title: {self.title}
User: {self.author}
Publish Datetime: {self.publish_datetime}
Detail Link: {self.detail_link}
Push Comments: {self.push_comment}        
"""