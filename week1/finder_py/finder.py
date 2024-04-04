from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=dict({'/*': {'origins': '*'}}))

@app.route('/getEmps', methods=['GET'])
def getEmps():
    emps=[
        {"name_en":"michael","name_cn":"尚亚辉","email":"michael.shang@sanofi.com"},
        {"name_en":"forrest","name_cn":"苏永佳","email":"forrest.su@sanofi.com"},
        {"name_en":"ashin","name_cn":"黄斌朕","email":"ashin.huang@sanofi.com"},
        {"name_en":"ben","name_cn":"刘申奥","email":"ben1.liu@sanofi.com"},
        {"name_en":"cathy","name_cn":"刘鸣","email":"cathy2.liu@sanofi.com"},
        {"name_en":"eileen","name_cn":"荀欣","email":"eileen.xun@sanofi.com"},
        {"name_en":"gan","name_cn":"卢干","email":"gan.lu@sanofi.com"},
        {"name_en":"guotong","name_cn":"宋国通","email":"guotong.song@sanofi.com"},
        {"name_en":"hanlin","name_cn":"孙汉霖","email":"hanlin.sun@sanofi.com"},
        {"name_en":"huan","name_cn":"陈欢","email":"huan3.chen@sanofi.com"},
        {"name_en":"jenny","name_cn":"杨靖","email":"jenny1.yang@sanofi.com"},
        {"name_en":"jessie","name_cn":"朱姣姣","email":"jessie.zhu@sanofi.com"},
        {"name_en":"lakin","name_cn":"金超慧","email":"lakin.jin@sanofi.com"},
        {"name_en":"lei","name_cn":"钟磊","email":"lei2.zhong@sanofi.com"},
        {"name_en":"lige","name_cn":"常丽鸽","email":"lige.chang@sanofi.com"},
        {"name_en":"lin","name_cn":"张麟","email":"lin9.zhang@sanofi.com"},
        {"name_en":"ling","name_cn":"景玲","email":"ling.jing@sanofi.com"},
        {"name_en":"miya","name_cn":"文雅","email":"miya.wen@sanofi.com"},
        {"name_en":"shangfei","name_cn":"王上非","email":"shangfei.wang@sanofi.com"},
        {"name_en":"tony","name_cn":"孙俊彦","email":"tony.sun@sanofi.com"},
        {"name_en":"xing","name_cn":"黄星","email":"xing.huang@sanofi.com"},
        {"name_en":"yu","name_cn":"谭宇","email":"yu.tan@sanofi.com"},
    ]
    return emps

if __name__ == '__main__':
    app.run()