class 登機證:
    def __init__(目前的self, 輸入的旅客姓名, 輸入的登機證編號, 輸入的登機時間,輸入的登機門編號,輸入的座位位置,輸入的行李件數,輸入的行李ID):
        目前的self._旅客姓名 = 輸入的旅客姓名
        目前的self._登記證編號 = 輸入的登機證編號
        目前的self._登機時間 = 輸入的登機時間
        目前的self._登機門編號 = 輸入的登機門編號
        目前的self._座位位置 = 輸入的座位位置
        目前的self._行李件數 = 輸入的行李件數
        目前的self._行李ID = 輸入的行李ID

    def 目前的旅客姓名(目前的self):
        return 目前的self._旅客姓名
    def 目前的登機證編號(目前的self):
        return 目前的self._登記證編號
    def 目前的登機時間(目前的self):
        return 目前的self._登機時間
    def 目前的登機門編號(目前的self):
        return 目前的self._登機門編號
    def 目前的座位位置(目前的self):
        return 目前的self._座位位置
    def 目前的行李件數(目前的self):
        return 目前的self._行李件數
    def 目前的行李ID(目前的self):
        return 目前的self._行李ID
    
    def 修改姓名(self, 新姓名):
        self.旅客姓名 = 新姓名
    def 修改登機證編號(self, 新登機證編號):
        self.登機證編號 = 新登機證編號
    def 修改登機時間(self, 新登機時間):
        self.登機時間 = 新登機時間
    def 修改姓名(self, 新行李件數):
        self.行李件數 = 新行李件數
    def 修改姓名(self, 新行李ID):
        self.行李ID = 新行李ID
    
    def main():
        登機證物件1=登機證(輸入的旅客姓名="熊大",輸入的登機證編號="GG 0051",輸入的登機時間="00:50",輸入的登機門編號="G2",輸入的座位位置="45A",輸入的行李件數="1",輸入的行李ID="TK888")
        登機證物件2=登機證(輸入的旅客姓名="熊二",輸入的登機證編號="GB 0044",輸入的登機時間="01:00",輸入的登機門編號="B6",輸入的座位位置="34H",輸入的行李件數="2",輸入的行李ID="MU112")
        登機證物件3=登機證(輸入的旅客姓名="胖達",輸入的登機證編號="GA 0078",輸入的登機時間="06:00",輸入的登機門編號="A5",輸入的座位位置="28E",輸入的行李件數="1",輸入的行李ID="AS320")
        print(登機證物件1.目前的旅客姓名())
        print("登記證編號:",登機證物件1.目前的登機證編號())
        print("登記時間:",登機證物件1.目前的登機時間())
        print("登記門編號:",登機證物件1.目前的登機門編號())
        print("座位位置:",登機證物件1.目前的座位位置())
        print("行李件數:",登機證物件1.目前的行李件數())
        print("行李ID:",登機證物件1.目前的行李ID())

        # 使用副函数修改姓名、登機證編號、登機時間、登機門編號、座位位置、行李件數、行李ID
        登機證物件1.修改姓名(新姓名="大熊")
        登機證物件1.修改登機證編號(新登機證編號="EQ 1123")
        登機證物件1.修改登機時間(新登機時間="05:00")
        登機證物件1.修改姓名(新登機門編號="R3")
        登機證物件1.修改姓名(新座位位置="54B")
        登機證物件1.修改姓名(新行李件數="2")
        登機證物件1.修改姓名(新行李ID="TF65")        
        # 显示修改后的姓名
        print("修改后的姓名:", 登機證物件1.旅客姓名)


        print(登機證物件2.目前的旅客姓名())
        print("登記證編號:",登機證物件2.目前的登機證編號())
        print("登記時間:",登機證物件2.目前的登機時間())
        print("登記門編號:",登機證物件2.目前的登機門編號())
        print("座位位置:",登機證物件2.目前的座位位置())
        print("行李件數:",登機證物件2.目前的行李件數())
        print("行李ID:",登機證物件2.目前的行李ID())

        print(登機證物件3.目前的旅客姓名())
        print("登記證編號:",登機證物件3.目前的登機證編號())
        print("登記時間:",登機證物件3.目前的登機時間())
        print("登記門編號:",登機證物件3.目前的登機門編號())
        print("座位位置:",登機證物件3.目前的座位位置())
        print("行李件數:",登機證物件3.目前的行李件數())
        print("行李ID:",登機證物件3.目前的行李ID())


class 行李:
    def __init__(目前的self,輸入的行李ID,輸入的行李重量,輸入的行李出發機場,輸入的行李目的地機場,輸入的行李所屬旅客姓名):
        目前的self._行李ID = 輸入的行李ID
        目前的self._行李重量 = 輸入的行李重量
        目前的self._行李出發機場 = 輸入的行李出發機場
        目前的self._行李目的地機場 = 輸入的行李目的地機場
        目前的self._行李所屬旅客姓名 = 輸入的行李所屬旅客姓名   
