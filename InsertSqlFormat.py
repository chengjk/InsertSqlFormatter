import sublime
import sublime_plugin
import logging
import re

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
#default 1.8, override by config
chineseWordLen=1.8

class InsertSqlFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		log.debug("starting format insert sql")
		settings = sublime.load_settings("config.sublime-settings")
		chineseWordLen=settings.get("chinese_word_lenght")
		log.debug("load config")
		log.info("chinese_word_lenght:"+'{:2.1f}'.format(chineseWordLen))
		regions=self.getSelectRegion()
		for region in regions:
			result=self.formatRegion(region)
			self.view.replace(edit, region, result)

	def getSelectRegion(self):
		has_selection = len(self.view.sel()) and self.view.sel()[0].size()
		if has_selection:
			log.debug("selected")
			regions = self.view.sel()
		else:
			log.debug("not select")
			regions = [sublime.Region(0, self.view.size())]
		return regions


	def formatRegion(self,region):
		inputStr=self.view.substr(region)
		inputStr=inputStr.replace("\n","")
		inputStr=inputStr.replace("\t","")
		#replace mutil space to single space.
		inputStr=" ".join(inputStr.split())
		sqls=inputStr.split(";")
		log.debug("*********** origin sql list **********")
		log.debug(sqls)
		log.debug("*********** origin sql list end **********")
		result=""
		for s in sqls:
			formated=self.formatSql(s)
			if formated:
				result=result+formated+";\n"
		return result
		
	def formatSql(self,insertSql):
		if ""==insertSql:
			return None
		
		text=insertSql
		sqlObj=self.parseSql(text)
			
		# retrun if without names 
		if not "names" in sqlObj:
			log.info("without field name.")
			# log.info(text)
			log.info(sqlObj)
			return text

		names=sqlObj["names"].split(",")
		values=sqlObj["values"].split(",")
		#keep name and value in the same len
		finalNames=[]
		finalValues=[]

		maxFieldLen=max(len(names),len(values))
		for i in range(maxFieldLen):
			name=""
			value=""
			if i>=len(names):
				# set default field name
			    name="undefined"
			else:
				name=names[i]
			if i>=len(values):
				# set default field value
				value="null"
			else:
				value=values[i]
			
			# get max len
			lenght=max(self.len(name),self.len(value))
			if lenght==self.len(name):
				# keep lenght with space
				value=self.strAppend(value," ",lenght-self.len(value))
			else:
				# keep lenght with space
				name=self.strAppend(name," ",lenght-self.len(name))

			finalNames.append(name)
			finalValues.append(value)
		fieldLen=len(finalNames)

		#build result
		result=sqlObj["header"]+"\n ("
		## append names
		for i in range(fieldLen):
			fname=finalNames[i]
			result=result+fname
			if i<fieldLen-1:
				result=result+","
		result=result+") values \n ("

		## append values
		for i in range(fieldLen):
			fvalue=finalValues[i]
			result=result+fvalue
			if i<fieldLen-1:
				result=result+","
		result=result+")"
		return result

	def parseSql(self,text):
		i=text.index("(")
		header=text[0:i]
		log.debug("========header==========")
		log.debug(header)
		body=text[i:]
		p=re.compile("[\s]*values[\s]*",re.IGNORECASE)
		lines=p.split(body)

		if len(lines)==2:
			names=lines[0]
			values=lines[1]
			log.debug("========names==========")
			# remote first and last ()
			names=names.strip()[1:len(names)-1];
			log.debug(names)
			log.debug("========values==========")
			# remote first and last ()
			values=values.strip()[1:len(values)-1];
			log.debug(values)
			log.debug("======== end ==========")
			return {"header":header,"names":names,"values":values}
		else:		
			values=lines[0]
			log.debug("values:"+values)
			return {"header":header,"values":values}

	def strAppend(self,text,char,n):
		for i in range(int(n)):
			text=text+char
		return text

	def len(self,str):
		result=0
		for ch in str:
			if '\u4e00' <= ch <= '\u9fff':
				result=result+chineseWordLen
			else:
				result=result+1
		return result;
