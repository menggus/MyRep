import itchat

"""
    登录微信,并爬去好友信息
"""

class Wechat:

    def __init__(self):
        # 登录方式,扫码
        self.mychat = itchat.auto_login(hotReload=True)


    def get_friends(self):
        # 好友信息,返回一个好友列表
        friends = itchat.get_friends(update=True)

        return friends

    def parse_friends(self, i):
        """
            解析数据
        :param data: info
        :return: a dict
        """
        if i is None:
            return

        info = dict()
        info["Name"] = i.get("NickName")  # 昵称
        info["Rename"] = i.get("RemarkName")  # 备注昵称
        info["Sex"] = i.get("Sex")  # 性别
        info["Province"] = i.get("Province")  # 省份
        info["City"] = i.get("City")  # 城市
        info["Signature"] = i.get("Signature")  # 个性签名
        info["AttrStatus"] = i.get("AttrStatus")  # 点赞数

        return info


    def save(self, info):

        # 写入文件
        with open("friends.csv", "a+", encoding="utf-8") as f:
            f.write("{},{},{},{},{},{},{}\n".format(info.get("Name"),
                                                  info.get("Rename"),
                                                  info.get("Sex"),
                                                  info.get("Province"),
                                                  info.get("City"),
                                                  info.get("Signature"),
                                                  info.get("AttrStatus")
                                                  ))
        print("{}:写入-------------OK".format(info.get("Name")))

    def close(self):
        # 退出登录
        itchat.logout()

    def run(self):
        # 获取数据
        data = self.get_friends()
        self.close()
        # 解析数据
        for i in data:
            info = self.parse_friends(i)
            # 保存数据
            self.save(info)


if __name__ == '__main__':
    mychat = Wechat()
    mychat.run()

