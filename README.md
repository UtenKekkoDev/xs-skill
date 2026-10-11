# 中文短篇小说写作 Skill

用于中文短篇网文和番茄短故事的创作、续写、全文大修与逐章精修，也可用于现有长篇的章节修订。

默认采用冷峻、快节奏的文风，可按要求调整。重点检查具体冲突、人物动机、合理反转、伏笔回收、章首悬念和章末钩子。

## 使用

将整个仓库文件夹放到个人 skills 目录，并将文件夹命名为 `short-fiction-writing`。

Windows PowerShell 示例（目标目录应尚不存在）：

```powershell
git clone https://github.com/UtenKekkoDev/xs-skill.git "$env:USERPROFILE/.codex/skills/short-fiction-writing"
```

调用示例：

> 用 $short-fiction-writing，按我提供的故事架构写一篇 11000–12000 字的小说。

> 用 $short-fiction-writing，对原稿逐章精修，保留结局，修正逻辑，强化章首悬念与章末钩子。

## 文件

- [SKILL.md](SKILL.md)：任务范围、写作流程与交付检查。
- [写作方法](references/writing-methods.md)：故事、人物、节奏、反转及语言。
- [修订检查](references/revision.md)：时间线、知识边界、规则、道具与伏笔。
- [番茄官方课堂补充](references/fanqie-official-guidance.md)：6 篇官方课程的来源与适用方法。
- [历史专项参考](references/historical-columbus.md)：西方题材与历史哥伦布计划资料。
- `references/source-documents/`：两份原始写作参考文档。
- `scripts/count_words.py`：仅正文文本的字数检查。
- `agents/openai.yaml`：名称、简介与默认调用提示。

## 字数检查

先将正文保存为 UTF-8 文本，排除书名、章节标题和说明，再运行：

```text
python scripts/count_words.py body.txt --min 11000 --max 12000
```

默认计算字母和数字字符数，包含汉字，排除标点与空白。上下限按实际任务调整；目标范围外返回退出码 1。

## 来源与适用边界

整理自原始写作参考文档、历史修订要求和番茄官方公开写作课堂。官方参考的检索日期为 2026 年 10 月 11 日，链接见对应参考文件。

当前用户要求优先。固定章数、字数比例和案例套路均不是普遍要求；历史投稿活动的日期与条件不代表现行规则。本 skill 不承诺流量、签约或收益。
