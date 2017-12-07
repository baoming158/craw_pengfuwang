import json

import itchat


def loginCallback():
    print("***登录成功***")

def exitCallback():
    print("***已退出***")

def login():
    itchat.auto_login(hotReload=True, enableCmdQR=2, loginCallback=loginCallback,
                      exitCallback=exitCallback)  # 首次扫描登录后后续自动登录

def callback(ch, method, properties, body):
    itchat.auto_login(hotReload=True, enableCmdQR=2)  # 首次扫描登录后后续自动登录
    users = itchat.search_friends(name='徐武强')  # 使用备注名来查找实际用户名
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    # 获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    data = body.decode("utf-8")
    result = json.loads(data)
    img_url = result['img_url']
    title = result['title']
    itchat.send(title, toUserName=userName)
    itchat.send_image("../"+img_url, toUserName=userName)


if __name__ == '__main__':
    callback()
