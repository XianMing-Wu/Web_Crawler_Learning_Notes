```mermaid
graph TD
    Start["开始爬虫"] --> Config["初始化配置"]
    Config --> Step1["步骤1: 获取分页Number"]
    Step1 --> GetPageNum["get_previous_page_number异步函数"]
    GetPageNum --> CreateClient["创建AsyncClient"]
    CreateClient --> SendRequest["发送异步请求"]
    SendRequest --> CheckStatus["检查响应状态"]
    CheckStatus --> Success["解析页面内容"]
    CheckStatus --> Error["抛出异常"]
    Success --> ExtractPageNum["提取分页Number"]
    ExtractPageNum --> Step2["步骤2: 获取帖子列表"]
    Step2 --> CalcRange["计算分页范围"]
    CalcRange --> LoopPages["循环遍历页面"]
    LoopPages --> CreateClient2["创建AsyncClient"]
    CreateClient2 --> FetchPage["fetch_bbs_note_list异步函数"]
    FetchPage --> SendRequest2["发送异步请求"]
    SendRequest2 --> CheckStatus2["检查响应状态"]
    CheckStatus2 --> Success2["解析页面内容"]
    CheckStatus2 --> Error2["记录错误并跳过"]
    Error2 --> LoopPages
    Success2 --> LoopNotes["循环遍历帖子"]
    LoopNotes --> ParseNote["parse_note_use_parsel异步函数"]
    ParseNote --> CreateNote["创建NoteContent对象"]
    CreateNote --> AddList["添加到列表"]
    AddList --> LoopNotes
    LoopNotes --> CompletePage["记录页面信息"]
    CompletePage --> LoopPages
    LoopPages --> Step3["步骤3: 获取帖子详情+推文数据"]
    Step3 --> LoopDetail["遍历帖子列表"]
    LoopDetail --> CheckLink{"检查detail_link是否存在"}
    CheckLink --> |存在| FetchDetail["fetch_bbs_note_detail异步函数"]
    CheckLink --> |不存在| SkipNote["跳过该帖子"]
    SkipNote --> LoopDetail
    FetchDetail --> CreateClient3["创建AsyncClient"]
    CreateClient3 --> SendRequest3["发送异步请求"]
    SendRequest3 --> CheckStatus3["检查响应状态"]
    CheckStatus3 --> Success3["解析帖子详情页"]
    CheckStatus3 --> Error3["记录错误并返回"]
    Error3 --> LoopDetail
    Success3 --> ExtractDetail["提取帖子详细信息"]
    ExtractDetail --> ExtractTitle["提取标题"]
    ExtractDetail --> ExtractAuthor["提取作者"]
    ExtractDetail --> ExtractDate["提取发布时间"]
    ExtractDate --> ExtractPush["提取推文数据"]
    ExtractPush --> LoopPush["遍历所有推文元素"]
    LoopPush --> CreatePush["创建NotePushComment对象"]
    CreatePush --> AddPush["添加到推文列表"]
    AddPush --> LoopPush
    LoopPush --> CreateDetail["创建NoteContentDetail对象"]
    CreateDetail --> SaveDetail["保存帖子详情数据"]
    SaveDetail --> LoopDetail
    LoopDetail --> RunCrawler["run_crawler异步函数"]
    RunCrawler --> EventLoop["启动asyncio事件循环"]
    EventLoop --> End["任务完成"]
```

## 主要变化说明

1. **异步函数标记**：所有函数都标记为异步函数，使用`async def`定义
2. **异步HTTP客户端**：添加了`AsyncClient`的创建和管理流程
3. **异步请求**：所有HTTP请求都改为异步请求，使用`await client.get()`
4. **异步解析**：帖子解析函数从`parse_note_use_bs`改为`parse_note_use_parsel`
5. **事件循环**：添加了`asyncio.run(run_crawler())`来启动异步事件循环
6. **异步等待**：在调用异步函数时添加了`await`关键字
7. **错误处理**：异步版本的错误处理更加简洁，直接使用异常抛出

这些变化使得爬虫能够并发处理多个请求，提高了爬取效率，特别是在网络I/O密集型任务中表现更优。