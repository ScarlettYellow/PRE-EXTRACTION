from __future__ import print_function, unicode_literals
import json
import requests


SUMMARY_URL = 'http://api.bosonnlp.com/summary/analysis'
# 注意：在测试时请更换为您的API Token
headers = {'X-Token': 'rgqjRw1X.18655.95OIK0ANhha4'}

source = {
    'not_exceed': 0,
    'percentage': 0.2,
    'title': '',
    'content': (
        '腾讯科技讯（刘亚澜）10月22日消息，'
        '前优酷土豆技术副总裁黄冬已于日前正式加盟芒果TV，出任CTO一职。'
        '资料显示，黄冬历任土豆网技术副总裁、优酷土豆集团产品技术副总裁等职务，'
        '曾主持设计、运营过优酷土豆多个大型高容量产品和系统。'
        '此番加入芒果TV或与芒果TV计划自主研发智能硬件OS有关。'
        '今年3月，芒果TV对外公布其全平台日均独立用户突破3000万，日均VV突破1亿，'
        '但挥之不去的是业内对其技术能力能否匹配发展速度的质疑，'
        '亟须招揽技术人才提升整体技术能力。'
        '芒果TV是国内互联网电视七大牌照方之一，之前采取的是“封闭模式”与硬件厂商预装合作，'
        '而现在是“开放下载”+“厂商预装”。'
        '黄冬在加盟土豆网之前曾是国内FreeBSD（开源OS）社区发起者之一，'
        '是研究并使用开源OS的技术专家，离开优酷土豆集团后其加盟果壳电子，'
        '涉足智能硬件行业，将开源OS与硬件结合，创办魔豆智能路由器。'
        '未来黄冬可能会整合其在开源OS、智能硬件上的经验，结合芒果的牌照及资源优势，'
        '在智能硬件或OS领域发力。'
        '公开信息显示，芒果TV在今年6月对外宣布完成A轮5亿人民币融资，估值70亿。'
        '据芒果TV控股方芒果传媒的消息人士透露，芒果TV即将启动B轮融资。')
}

resp = requests.post(
    SUMMARY_URL,
    headers=headers,
    data=json.dumps(source).encode('utf-8'))
resp.raise_for_status()


print(resp.text)



# var e = "http://www.urlgot.com/core";
# var n = "https://www.youtube.com/watch?v=drK3tI8tq_4";
# $.ajax({
#         url: e,
#         type: "post",
#         data: {
#             mediaUrl: n
#         },
#         success: function(e) {
#             console.log(e)
#     }
# });