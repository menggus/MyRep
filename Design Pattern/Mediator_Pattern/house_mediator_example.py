class HouseInfo:
    """房屋信息类"""

    def __init__(self, area, price, hasWindow, hasBashroom, hasKitchen, address, owner):
        self.__area = area
        self.__price= price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBashroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner.get_name()

    def get_address(self):
        return self.__address

    def get_owner(self):

        return self.__owner

    def show_info(self):

        print("房源信息--面积:{} ㎡;  价格:{} Rmb;  窗户:{};  浴室:{};  厨房:{};  地址:{};  房东:{};".format(
            self.__area,
            self.__price,
            "有" if self.__hasWindow else "无",
            self.__hasBathroom,
            "有" if self.__hasKitchen else "无",
            self.__area,
            self.__owner,
        ))


class HouseOwner:
    """房东类"""

    def __init__(self, name):
        self.__name = name
        self.__houseinfo = None

    def get_name(self):

        return self.__name

    def set_houseinfo(self, area, price, hasWindow, hasBashroom, hasKitchen, address):
        self.__houseinfo = HouseInfo(area, price, hasWindow, hasBashroom, hasKitchen, address, self)

    def pubulish_houseinfo(self, agency):
        """
            发布房源
        :param agency:  代理,中介
        :return:
        """
        agency.add_houseinfo(self.__houseinfo)
        print(f"{self.get_name()} 在{agency.get_name()} , 发布房源信息.......")
        self.__houseinfo.show_info()


class HouseAgency:
    """中介"""

    def __init__(self, name):
        self.__name = name
        self.__houseinfos = []

    def get_name(self):

        return self.__name

    def add_houseinfo(self, houseinfo):

        self.__houseinfos.append(houseinfo)

    def remove_houseinfo(self, houseinfo):
        for info in self.__houseinfos:
            if info == houseinfo:
                self.__houseinfos.remove(info)

    def search_houseinfo(self, description):
        """
            针对用户描述,转化搜索关键词
        :param description: 描述
        :return:
        """
        #　省略
        return description

    def get_match_houseinfo(self, searchkeyswords):
        """匹配关键词查找房源"""
        # 省略,直接输出全部房源
        print("{} 为您找到如下合适房源:".format(self.get_name()))

        for info in self.__houseinfos:
            print(info.show_info())

        return self.__houseinfos

    def sign_contract(self, houseinfo, year):

        print(f"签订合同: 甲方:{self.get_name()} 与 乙方:{houseinfo.get_owner()} 签订合同, 合同期限:{year}年. 允许甲方使用和转租.")

    def sign_contracts(self, year):
        for i in self.__houseinfos:
            self.sign_contract(i, year)


class Customer:
    """租户"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):

        return self.__name

    def find_house(self, description, agency):
        print(f"{agency.get_name()} 我想找一个 {description} 这样的房子.")

        return agency.get_match_houseinfo(agency.search_houseinfo(description))

    def see_house(self, houseinfo):
        """现场查看房子"""
        # 省略
        print("现场看房......")
        index = len(houseinfo) - 1
        return houseinfo[index]

    def sign_contract(self, houseinfo, agency, year):

        print(f"签订合同: 甲方:{self.get_name()} 与 乙方:{agency.get_name()} 针对房屋:{houseinfo.get_address()} 签订合同, "
              f"合同期限:{year}年. 允许甲方使用和转租.")


def main():
    # 房屋中介
    zf = HouseAgency("租房网")

    # 房东1
    owner1 = HouseOwner("张三")
    owner1.set_houseinfo(30, 1500, 1, "独立卫生间", 1, "宝安小区")
    owner1.pubulish_houseinfo(zf)

    # 房东2
    owner2 = HouseOwner("李四")
    owner2.set_houseinfo(80, 2500, 1, "独立卫生间", 1, "南山小区")
    owner2.pubulish_houseinfo(zf)

    # 房东3
    owner1 = HouseOwner("王五")
    owner1.set_houseinfo(20, 500, 0, "公共卫生间", 0, "龙华小区")
    owner1.pubulish_houseinfo(zf)

    print("-"*100)

    # 租房客
    tony = Customer("tony")
    houseinfo = tony.find_house("50平米, 1500元, 要有独立卫生间,窗户,触厨房", zf)

    print("正在查看房源信息......")
    print("找到中意房源......")

    # 现场看房
    house = tony.see_house(houseinfo)

    # 签订合同
    tony.sign_contract(house, zf, 3)


if __name__ == '__main__':
    main()






















