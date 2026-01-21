#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2026/01/21 15:58
# @Author : way
# @Site :
# @Describe: 一般动态接口应该是读数据库获取最新数据；此处简化处理，使用 add_random 与指标累计叠加，模拟数据增长，接口返回数据对象

import copy
import random

# 参与累计的字段
_DATA_ATTRS = [
    'counter', 'counter2',
    'echart1_data', 'echart2_data',
    'echarts3_1_data', 'echarts3_2_data', 'echarts3_3_data',
    'echart4_data', 'echart5_data', 'echart6_data',
    # 'map_1_data',
]
_store = {'data': None, 'corp': None, 'job': None}


def add_random(obj, factor=0.1):
    """
    给各指标增加随机数值。只在原值基础上正向叠加，不减少、不回落，直接修改 obj。
    :param obj: 具备 counter、counter2、echart*_data、map_1_data 等属性的数据对象
    :param factor: 每次叠加的随机增幅上限，如 0.1 表示最多 +10%，默认 0.1
    """
    def _rand_num(v, is_int=True, min_val=0, max_val=None):
        raw = v * (1 + random.uniform(0, factor))
        new_v = round(raw) if is_int else raw
        new_v = max(min_val, v, new_v)
        if max_val is not None:
            new_v = min(new_v, max_val)
        return new_v

    if obj.counter and 'value' in obj.counter:
        obj.counter['value'] = _rand_num(
            obj.counter['value'], is_int=True, min_val=0
        )
    if obj.counter2 and 'value' in obj.counter2:
        obj.counter2['value'] = _rand_num(
            obj.counter2['value'], is_int=True, min_val=0
        )

    for attr in ('echart1_data', 'echart2_data', 'echarts3_1_data',
                 'echarts3_2_data', 'echarts3_3_data', 'echart5_data'):
        d = getattr(obj, attr, None)
        if not d or not d.get('data'):
            continue
        for item in d['data']:
            if 'value' in item and isinstance(item['value'], (int, float)):
                item['value'] = _rand_num(item['value'], is_int=True, min_val=1)

    if obj.echart4_data and obj.echart4_data.get('data'):
        for item in obj.echart4_data['data']:
            if 'value' in item and isinstance(item['value'], list):
                item['value'] = [
                    _rand_num(x, is_int=True, min_val=0) for x in item['value']
                ]

    if obj.echart6_data and obj.echart6_data.get('data'):
        for item in obj.echart6_data['data']:
            v1 = item.get('value', 50)
            v2 = item.get('value2', 50)
            if v1 is None and v2 is None:
                continue
            item['value'] = _rand_num(v1, is_int=True, min_val=1)
            item['value2'] = _rand_num(v2, is_int=True, min_val=1)

    # if obj.map_1_data and obj.map_1_data.get('data'):
    #     for item in obj.map_1_data['data']:
    #         if 'value' in item:
    #             item['value'] = _rand_num(
    #                 item['value'], is_int=True, min_val=1, max_val=1000
    #             )


def _get_data_state(obj):
    """从数据对象提取供累计的字段快照"""
    return {k: copy.deepcopy(getattr(obj, k, None)) for k in _DATA_ATTRS}


def _set_data_state(obj, state):
    """把之前累计的状态写回数据对象"""
    if state is None:
        return
    for k in _DATA_ATTRS:
        if k not in state:
            continue
        v = state[k]
        setattr(obj, k, copy.deepcopy(v) if v is not None else None)


def get_accumulated_data(key, factory, factor=0.1):
    """
    在上一轮结果上叠加随机并累计，返回 to_dict()。
    :param key: 存储键，'data' / 'corp' / 'job'
    :param factory: 无参可调用对象，返回新的数据实例，如 SourceData、CorpData、JobData
    :param factor: add_random 的随机幅度
    :return: 数据字典，可直接用于 jsonify
    """
    data = factory()
    if _store.get(key) is not None:
        _set_data_state(data, _store[key])
    add_random(data, factor=factor)
    _store[key] = _get_data_state(data)
    return data
