# InsertSqlFormatter
Sublime 3 Text plugin.  format inset sql, align field names and values with space. 


## Getting Start

1. context-menu/format insert sql
2. commands: `ctrl+shift+p`, search `format sql`
3. hotkey:`ctrl+alt+l`

## Feature

- 格式化选择区域或全部。选择后，只格式化选择区域，反之格式化全部。
- 支持多个选区。
- 一个选区支持多个sql。

只能格式化正确的 insert sql，sql错误时会无法执行。


## Config
`{Package}/InsertSqlFormatter/config.sublime-settings`
中文长度，默认1.8。对齐效果比较好。应设置为常用字体的中文字宽比例。



## Effect

### Normal sql

```sql
-- origin
insert into `test`.`agent_user` ( `status`, `id`, `email`, `user_id`, `created`, `tel`, `modified`, `agent`) values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');

-- formated
insert into `test`.`agent_user` 
( `status` , `id`, `email`                   , `user_id` , `created`   , `tel`        , `modified`  , `agent`) values 
( '中文测试', '1' , 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');  
```


### With Function
```sql
-- origin
insert into `test`.`agent_user` ( `status`, `id`, `email`, `user_id`, `created`, `tel`, `modified`, `agent`) values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', now(), '150xxxx1256', now(), 'WF');
-- formated
insert into `test`.`agent_user` 
( `status` , `id`, `email`                   , `user_id` , `created`, `tel`        , `modified`, `agent`) values 
( '中文测试', '1' , 'chengxxxxxai@foxmail.com', '28950596', now()    , '150xxxx1256', now()     , 'WF');  

```

### Messy

```sql
-- origin
insert into `test`.`agent_user` 
	( `status`, `id`, `email`, `user_id`, `created`,
	 `tel`, `modified`, `agent`) values ( '中文测试', 
	 '1', 'chengxxxxxai@foxmail.com',
	  '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');

-- formated
insert into `test`.`agent_user` 
( `status` , `id`, `email`                   , `user_id` , `created`   , `tel`        , `modified`  , `agent`) values 
( '中文测试', '1' , 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');  

```

### Without Names

```sql
-- origin
insert into `test`.`agent_user` values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', 
	'28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');

-- formated
insert into `test`.`agent_user` values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');

```
