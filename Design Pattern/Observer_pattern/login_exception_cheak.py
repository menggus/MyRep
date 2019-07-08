from obs_pattern_framework import Observable, Observer
import time


class Account(Observable):
    """登录账号"""
    def __init__(self):
        super().__init__()
        self.__latesIp = dict()
        self.__latesRegion = dict()

    def  login(self, name, ip):
        # 这里还省略账户登录,这里模拟登录时的情况
        # 解析ip获取,地区信息
        region = self.__region(ip)
        # 判断地区信息是否在最近登录地区地址中
        if self.__islongdistance(name, region):
            obj = {
                "name": name,
                "ip": ip,
                "region": region,
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            }
            self.notify(obj)
        # 添加ip和地址
        self.__latesRegion[name] = region
        self.__latesIp[name] = ip


    def __region(self, ip):
        """
            通过ip地址,解析登录地点(这里是在模拟解析地区,项目中应该调用ip解析服务)
        :param ip: ip地址
        :return: None or region
        """
        ipReigon = {
            "101.47.18.9": "浙江省杭州市",
            "113.116.59.252": "广东省深圳市",
        }
        region = ipReigon.get(ip)

        return "" if region is None else region

    def __islongdistance(self, name, region):
        """
            计算本次登录与最近几次登录的地区差距(这里采用字符串匹配来模拟, 项目中应该调用地理信息相关的服务)

        :param name: 账户名
        :param region: 地区
        :return: bool
        """
        latesRegion = self.__latesRegion.get(name)

        return latesRegion is not None and latesRegion != region


class SmsSender(Observer):
    """短信发送"""

    def update(self, observable, obj):
        print("[短信发送]+{} 您好! 检测到您的账号登录异常.\n最近一次登录信息:\n \t登录地区:{}, IP:{}, 登录时间: {}".format(
            obj.get("name"),
            obj.get("region"),
            obj.get("ip"),
            obj.get("time")

        ))


class MailSender(Observer):
    """邮箱发送"""
    def update(self, observable, obj):
        print("[邮箱发送]+{} 您好! 检测到您的账号登录异常.\n最近一次登录信息:\n \t登录地区:{}, IP:{}, 登录时间: {}".format(
            obj.get("name"),
            obj.get("region"),
            obj.get("ip"),
            obj.get("time")

        ))


def main():
    account = Account()
    sms = SmsSender()
    mail = MailSender()
    account.add_observer(sms)
    account.add_observer(mail)

    account.login("tao", "101.47.18.9")

    account.login("tao", "113.116.59.252")


if __name__ == '__main__':
    main()






