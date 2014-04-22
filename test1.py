#coding=utf-8
'''
本程序演示的launch函数 core组件的用法.

1.launch函数的用法
  *如何向应用程序中传递命令行参数
  *

2.core组件的使用
  *如何向core中注册组件，以及如何使用已经注册的组件
  *使用log功能，进行程序调试

'''

from pox.core import core

#获得log对象
log = core.getLogger()

class MyComponent ():
  '''
  这是一个测试组件，被用于注册到core中
  '''
  def sayhello(self):
    '''
    这是一个测试方法，用户向屏幕上打印Hello，World字符串
    '''
    print "Hello, world!"


def launch(name = "My Default Name"):
  '''
  这是应用程序开始的地方：launch()方法
  '''
  print "The name is ", name    #输出调试信息时推荐使用log对象
  log.info("此信息来自log.info()方法")
  #log.debug("此信息来自log.debug()方法",'aaaa')
  log.error("此信息来自log.error()方法")
  print dir(log)
  myComponent = MyComponent()
  #注册组件
  core.register("myComponent",myComponent)
  core.myComponent.sayhello()
