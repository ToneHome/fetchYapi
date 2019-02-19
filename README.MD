技术栈

​	Python 3.5

​	Django1.11.8

​	mysql 3.5



接口列表

/api/fetchApi

获取 Yapi项目的分类

方式：POST

参数

| parmas       | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| apiBaseUrl   | Yapi 的 主域名 （测试环境为：http://yapi.demo.qunar.com）    |
| apiProjectId | Yapi 项目的 id  http://yapi.demo.qunar.com/project/**37254**/interface/api |
| username     | Yapi系统的账号                                               |
| pssword      | 密码                                                         |

返回

| response | 描述     |
| -------- | -------- |
| list     | 分类列表 |





/api/getApiTree

获取 每个分类下的 接口

方式 POST

参数

| parmas       | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| apiBaseUrl   | Yapi 的 主域名 （测试环境为：http://yapi.demo.qunar.com）    |
| apiProjectId | Yapi 项目的 id  http://yapi.demo.qunar.com/project/**37254**/interface/api |
| username     | Yapi系统的账号                                               |
| pssword      | 密码                                                         |
| catList      | 重命名之后的 分类列表                                        |

返回

| response | 描述                           |
| -------- | ------------------------------ |
| list     | 返回分类下的接口，组成的树结构 |

