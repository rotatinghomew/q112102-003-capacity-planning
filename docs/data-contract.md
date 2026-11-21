# 人力服务配置：资料契约

`demands` 是完整交付单位，`legs` 是同一需求的有序工序。每项工序要在需求时窗内连续实施；采用当地日期，时间为当天 00:00 后整数分钟。`roles` 用分号分隔，要由不同人员分别承担；第二道及后续工序的 `gap_min`、`gap_max` 是相对上道结束的允许分钟数（含端点）。同一工作人员同一时间不能参加两个活动；两个相邻服务之间要留驻点通行时间。两时段之间不可用的区域不能用于满足连续工序；一段可用时窗内的首末位置以表中驻点为准。技能 `revoked` 从记录日期起不可用于服务；一人可有多项技能。
`offers` 是人力增援情景，`scenario=base` 为现有人力。`commitments` 是已经发给住户并接受的人员安排，一道工序可分别登记几名人员；仅部分人员接受时，已接人员及时间仍是承诺，不代表整道工序有足够人员。带签认的变化在 `changes` 中追加。样例中 `C2` 在第一批计划之前，`C3`、`C4` 在后。时段左闭右开。`targets` 按完整需求量解释。

## 输入表

- `demands.csv`：`id`、`village`、`site`、`date`、`start`、`end`、`urgency`、`verified`
- `legs.csv`：`demand`、`leg`、`duration`、`roles`、`gap_min`、`gap_max`
- `skills.csv`：`worker`、`skill`、`state`、`date`
- `offers.csv`：`scenario`、`worker`、`date`、`start`、`end`、`home`
- `travel.csv`：`origin`、`destination`、`minutes`
- `targets.csv`：`village`、`min_tasks`
- `commitments.csv`：`id`、`demand`、`leg`、`worker`、`role`、`start`、`end`、`accepted_at`
- `changes.csv`：`id`、`action`、`subject`、`scope`、`at`
