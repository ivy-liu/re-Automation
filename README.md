
* 私有变量和方法


__private_attrs:两个下划线开头，生命该属性为私有，不能在类的外部被使用或直接访问。


在类内部的方法中使用：self.__private_attrs

个人觉得python的私有没有什么意义，规则存在，
但实际通过对象调用类，调用私有方法依然可以使用
```python
class Animal:
    def __heshui(self):
        print('动物，喝水')

    def test_heshui(self):
        self.__heshui()#调用类内部私有方法：self.__heshui()需要使用self

class Cat(Animal):
    def heshui(self):
        super()._Animal__heshui()
    # def cat_heshui(self):
    #     pass
new_cat=Cat()
# new_cat.__heshui()#报错 外部无法访问

new_cat.heshui()#运行正常，打印：动物，喝水

```





  