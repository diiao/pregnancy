from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/article/',methods = ['POST'])
def article():
    data = request.get_json()
    list = data.get('list')
    if list == 1:
        data = [
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%A6%8A%E5%A8%A0%E6%97%85%E7%A8%8B.png",
                "name": "妊娠旅程",
                "hits" :0,
                "projects": [
                    {
                        "title": "生命起源及胎儿生长发育",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.1.1.md"
                    },
                    {
                        "title":"孕期常见症状及处理",
                        "type":"text",
                        "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/1.1.2.md"
                    },
                    {
                        "title":"孕期常见异常症状的识别及处理",
                        "type":"text",
                        "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/1.1.3.md"
                    }
                ]
            },
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E6%9C%9F%E5%BE%85%E4%B8%AD%E7%9A%84%E5%A6%88%E5%A6%88.png",
                "name": "期待中的妈妈：正常分娩",
                "hits": 0,
                "projects": [
                    {
                        "title": "怀孕后的情绪反应",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.2.1.md"
                    },
                    {
                        "title": "临产先兆早知道",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.2.2.md"
                    },
                    {
                        "title": "产痛是怎么回事？",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.2.3.md"
                    }
                ]
            },
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%88%86%E5%A8%A9%E7%8E%AF%E5%A2%83.png",
                "name": "分娩环境",
                "hits": 0,
                "projects": [
                    {
                        "title": "产妇何时可以进入待产房和产房",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.3.1.md"
                    },
                    {
                        "title": "产妇可以要求家人或朋友陪产吗？",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/1.3.2.md"
                    }
                ]
            }
        ]
    elif list == 2:
        data = [
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E4%BA%A7%E5%A6%87%E5%88%86%E5%A8%A9%E6%95%85%E4%BA%8B.png",
                "name": "分享妇女分娩故事",
                "hits": 0,
                "projects": [
                    {
                        "title": "无医学指征计划剖宫产，最后成功自然分娩",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.1.1.md"
                    },
                    {
                        "title": "胎膜早破需要剖宫产吗？",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.1.2.md"
                    },
                    {
                        "title": "站着生产更顺利吗？无保护分娩是真的吗？",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.1.3.md"
                    }
                ]
            },
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%88%86%E5%A8%A9%E5%87%86%E5%A4%87%E5%8F%8A%E9%95%87%E7%97%9B.png",
                "name": "分娩准备及镇痛",
                "hits": 0,
                "projects": [
                    {
                        "title": "去医院应该准备的物品清单",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.2.1.md"
                    },
                    {
                        "title": "缓解宫缩疼痛小妙招",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.2.2.md"
                    },
                    {
                        "title": "如何缓解分娩的痛",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/2.2.3.md"
                    }
                ]
            },
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%88%86%E5%A8%A9%E8%BF%87%E7%A8%8B.png",
                "name": "分娩过程",
                "hits": 0,
                "projects": [
                    {
                        "title": "第一产程",
                        "type": "video",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E7%AC%AC%E4%B8%80%E4%BA%A7%E7%A8%8B.mp4"
                    },
                    {
                        "title": "第二产程",
                        "type": "video",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E7%AC%AC%E4%BA%8C%E4%BA%A7%E7%A8%8B.mp4"
                    },
                    {
                        "title": "第三产程",
                        "type": "video",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E7%AC%AC%E4%B8%89%E4%BA%A7%E7%A8%8B.mp4"
                    }
                ]
            }
        ]
    elif list == 3:
        data = [
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%91%BC%E5%90%B8%E6%8A%80%E5%B7%A7%E9%87%8D%E5%BB%BA.png",
                "name": "呼吸技巧重建",
                "hits": 0,
                "projects": [
                    {
                        "title": "拉玛泽呼吸减痛法",
                        "type": "text",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/3.1.1.md"
                    },
                    {
                        "title": "拉玛泽呼吸",
                        "type": "video",
                        "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E6%8B%89%E7%8E%9B%E6%B3%BD%E5%91%BC%E5%90%B8%E8%A7%86%E9%A2%91.mp4"
                    }
                ]
            },
            {
                "imgUrl": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E9%9F%B3%E4%B9%90%E6%94%BE%E6%9D%BE%E7%96%97%E6%B3%95.png",
                "name": "音乐放松疗法",
                "hits": 0,
                "projects": [
                    {
                        "title": "中国古典音乐",
                        "type":"video",
                        "videos": [
                            {
                                "title": "夕阳萧鼓",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%A4%95%E9%98%B3%E7%AE%AB%E9%BC%93.mp4"
                            },
                            {
                                "title":"平湖秋月",
                                "type":"video",
                                "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%B9%B3%E6%B9%96%E7%A7%8B%E6%9C%88.mp4"
                            },
                            {
                                "title":"广陵散",
                                "type":"video",
                                "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%B9%BF%E9%99%B5%E6%95%A3.mp4"
                            },
                            {
                                "title":"春江花月夜",
                                "type":"video",
                                "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/%E6%98%A5%E6%B1%9F%E8%8A%B1%E6%9C%88%E5%A4%9C.mp4"
                            },
                            {
                                "title": "梅花三弄",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E6%A2%85%E8%8A%B1%E4%B8%89%E5%BC%84.mp4"
                            }
                        ]
                    },
                    {
                        "title": "世界经典名曲",
                        "type": "video",
                        "videos": [
                            {
                                "title": "安妮的仙境",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%AE%89%E5%A6%AE%E7%9A%84%E4%BB%99%E5%A2%83.mp4"
                            },
                            {
                                "title":"平湖秋月",
                                "type":"video",
                                "url":"https://qiniu.freespace.yuxue0824.com/pregnancy/%E5%B9%B3%E6%B9%96%E7%A7%8B%E6%9C%88.mp4"
                            },
                            {
                                "title": "清晨",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E6%B8%85%E6%99%A8.mp4"
                            }
                            ,
                            {
                                "title": "秋天的落叶",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E7%A7%8B%E5%A4%A9%E7%9A%84%E8%90%BD%E5%8F%B6.mp4"
                            },
                            {
                                "title": "绿野仙踪",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E7%BB%BF%E9%87%8E%E4%BB%99%E8%B8%AA.mp4"
                            },
                            {
                                "title": "雪之梦",
                                "type":"video",
                                "url": "https://qiniu.freespace.yuxue0824.com/pregnancy/%E9%9B%AA%E4%B9%8B%E6%A2%A6.mp4"
                            },
                        ]
                    }
                ]
            },
        ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=6001)
