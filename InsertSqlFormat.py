import sublime
import sublime_plugin
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
#default 1.8, override by config
chineseWordLen=1.8

class InsertSqlFormatCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		log.debug("starting")

		settings = sublime.load_settings("config.sublime-settings")
		chineseWordLen=settings.get("chinese_word_lenght")
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
		inputStr=self.view.substr(region)+"\n"
		#todo inputStr could be mutil sql.
		# sqls=inputStr.split(";")
		# result=""
		# for s in sqls:
		# 	if not s:
		# 		log.debug(s)
		# 		result=result+self.formatSql(s+";")
		# return result
		return self.formatSql(inputStr)


	def formatSql(self,insertSql):
		# inputStr=self.view.substr(region)+"\n"
		text=insertSql.replace("\n","")
		text=text.replace("\t","")
		#replace mutil space to single space.
		text=" ".join(text.split())
		lines=text.split("(")
		if len(lines)<3:
			log.info("without field name.")
			return text

		names=lines[1].split(",")
		values=lines[2].split(",")

		#keep name and value in the same len
		finalNames=[]
		finalValues=[]
		index=0
		for name in names:
			value=values[index]
			lenght=max(self.len(name),self.len(value))
			if lenght==self.len(name):
				value=self.strAppend(value," ",lenght-self.len(value))
			else:
				name=self.strAppend(name," ",lenght-self.len(name))

			finalNames.append(name)
			finalValues.append(value)
			index=index+1
		fieldLen=len(finalNames)

		#build result
		result=lines[0]+"\n("
		## append names
		for i in range(fieldLen):
			fname=finalNames[i]
			result=result+fname
			if i<fieldLen-1:
				result=result+","
		result=result+"\n("
		## append values
		for i in range(fieldLen):
			fvalue=finalValues[i]
			result=result+fvalue
			if i<fieldLen-1:
				result=result+","
		return result+"\n"

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




