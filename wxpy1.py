""" 
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

my_friend = bot.friends().search('梁云鹏')[0]
my_friend.send('顶')

@bot.register()
def print_others(msg):
    print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
    return '我不在'.format(msg.text, msg.type)
    
embed()  
"""

""" 
from wxpy import *
import math
import json
class bots:
    def __init__(self):
        pass
    def initBot(self):
        bot = Bot()
        my_friend = bot.friends();
        self.friendsArr=[]
        sexArr=['未知','男','女']
        for ff in my_friend:
            ffDict={}
            ffDict.update({'wxid':ff.wxid})
            ffDict.update({'city':ff.city})
            ffDict.update({'sex':sexArr[ff.sex]})
            ffDict.update({'isFriend':ff.is_friend.nick_name})
            ffDict.update({'nick_name':ff.nick_name})
            ffDict.update({'user_name':ff.user_name})
            ffDict.update({'province':ff.province})
            ffDict.update({'remark_name':ff.remark_name})
            self.friendsArr.append(ffDict)

    def setFriendsDataToJson(self,fileName):
        f=open(fileName,'w+')
        jstr=json.dumps(self.friendsArr)
        f.write(jstr)
    def getTheSexNum(self):
        unknown,male,female=0,0,0
        # print(self.friendsArr[0])
        # return
        for item in self.friendsArr:
            if item.get('sex')=='男':
                male+=1
            elif item.get('sex')=="女":
                female+=1
            else:
                unknown+=1
        print('count:'+str(len(self.friendsArr)),'男:'+str(male),'女:'+str(female))
        nan = str((male/len(self.friendsArr))*10)
        nv = str((female/len(self.friendsArr))*10)
        print('男性占比例:'+nan+'成','女性占比例:'+nv+'成')
botObj=bots()
botObj.initBot()
botObj.getTheSexNum() 
"""

from wxpy import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

bot= Bot()
fr_info=bot.friends()


pro_info={}
for fr in fr_info:
    if fr.city in pro_info.keys():
        pro_info[fr.city]+=1
    else: 
         pro_info[fr.city]=1

key_list = [key for key in pro_info]
print(key_list)

num_list = [pro_info for pro_info in pro_info]
print(num_list)
   
salary = key_list
group = num_list
plt.hist(salary, group, histtype='bar', rwidth=0.8)

plt.legend()

plt.xlabel('salary-group')
plt.ylabel('salary')

plt.title(u'直方图')

plt.show()
