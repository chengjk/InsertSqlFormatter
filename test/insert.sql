
### Normal sql
-- origin
insert into `test`.`agent_user` ( `status`, `id`, `email`, `user_id`, `created`, `tel`, `modified`, `agent`) values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');
-- formated
insert into `test`.`agent_user` 
( `status` , `id`, `email`                   , `user_id` , `created`   , `tel`        , `modified`  , `agent`) values 
( '中文测试', '1' , 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');  

### With Function
-- origin
insert into `test`.`agent_user` ( `status`, `id`, `email`, `user_id`, `created`, `tel`, `modified`, `agent`) values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', now(), '150xxxx1256', now(), 'WF');
-- formated
insert into `test`.`agent_user` 
( `status` , `id`, `email`                   , `user_id` , `created`, `tel`        , `modified`, `agent`) values 
( '中文测试', '1' , 'chengxxxxxai@foxmail.com', '28950596', now()    , '150xxxx1256', now()     , 'WF');  

### Messy
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



### Without names
-- origin
insert into `test`.`agent_user` values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', 
	'28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');

-- formated
insert into `test`.`agent_user` values ( '中文测试', '1', 'chengxxxxxai@foxmail.com', '28950596', '2018-10-23', '150xxxx1256', '2018-10-23', 'WF');
