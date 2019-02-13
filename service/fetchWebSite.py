
import requests
import json
import time


class CheckUrlJurisdiction(object):
    """
    实例初始化字段说明
    userapi: api后台登录账号
    passwdapi: api后台登录密码
    project_id: api后台需要检测项目Id
    self.api_count: api 数量
    self.api_list: 接口列表
    self.time: 运行花费时间
    """

    def __init__(self, userapi, passwdapi, project_id,apiurl):
        self.userapi = userapi
        self.passwdapi = passwdapi
        self.project_id = project_id
        self.api_count = 0
        self.api_list = []
        self.time = float()
        self.apiurl = apiurl
        self.api = requests.session()
        """api_login"""
        loginjson = {'email': self.userapi,
                     'password': self.passwdapi}
        loginheader = {'Content-Type': 'application/json;charset=UTF-8'}
        print("api后台登录状态:", self.api.post(url=self.apiurl + "/api/user/login", data=json.dumps(loginjson), verify=False,
                                          headers=loginheader).json().get("errmsg"))

    def geturlpath(self):
        """根据group_id获取对应模块id limit为每页模块条数"""
        print("正在检测发布系统遗漏的接口地址(本次程序检测所花费时间可能较长，请耐心等待)")
        starttime = time.clock()
        getid = {}
        thisJson = self.api.get(url=self.apiurl + "/api/interface/list?page=1&limit=20&project_id=37254", verify=False, params=getid).json()
        ids = thisJson.get("data").get(
            "list")
        for i in range(0, len(ids)):
            # self.get_path_by_id(ids[i].get("_id"))
            print(ids[i].get("_id"))
        timeend = time.clock()
        self.time = str("%.2f" % (timeend - starttime))

    """通过模块id找寻path"""

    def get_path_by_id(self, _id):
        """检测 每个接口的 内容"""
        details = self.api.get(self.apiurl + "/api/interface/get?id=%s" % _id,
                               verify=False).json()


#
# if __name__ == "__main__":
#     xiejiangpeng = CheckUrlJurisdiction("297229267@qq.com", "litong0522", 37254,'http://yapi.demo.qunar.com')
#     xiejiangpeng.geturlpath()