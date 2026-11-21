# 记录格式

求助记录以 id、task、stage、goal、request、check、result 描述任务阶段、求助及后续检查。result 的 unknown 不等于失败。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
