#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/30 12:34
# @Author : way
# @Site : 
# @Describe: 10 万厦门招聘数据可视化

from data import SourceDataDemo


class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '厦门招聘大数据'
        self.counter = {'name': '招聘人数', 'value': 270665}
        self.counter2 = {'name': '招聘企业数', 'value': 11059}
        self.echart1_data = {
            'title': '最缺人的行业',
            'data': [
                {"name": "IT互联网", "value": 40215},
                {"name": "电子技术", "value": 17112},
                {"name": "建筑与工程", "value": 17022},
                {"name": "贸易进出口", "value": 16863},
                {"name": "机械重工", "value": 15705},
                {"name": "教育培训", "value": 11718},
            ]
        }
        self.echart2_data = {
            'title': '最缺人的公司',
            'data': [
                {"name": "外资", "value": 8991},
                {"name": "民营/私营", "value": 207644},
                {"name": "合资", "value": 8317},
                {"name": "事业单位", "value": 842},
                {"name": "台资/港资", "value": 10969},
                {"name": "国营企业", "value": 8901},
                {"name": "上市公司", "value": 13770},
                {"name": "其他", "value": 11231},
            ]
        }
        self.echarts3_1_data = {
            'title': '工作时间',
            'data': [
                {"name": "6.5小时", "value": 2105},
                {"name": "7小时", "value": 21761},
                {"name": "7.5小时", "value": 41025},
                {"name": "8小时", "value": 104917},
                {"name": "10小时", "value": 4910},
                {"name": "12小时", "value": 3883},
            ]
        }
        self.echarts3_2_data = {
            'title': '上班天数',
            'data': [
                {"name": "5天/周", "value": 84910},
                {"name": "5.5天/周", "value": 21530},
                {"name": "6天/周", "value": 56152},
                {"name": "6.5天/周", "value": 1574},
                {"name": "7天/周", "value": 1500},
                {"name": "大小周", "value": 7717},
            ]
        }
        self.echarts3_3_data = {
            'title': '班制',
            'data': [
                {"name": "正常白班", "value": 111140},
                {"name": "正常晚班", "value": 873},
                {"name": "正常夜班", "value": 121},
                {"name": "不定时工作制", "value": 4715},
                {"name": "2班倒", "value": 14977},
                {"name": "3班倒", "value": 1986},
                {"name": "4班倒", "value": 199},
            ]
        }
        self.echart4_data = {
            'title': '学历与机遇',
            'data': [
                {"name": "招聘人数",
                 "value": [76837, 3942, 20330, 25676, 19644, 84883, 37838, 1428, 87]},
                {"name": "平均薪资",
                 "value": [5474, 4065, 4461, 4771, 4819, 5818, 7458, 9226, 17128]},
            ],
            'xAxis': ['不限', '小学', '初中', '中专', '高中', '大专', '本科', '硕士', '博士'],
        }
        self.echart5_data = {
            'title': '平均薪资',
            'data': [
                {"name": "外资", "value": 5412},
                {"name": "民营/私营", "value": 5812},
                {"name": "合资", "value": 5742},
                {"name": "事业单位", "value": 8224},
                {"name": "台资/港资", "value": 5239},
                {"name": "国营企业", "value": 5567},
                {"name": "上市公司", "value": 6432},
                {"name": "其他", "value": 5365},
            ]
        }
        self.echart6_data = {
            'title': '工作年限与薪资',
            'data': [
                {"name": "1-3年", "value": 5302, "value2": 15000 - 5302, "color": "01", "radius": ['59%', '70%']},
                {"name": "3-5年", "value": 6938, "value2": 15000 - 6938, "color": "02", "radius": ['49%', '60%']},
                {"name": "5-10年", "value": 9750, "value2": 15000 - 9750, "color": "03", "radius": ['39%', '50%']},
                {"name": "10年以上", "value": 14350, "value2": 15000 - 14350, "color": "05", "radius": ['29%', '40%']},
                {"name": "不限", "value": 5272, "value2": 15000 - 5272, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 20000,
            'data': [
                {
                    "name": "甘肃省",
                    "value": 9
                },
                {
                    "name": "咸阳",
                    "value": 9
                },
                {
                    "name": "兰州",
                    "value": 1
                },
                {
                    "name": "拉萨",
                    "value": 15
                },
                {
                    "name": "咸宁",
                    "value": 4
                },
                {
                    "name": "湖州",
                    "value": 1
                },
                {
                    "name": "石家庄",
                    "value": 2
                },
                {
                    "name": "营口",
                    "value": 1
                },
                {
                    "name": "晋江",
                    "value": 995
                },
                {
                    "name": "湛江",
                    "value": 1
                },
                {
                    "name": "苏州",
                    "value": 11
                },
                {
                    "name": "宁德",
                    "value": 326
                },
                {
                    "name": "安溪",
                    "value": 324
                },
                {
                    "name": "连云港",
                    "value": 23
                },
                {
                    "name": "商洛",
                    "value": 1
                },
                {
                    "name": "潮州",
                    "value": 37
                },
                {
                    "name": "宁夏",
                    "value": 4
                },
                {
                    "name": "喀什地区",
                    "value": 4
                },
                {
                    "name": "烟台",
                    "value": 2
                },
                {
                    "name": "保定",
                    "value": 2
                },
                {
                    "name": "杭州",
                    "value": 36
                },
                {
                    "name": "厦门",
                    "value": 231249
                },
                {
                    "name": "运城",
                    "value": 1
                },
                {
                    "name": "福州",
                    "value": 1438
                },
                {
                    "name": "九江",
                    "value": 1
                },
                {
                    "name": "南平",
                    "value": 248
                },
                {
                    "name": "潜江",
                    "value": 3
                },
                {
                    "name": "新疆",
                    "value": 3
                },
                {
                    "name": "湖南省",
                    "value": 62
                },
                {
                    "name": "吉安",
                    "value": 2
                },
                {
                    "name": "遵义",
                    "value": 2
                },
                {
                    "name": "郑州",
                    "value": 13
                },
                {
                    "name": "福建省",
                    "value": 20304
                },
                {
                    "name": "三亚",
                    "value": 4
                },
                {
                    "name": "山西省",
                    "value": 32
                },
                {
                    "name": "扬州",
                    "value": 1
                },
                {
                    "name": "丽水",
                    "value": 6
                },
                {
                    "name": "内蒙古",
                    "value": 5
                },
                {
                    "name": "上饶",
                    "value": 1
                },
                {
                    "name": "盐城",
                    "value": 2
                },
                {
                    "name": "汕头",
                    "value": 26
                },
                {
                    "name": "南充",
                    "value": 2
                },
                {
                    "name": "安庆",
                    "value": 1
                },
                {
                    "name": "深圳",
                    "value": 125
                },
                {
                    "name": "南京",
                    "value": 7
                },
                {
                    "name": "青岛",
                    "value": 8
                },
                {
                    "name": "河北省",
                    "value": 55
                },
                {
                    "name": "黄浦区",
                    "value": 7
                },
                {
                    "name": "龙岩",
                    "value": 1219
                },
                {
                    "name": "西藏",
                    "value": 1
                },
                {
                    "name": "十堰",
                    "value": 10
                },
                {
                    "name": "安徽省",
                    "value": 32
                },
                {
                    "name": "德州",
                    "value": 2
                },
                {
                    "name": "泰州",
                    "value": 1
                },
                {
                    "name": "太仓",
                    "value": 1
                },
                {
                    "name": "广西",
                    "value": 56
                },
                {
                    "name": "南安",
                    "value": 640
                },
                {
                    "name": "芜湖",
                    "value": 1
                },
                {
                    "name": "肇庆",
                    "value": 11
                },
                {
                    "name": "陕西省",
                    "value": 19
                },
                {
                    "name": "揭阳",
                    "value": 6
                },
                {
                    "name": "成都",
                    "value": 41
                },
                {
                    "name": "武汉",
                    "value": 13
                },
                {
                    "name": "百色",
                    "value": 5
                },
                {
                    "name": "河池",
                    "value": 1
                },
                {
                    "name": "辽宁省",
                    "value": 13
                },
                {
                    "name": "大连",
                    "value": 2
                },
                {
                    "name": "鹰潭",
                    "value": 4
                },
                {
                    "name": "莆田",
                    "value": 349
                },
                {
                    "name": "张家港",
                    "value": 1
                },
                {
                    "name": "西安",
                    "value": 13
                },
                {
                    "name": "海南省",
                    "value": 15
                },
                {
                    "name": "贵州省",
                    "value": 13
                },
                {
                    "name": "上海",
                    "value": 318
                },
                {
                    "name": "五家渠",
                    "value": 2
                },
                {
                    "name": "宿州",
                    "value": 1
                },
                {
                    "name": "海淀区",
                    "value": 3
                },
                {
                    "name": "济南",
                    "value": 1
                },
                {
                    "name": "威海",
                    "value": 1
                },
                {
                    "name": "南宁",
                    "value": 11
                },
                {
                    "name": "梅州",
                    "value": 3
                },
                {
                    "name": "中山",
                    "value": 9
                },
                {
                    "name": "惠州",
                    "value": 9
                },
                {
                    "name": "武夷山",
                    "value": 5
                },
                {
                    "name": "昆明",
                    "value": 8
                },
                {
                    "name": "珠海",
                    "value": 4
                },
                {
                    "name": "金华",
                    "value": 2
                },
                {
                    "name": "江西省",
                    "value": 117
                },
                {
                    "name": "顺德",
                    "value": 1
                },
                {
                    "name": "唐山",
                    "value": 3
                },
                {
                    "name": "东莞",
                    "value": 26
                },
                {
                    "name": "抚州",
                    "value": 1
                },
                {
                    "name": "常熟",
                    "value": 1
                },
                {
                    "name": "贵阳",
                    "value": 1
                },
                {
                    "name": "沈阳",
                    "value": 3
                },
                {
                    "name": "台州",
                    "value": 3
                },
                {
                    "name": "长乐",
                    "value": 9
                },
                {
                    "name": "浙江省",
                    "value": 209
                },
                {
                    "name": "其他",
                    "value": 11
                },
                {
                    "name": "日照",
                    "value": 1
                },
                {
                    "name": "南通",
                    "value": 1
                },
                {
                    "name": "山东省",
                    "value": 102
                },
                {
                    "name": "仙桃",
                    "value": 5
                },
                {
                    "name": "黑龙江省",
                    "value": 1
                },
                {
                    "name": "赣州",
                    "value": 16
                },
                {
                    "name": "北京",
                    "value": 177
                },
                {
                    "name": "昆山",
                    "value": 3
                },
                {
                    "name": "浦东新区",
                    "value": 17
                },
                {
                    "name": "宁波",
                    "value": 9
                },
                {
                    "name": "福清",
                    "value": 40
                },
                {
                    "name": "石狮",
                    "value": 354
                },
                {
                    "name": "梧州",
                    "value": 3
                },
                {
                    "name": "国外",
                    "value": 196
                },
                {
                    "name": "佛山",
                    "value": 21
                },
                {
                    "name": "常州",
                    "value": 1
                },
                {
                    "name": "长治",
                    "value": 2
                },
                {
                    "name": "重庆",
                    "value": 65
                },
                {
                    "name": "江苏省",
                    "value": 136
                },
                {
                    "name": "三明",
                    "value": 197
                },
                {
                    "name": "合肥",
                    "value": 6
                },
                {
                    "name": "广州",
                    "value": 73
                },
                {
                    "name": "淮安",
                    "value": 10
                },
                {
                    "name": "温州",
                    "value": 13
                },
                {
                    "name": "朝阳区",
                    "value": 5
                },
                {
                    "name": "南昌",
                    "value": 14
                },
                {
                    "name": "绍兴",
                    "value": 1
                },
                {
                    "name": "徐州",
                    "value": 8
                },
                {
                    "name": "平顶山",
                    "value": 3
                },
                {
                    "name": "台湾",
                    "value": 4
                },
                {
                    "name": "",
                    "value": 77
                },
                {
                    "name": "河南省",
                    "value": 34
                },
                {
                    "name": "长沙",
                    "value": 22
                },
                {
                    "name": "湖北省",
                    "value": 78
                },
                {
                    "name": "山南",
                    "value": 3
                },
                {
                    "name": "漳州",
                    "value": 7038
                },
                {
                    "name": "四川省",
                    "value": 125
                },
                {
                    "name": "无锡",
                    "value": 2
                },
                {
                    "name": "香港",
                    "value": 3
                },
                {
                    "name": "泉州",
                    "value": 2817
                },
                {
                    "name": "临夏回族自治州",
                    "value": 1
                },
                {
                    "name": "银川",
                    "value": 7
                },
                {
                    "name": "荆门",
                    "value": 1
                },
                {
                    "name": "吉林省",
                    "value": 8
                },
                {
                    "name": "广东省",
                    "value": 209
                },
                {
                    "name": "义乌",
                    "value": 5
                },
                {
                    "name": "铜仁",
                    "value": 1
                },
                {
                    "name": "海口",
                    "value": 9
                },
                {
                    "name": "天津",
                    "value": 69
                },
                {
                    "name": "云南省",
                    "value": 25
                }
            ]
        }
