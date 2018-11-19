"""
jieba添加自定义词或词库
"""
import jieba
str_text="李小福是创新办主任也是云计算方面的专家"
str_jing2=jieba.cut(str_text,cut_all=False)
print('add_word前:'+"/".join(str_jing2))
#添加自定义词
for i in ["创新办","云计算"]:#准备自定义词
    jieba.add_word(i)#动态添加自定义词
str_jing3=jieba.cut(str_text,cut_all=False)
print('add_word后:'+"/".join(str_jing3))
jieba.del_word("云计算")#动态删除词
str_jing3=jieba.cut(str_text,cut_all=False)
print('del_word后:'+"/".join(str_jing3))

"""
add_word前:李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家
add_word后:李小福/是/创新办/主任/也/是/云计算/方面/的/专家
del_word后:李小福/是/创新办/主任/也/是/云/计算/方面/的/专家
"""

s="李小福是创新办主任也是云计算方面的专家"
temp=jieba.cut(s)
print(",".join(temp))
#自定义词典（创新办 5 nt 云计算 10 n）
jieba.load_userdict(r"D:\Users\Administrator\PycharmProjects\test\dict.txt")
temp=jieba.cut(s)
print("修正词频前："+"/".join(temp))
# 可调节单个词语的词频，使其能（或不能）被分出来
jieba.suggest_freq("也是",tune=True)
temp=jieba.cut(s)
print("修正词频后："+"/".join(temp))
"""
修正词频前：李小福/是/创新办/主任/也/是/云计算/方面/的/专家
修正词频后：李小福/是/创新办/主任/也是/云计算/方面/的/专家
"""