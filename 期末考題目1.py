class 蔬菜:
    #建構子以設定目前的蔬菜品種、價格、重量
    def __init__(目前的self, 輸入的蔬菜名稱, 輸入的蔬菜重量, 輸入的蔬菜單價):
        目前的self._蔬菜名稱 = 輸入的蔬菜名稱
        目前的self._蔬菜重量 = 輸入的蔬菜重量
        目前的self._蔬菜單價 = 輸入的蔬菜單價
  
    #計算蔬菜價格=蔬菜重量*蔬菜的單價
    def 計算蔬菜單價(目前的self):
        return 目前的self._蔬菜單價
    def 計算蔬菜重量(目前的self):
        return 目前的self._蔬菜重量
    def 計算蔬菜價格(目前的self):
        return 目前的self.計算蔬菜重量*目前的self.計算蔬菜單價
 
    #主函式
    def main(): 
        蔬菜物件1 = 蔬菜("水蓮", 300, 0.05)  #呼叫建構子，建立蔬菜物件1
        蔬菜物件2 = 蔬菜("空心菜", 500, 0.020) #呼叫建構子，建立蔬菜物件2
        蔬菜物件3 = 蔬菜("高麗菜", 1300, 0.015) #呼叫建構子，建立蔬菜物件3
        print(蔬菜物件1._蔬菜名稱) 
        print("價格=",蔬菜物件1._蔬菜重量*蔬菜物件1._蔬菜單價)     
        print("單價=",蔬菜物件1.計算蔬菜單價())
        print("重量=",蔬菜物件1.計算蔬菜重量())
        print("價格=",蔬菜物件1.計算蔬菜價格())    
        print(蔬菜物件2._蔬菜名稱) 
        print("價格=",蔬菜物件2._蔬菜重量*蔬菜物件2._蔬菜單價)     
        print("單價=",蔬菜物件2.計算蔬菜單價())
        print("重量=",蔬菜物件2.計算蔬菜重量())
        print("價格=",蔬菜物件2.計算蔬菜價格())
        print(蔬菜物件3._蔬菜名稱) 
        print("價格=",蔬菜物件3._蔬菜重量*蔬菜物件3._蔬菜單價)     
        print("單價=",蔬菜物件3.計算蔬菜單價())
        print("重量=",蔬菜物件3.計算蔬菜重量())
        print("價格=",蔬菜物件3.計算蔬菜價格()) 