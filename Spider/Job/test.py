str = "上海-闵行区  |  2年经验  |  大专  |  招若干人  |  06-20发布"
a = str.split()
print(a)
# 去掉 句子中的\xa0\xa0
str = "".join(str.split())

print(str)

import re

str1 = """<div class="bmsg job_msg inbox">
<p>岗位职责：</p><p>  </p>1、负责公司产品微服务组件的开发。<div>2、对接口编写自动化测试用例。<br><p>3、负责公司应用系统的日常维护。</p><p>任职要求：</p><p>1、专科及以上学历。</p><p>2、学习能力强。</p><p>3、团队沟通协作好。</p><p>                </p><p>4、有一定Python基础。</p><p>福利待遇：</p><p>1、带薪年假，七险一金，项目薪酬</p><p>2、发展空间大，扁平管理</p><p>3、员工旅游，周末双休</p><p>4、交通便利</p><p>5、早九晚五点半</p></div>						
<div class="mt10">"""
a = re.findall(r'<div class="bmsg job_msg inbox">.*?<div class="mt10">', str1, re.S)
print(a)
a = re.sub(r"<.*?>", "", a[0])
print(a)