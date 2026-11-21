# 数据说明

社区服务需求、人员能力、时段与已确认安排的规划输入。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `demand.csv`

字段：`demand_id`、`grid_ref`、`service_code`、`requested_slot`、`urgency`、`confidence`。当前演练样本 4 条。

## `workers.csv`

字段：`worker_ref`、`skill`、`available_from`、`available_to`、`grid_ref`。当前演练样本 4 条。

## `commitments.csv`

字段：`commitment_id`、`demand_id`、`worker_ref`、`accepted_at`、`state`。当前演练样本 2 条。
