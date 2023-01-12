#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/1/4 2:53 下午
# @File  : service11.py
# @Author: jinxia
# @Contact : github: jinxia
# @Desc  :

import jieba
import numpy as np
# import logging.config
import logging
import sys
# from loguru import logger
import json
import os
import re
from abstract import Dytext
# sys.path.append('..')

from similarities import (
    SimHashSimilarity,
    TfidfSimilarity,
    BM25Similarity,
    WordEmbeddingSimilarity,
    CilinSimilarity,
    HownetSimilarity,
    SameCharsSimilarity,
    SequenceMatcherSimilarity,
)

# logger.remove()
# logger.add(sys.stderr, level="INFO")

# def sim_and_search(m):
#     print(m)
#     if 'BM25' not in str(m):
#         sim_scores = m.similarity(text1, text2)
#         print('sim scores: ', sim_scores)
#         for (idx, i), j in zip(enumerate(text1), text2):
#             s = sim_scores[idx] if isinstance(sim_scores, list) else sim_scores[idx][idx]
#             print(f"{i} vs {j}, score: {s:.4f}")
#     #统计文档的个数
#     m.add_corpus(corpus)
#     #进行相似度计算
#     # res = m.most_similar(queries, topn=3)
#     res = m.most_similar(queries)
#    #{0: {4: 1.0, 2: 0.4285055994987488, 3: 0.34824615716934204, 0: 0.3471887409687042, 1: 0.07818949222564697}}
#     print('sim search: ', res)
#     for q_id, c in res.items():
#         print('query:', queries[q_id])
#         print("search top 3:")
#         for corpus_id, s in c.items():
#             print(f'\t{m.corpus[corpus_id]}: {s:.4f}')
#     print('-' * 50 + '\n')



# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': True,
# })
logfile = "similar.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(module)s - %(funcName)s - %(message)s",
    handlers=[
        logging.FileHandler(logfile, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("Main")
logger.info(f"日志记录到: {logfile}")

from flask import Flask, request, jsonify, abort
app = Flask(__name__)

# 根据分词选择摘要，摘要字数100个字以内，要求包含分词数量最多的一段话
# 是否有必须包含的词，需要前端提供给权重
# 文本摘要有2中方案 1.包含分词数量最多的一段话 ；2.用模型抽取一段话作为摘要，需要考虑字数为80-100
def abstract(keyword, file_list, min_length=100):
    '''
    获取动态摘要，要求一篇文本为一行
    :param word_list: 分词列表
    :param k: 摘要的大小，100个字
    :param path: 需要获取摘要的文本的路径
    :return: 返回摘要和分词
    :rtype:
    '''
    # keyword = ['资金', '检查', '工作', '方案']
    # 顺序读取文件夹下的所有文件
    # path = './测试文本'
    left = 0
    right = 100
    result = 0
    # 存储所有的文章内容列表
    text_list = []
    # 存储所有动态摘要的列表
    abstract_content = []
    # 存储所有关键字个数的列表
    keyword_content = []
    result_text = ""
    # path_list = os.listdir(path)
    # for filename in path_list:
    #     # encoding='utf-8'
    #     f = open(os.path.join(path, filename), 'rb')
    #     text = f.read().decode(errors='replace')
    #     f.close()
    #     # 对文章内容和文章id组件
    #     file_content.append(text)
    # for text in file_list:
    #     # 对文章用句号进行分句
    #     file_content = re.split(r'。', text)
    #     one_line = file_content[0]
    #     for i in range(1, len(file_content)):
    #         # one_line = file_content[i]
    #         if len(file_content[i]) < 105:
    #             one_line = one_line + '' + file_content[i+1]
    #             i += 1
    #         else:
    #             text_list.append(one_line)
    #仅测试用
    # for text in file_list:
    #     abstract_text = text[left:right]
    #     abstract_content.append(abstract_text)
    for text in file_list:
    # # 对文章用句号进行分句
        content_list = re.split(r'。', text)
        segments = []
        # 段落长度
        seg_len = 0
        # 拼接好的文本
        concat_text = ""
        for one_text in content_list:
            text_len = len(one_text)
            seg_len += text_len
            if concat_text:
                concat_text = concat_text + "。" + one_text
            else:
                concat_text = one_text
            if seg_len < min_length:
                seg_len += text_len
            else:
                segments.append(concat_text)
                concat_text = ""
                seg_len = 0
        if len(concat_text) > min_length:
            segments.append(concat_text)
        for abstract_text in segments:
            # 存储一段摘要内所有的关键词
            keyword_list = []
            for one in keyword:
                # 分别遍历关键字
                one_list = re.findall(one, abstract_text)
                keyword_list = keyword_list + one_list
                # 保存包含关键字最多的字段
            if result < len(keyword_list):
                result = len(keyword_list)
                result_text = abstract_text

        # if result != 0:
        abstract_content.append(result_text)
        keyword_content.append(result)
        # else:
        #     abstract_content.append([''])
        #     keyword_content.append([0])
        print('摘要文本为：', result_text)
        print('包含关键字的个数为：', result)
        result = 0
        result_text = ''
    return abstract_content


@app.route("/api/similar_word", methods=['POST'])
def similar_word():
    """
    接收近义词和同义词
    Args:
        data = {
	"国家电网有限公司" : ["国网","国电"],
	"土豆" : ["马铃薯","芋头"],
	"国电通有限公司" : "国电通"
}
    Returns: 本地保存
    """
    jsonres = request.get_json()
    # jsonres = request.get_data()
    # jsonres = json.loads(jsonres)
    test_data = jsonres.keys()
    # task_id = jsonres.get('id')
    #现在实体的长度大于一定长度
    if not test_data:
        return jsonify("传入的数据不能为空"), 202
    else:
        logging.info("成功收到近义词表")
    #返回200说明获取数据成功
    #将获取的同义词保存到本地txt文件中
    with open('similar_word.txt', 'w', encoding='utf-8') as file:
        file.write(json.dumps(jsonres, ensure_ascii=False))
    data = {
        "code":200
    }
    return jsonify(data)


@app.route("/api/query_process", methods=['POST'])
def query_process():
    """
    分析分句意图，将同义词，近义词替换后，返回给前端
    Args:
        data = {
	"query" : "国网检查的方案"
}
    Returns: {
	"query" : "国家电网有限公司检查的方案"
	"query_word" : ["国家电网有限公司","检查","方案"]
}
    """
    jsonres = request.get_json()
    # jsonres = request.get_data()
    # jsonres = json.loads(jsonres)
    test_data = jsonres.get('query')
    #现在实体的长度大于一定长度
    if not test_data:
        return jsonify("传入的数据不能为空"), 202
    else:
        logging.info("收到查询语句：",test_data)
    #打开同义词典
    with open('similar_word.txt', 'r', encoding='utf-8') as file:
        jsonres = json.load(file)
    file.close()
    keys = list(jsonres.keys())
    # 所有的key值组成新的词典
    with open('key_dist.txt', 'w', encoding='utf-8') as file:
        for i in keys:
            file.write(i + '\n')
    file.close()
    # query = "国电通检测方案"
    query = test_data
    # 给结巴加载自定义词典key_dist.txt
    jieba.load_userdict("key_dist.txt")
    word_list = jieba.lcut(query)
    # 分别和同义词典匹配，有匹配的则替换
    for one in keys:
        a = [jsonres[one] if i == one else i for i in word_list]
    # 将新的分词结果组合成新的问题
    new_query = ''.join(a)
    logger.info('替换同义词后，新的查询语句为：',new_query)
    data = {
        "query_new" : new_query,
        "query_word": a
    }
    return jsonify(data)

@app.route("/api/file_process", methods=['POST'])
def file_process():
    """
    对前端传过来的文章，进行摘要和排序的处理
    Args:
        data = {"id":"84","modelType":"3"}
    Returns: 返回格式 {"progress":"", "train_id": }
     嵌套列表 预测的返回的结果，所有可能关系
    """
    jsonres = request.get_json()
    query = jsonres.get('qa', None)
    #qaField是个列表，需要动态获取
    qaField = jsonres.get('qaField', None)
    file = jsonres.get('list', None)
    #存储所有文章的id
    file_id = []
    #存储所有文章内容列表
    file_list = []
    # 记录下id对应每个文件的字典
    id2article = {}
    for one in file:
        # 首先把一篇文章合并存在files里面
        files = []
        id = one['id']
        file_id.append(id)
        for two in qaField:
            files.append(one[two])
        files_con = "".join(files)
        file_list.append(files_con)
        id2article[id] = one


    #query进行分析和停用词处理
    stopwords = dytext.get_stopwords_list()
    sentence_depart = dytext.seg_depart(query)
    query_list = dytext.move_stopwords(sentence_depart, stopwords)
    #对file进行处理，获取file_list文章列表，和file_id，文章的id
    # file_id = list(file.keys())
    # file_list = list(file.values())
    abstract_content = abstract(query_list,file_list)
    # list_tuple = list(zip(keyword_content, file_id, abstract_content, ))
    # corpus = abstract_content
    # queries = ['资金检查工作方案']
    # print('query: ', query)
    # print('corpus: ', corpus)

    # sim_and_search(SimHashSimilarity())

    # sim_and_search(TfidfSimilarity())
    query_sentences = [query]
    sim_scores = m.similarity(query_sentences, abstract_content)
    print('sim scores: ', sim_scores)
    sim_scores = sim_scores.numpy()
    sim_scores_first = sim_scores[0]
    indices = np.argsort(sim_scores_first)
    sort_indice = sorted(indices, reverse=True)
    article_list = []
    for idx in sort_indice:
        abs_sentence = abstract_content[idx]
        fid = file_id[idx]
        original_article = id2article[fid]
        original_article["zzy_abstract"] = abs_sentence
        article_list.append(original_article)

    jsonres['key_word'] = query_list
    jsonres['list'] = article_list

    result = jsonres
    print(result)

    return jsonify(result)

if __name__ == "__main__":
    dytext = Dytext()
    m = TfidfSimilarity()
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=3328, debug=False, threaded=False)