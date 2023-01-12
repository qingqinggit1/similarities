#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/1/8 2:25 下午
# @File  : similar_test.py
# @Author: jinxia
# @Contact : github: jinxia
# @Desc  :

import unittest
import requests
import time, os
import json
import base64
import random
import string
import pickle
import sys
import pandas as pd


class similarTestCase(unittest.TestCase):
    # 自动化训练平台的测试代码
    # 确保Flask server已经启动
    host = '192.168.10.242'
    # host = '127.0.0.1'
    env_host = os.environ.get('host')
    if env_host:
        host = env_host
    host_mtdnn = f'http://{host}:3326'
    def test_similar_word(self):
        """
        自动接收标注平台的数据，并处理
        :return:
        :rtype:
        """
        # 2. 执行
        url = f"{self.host_mtdnn}/api/similar_word"
        # # data_file = "/Users/admin/Downloads/all1.json"
        # data_file = "/home/fujinxia/train/mt-dnn/all1.json"
        # with open(data_file, "r", encoding="utf-8") as f:
        #     data = json.load(f)

        #前端的数据格式
        params = {
	                "国网" : "国家电网有限公司",
	                "土豆" : "马铃薯",
	                "国电通" : "国电通有限公司",
                    "资金方案" : "资金检查方案审查",
                    "三重一大" : "三重一大政策",
                    "小金人" : "资金财库小金人"
           }
        # params = {'data': data}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        print(result)
        assert r.status_code == 200
        assert result is not None, "返回结果为None"
        #检查结果，里面肯定是字典格式
        print("同义词典接口测试完成")
    def test_query_process(self):
        """
        给前端返回训练进度
        :return:
        :rtype:
        """
        # 2. 执行
        url = f"{self.host_mtdnn}/api/query_process"
        params = {"query" : "小金人的意思是什么？"}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        print(result)
        #检查结果，里面肯定是字典格式
        print("query分析接口测试完成")

    def test_file_process_one(self):
        """
        给前端返回训练结果
        :return:
        :rtype:
        """
        # 2. 执行
        url = f"{self.host_mtdnn}/api/file_process"
        params1 = {
                    "query" : "资金检查",
                    "file" : {

                        "001" : "关于印发《连城县财政局开展财政专项资金检查工作方案对预算收入管理情况的检查,按照综合预算的要求，加强对预算收入管理的监督检查,重点检查各单位依法取得的罚没收入、行政事业性收费、政府性基金、国有资产收益和处置等非税收入，未按规定及时足额上缴国库，隐瞒、截留、挤占、挪用、坐支或者私分，以及违规转移到所属工会、培训中心、服务中心等单位使用，不按规定使用财政部门统一印制或监制的收费票据等问题；严肃查处各种形式的乱收费、乱罚款、乱摊派。",
                        "002" : "资金管理）专项资金检查工作实施方案对预算支出管理情况的检查，遵循先有预算、后有支出的原则，加强对预算支出管理的监督检查,（1）检查是否存在超预算或者无预算安排支出，虚列支出、转移或者套取预算资金，转嫁支出，违反规定擅自设立项目、超标准超范围发放津贴补贴，没有按规定使用公务卡等问题。",
                        "003" : "关于印发《开展疫情防控和资金管理使用情况检查工作实施，（3）对会议费和培训费的检查,会议费重点检查计划外召开会议，以虚报、冒领手段骗取会议费，虚报会议人数、天数等进行报销，违规扩大会议费开支范围、擅自提高会议费开支标准，在非定点饭店或严禁召开会议的风景名胜区召开会议，违规转嫁或摊派会议费用以及报销与会议无关费用等问题。培训费重点检查计划外举办培训班，超范围和开支标准列支培训费，虚报和未按规定程序报销培训费，转嫁、摊派培训费用和向参训人员乱收费，借会议、培训之名组织会餐、安排宴请、公款旅游以及在会议费、培训费中列支公务接待费等与会议、培训无关的支出。"
                    }
        }
        params2 = {
                      "qa": "资金检查",
                      "qaField": "title",
                      "list": [
                        {
                          "createTime": "2023-01-10 19:20:44",
                          "id": "1234567890",
                          "projectName": "审计中台建设项目",
                          "title": "关于印发《连城县财政局开展财政专项资金检查工作方案对预算收入管理情况的检查,按照综合预算的要求，加强对预算收入管理的监督检查,重点检查各单位依法取得的罚没收入、行政事业性收费、政府性基金、国有资产收益和处置等非税收入，未按规定及时足额上缴国库，隐瞒、截留、挤占、挪用、坐支或者私分，以及违规转移到所属工会、培训中心、服务中心等单位使用，不按规定使用财政部门统一印制或监制的收费票据等问题；严肃查处各种形式的乱收费、乱罚款、乱摊派。",
                          "projectId": "1"
                        },
                          {
                              "createTime": "2023-01-10 19:20:44",
                              "id": "1234567891",
                              "projectName": "审计中台建设项目",
                              "title": "资金管理）专项资金检查工作实施方案对预算支出管理情况的检查，遵循先有预算、后有支出的原则，加强对预算支出管理的监督检查,（1）检查是否存在超预算或者无预算安排支出，虚列支出、转移或者套取预算资金，转嫁支出，违反规定擅自设立项目、超标准超范围发放津贴补贴，没有按规定使用公务卡等问题。",
                              "projectId": "1"
                          },
                          {
                              "createTime": "2023-01-10 19:20:44",
                              "id": "123456789",
                              "projectName": "审计中台建设项目",
                              "title": "关于印发《开展疫情防控和资金管理使用情况检查工作实施，（3）对会议费和培训费的检查,会议费重点检查计划外召开会议，以虚报、冒领手段骗取会议费，虚报会议人数、天数等进行报销，违规扩大会议费开支范围、擅自提高会议费开支标准，在非定点饭店或严禁召开会议的风景名胜区召开会议，违规转嫁或摊派会议费用以及报销与会议无关费用等问题。培训费重点检查计划外举办培训班，超范围和开支标准列支培训费，虚报和未按规定程序报销培训费，转嫁、摊派培训费用和向参训人员乱收费，借会议、培训之名组织会餐、安排宴请、公款旅游以及在会议费、培训费中列支公务接待费等与会议、培训无关的支出。",
                              "projectId": "1"
                          }
  ]
}
        params = {
            "qa":"Swagger它可以轻松整合解决方案",
            "qaField":"title",
            "list":[
                {
                    "createTime":"2023-01-10 19:20:44",
                    "id":"123456789","projectName":"审计中台建设项目",
                    "title":"从最早开始的word文档，到后续的showdoc，都能减少很多沟通成本，但随之带来的问题也比较麻烦。在开发期间接口会因业务的变更频繁而变动，如果需要实时更新接口文档，这是一个费时费力的工作。为了解决上面的问题，Swagger应运而生。他可以轻松的整合进框架，并通过一系列注解生成强大的API文档。他既可以减轻编写文档的工作量，也可以保证文档的实时更新，将维护文档与修改代码融为一体，是目前较好的解决方案。常用注解",
                    "projectId":"1"
                }
            ]
        }

        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        print(result)
        # assert r.status_code == 200
        # assert result is not None, "返回结果为None"
        # print(json.dumps(result, indent=4, ensure_ascii=False))
        #检查结果，里面肯定是字典格式
        print("对文件处理接口测试完成")
    def test_file_process_many(self):
        """
        给前端返回训练结果
        :return:
        :rtype:
        """
        # 2. 执行
        url = f"{self.host_mtdnn}/api/file_process"
        params2 = {
                      "qa": "资金检查",
                      "qaField": "title",
                      "list": [
                        {
                          "createTime": "2023-01-10 19:20:44",
                          "id": "1234567890",
                          "projectName": "审计中台建设项目",
                          "title": "关于印发《连城县财政局开展财政专项资金检查工作方案对预算收入管理情况的检查,按照综合预算的要求，加强对预算收入管理的监督检查,重点检查各单位依法取得的罚没收入、行政事业性收费、政府性基金、国有资产收益和处置等非税收入，未按规定及时足额上缴国库，隐瞒、截留、挤占、挪用、坐支或者私分，以及违规转移到所属工会、培训中心、服务中心等单位使用，不按规定使用财政部门统一印制或监制的收费票据等问题；严肃查处各种形式的乱收费、乱罚款、乱摊派。",
                          "projectId": "1"

                        },
                          {
                              "createTime": "2023-01-10 19:20:44",
                              "id": "1234567891",
                              "projectName": "审计中台建设项目",
                              "title": "资金管理）专项资金检查工作实施方案对预算支出管理情况的检查，遵循先有预算、后有支出的原则，加强对预算支出管理的监督检查,（1）检查是否存在超预算或者无预算安排支出，虚列支出、转移或者套取预算资金，转嫁支出，违反规定擅自设立项目、超标准超范围发放津贴补贴，没有按规定使用公务卡等问题。",
                              "projectId": "1"
                          },
                          {
                              "createTime": "2023-01-10 19:20:44",
                              "id": "123456789",
                              "projectName": "审计中台建设项目",
                              "title": "关于印发《开展疫情防控和资金管理使用情况检查工作实施，（3）对会议费和培训费的检查,会议费重点检查计划外召开会议，以虚报、冒领手段骗取会议费，虚报会议人数、天数等进行报销，违规扩大会议费开支范围、擅自提高会议费开支标准，在非定点饭店或严禁召开会议的风景名胜区召开会议，违规转嫁或摊派会议费用以及报销与会议无关费用等问题。培训费重点检查计划外举办培训班，超范围和开支标准列支培训费，虚报和未按规定程序报销培训费，转嫁、摊派培训费用和向参训人员乱收费，借会议、培训之名组织会餐、安排宴请、公款旅游以及在会议费、培训费中列支公务接待费等与会议、培训无关的支出。",
                              "projectId": "1"
                          }
  ]
}
        params = {
            "qa":"Swagger它可以轻松整合解决方案",
            "qaField":["title","content"],
            "list":[
                {
                    "createTime":"2023-01-10 19:20:44",
                    "id":"12345678900","projectName":"审计中台建设项目",
                    "title":"从最早开始的word文档，到后续的showdoc，都能减少很多沟通成本，但随之带来的问题也比较麻烦。在开发期间接口会因业务的变更频繁而变动，如果需要实时更新接口文档，这是一个费时费力的工作。为了解决上面的问题，Swagger应运而生。他可以轻松的整合进框架，并通过一系列注解生成强大的API文档。他既可以减轻编写文档的工作量，也可以保证文档的实时更新，将维护文档与修改代码融为一体，是目前较好的解决方案。常用注解",
                    "content":"从最早开始的word文档。",
                    "projectId":"1"
                },
                {
                    "createTime": "2023-01-10 19:20:44",
                    "id": "12345678911", "projectName": "审计中台建设项目",
                    "title": "随着Spring Boot、Spring Cloud等微服务的流行，在微服务的设计下，小公司微服务工程jar小的几十个，大公司大的工程拆分jar多则几百上万个，这么多的微服务必定产生了大量的接口调用。而接口的调用就必定要写接口文档（由开发人员编写）。存在的问题：（面对多个开发人员或多个开发团队）项目开发接口众多，细节，复杂，且多样化，高质量地创建接口文档费时，费力。随着项目的进行，不可避免整改和优化，需要不断的修改接口实现，伴随着也需要同时修改接口文档，管理不方便不说，还容易出现不一致的情况。Swagger是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful风格的Web服务。实际开发过程中Swagger能够完美的与SpringBoot程序整合，组织出强大RESTful API文档，它既可以减少我们创建文档的工作量，同时也整合了说明内容在实现代码中，让维护文档和修改代码融为一体，可以让我们在修改代码逻辑的同时方便的修改文档说明。另外Swagger2还提供了强大的页面测试功能，让开发者能快速的调试每个RESTful API。",
                    "content": "从最早开始的word文档。",
                    "projectId": "1"
                },
                {
                    "createTime": "2023-01-10 19:20:44",
                    "id": "12345678922", "projectName": "审计中台建设项目",
                    "title": "1、传统方式传统方式是文档设计好之后，分别发给前端和后端人员。这样有个缺点，接口信息一旦变化，文档就需要重新发送给前后端人员。无法做到实时。所以浪费时间和精力。2、swagger方式我们的后台应用集成了swagger之后，会自动暴露出我们的接口，而且这个接口形式还通过restful风格发布的。一旦后端的接口有变化，会立刻显示出来，因此极大地提高了效率。OK，基本上一句话就可以总结他的好处，那就是后端写的api文档可以通过swagger的形式实时的发布出来，供前端人员查看。3、其他方式swagger的页面说实话长得不好看，也有一些其他的方案，不是有很多bug，就是收费。目前swagger是使用的最多的。我目前也正在做这个样的开源项目，基于swagger做出类似于其他方案的页面，而且功能更加的强大。",
                    "content": "从最早开始的word文档。",
                    "projectId": "1"
                }
            ]
        }

        headers = {'content-type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(params), timeout=360)
        result = r.json()
        print(result)
        # assert r.status_code == 200
        # assert result is not None, "返回结果为None"
        # print(json.dumps(result, indent=4, ensure_ascii=False))
        #检查结果，里面肯定是字典格式
        print("对文件处理接口测试完成")

if __name__ == '__main__':
    similarTestCase.host = os.environ.get('mtdnnhost', similarTestCase.host)
    ##确保Flask server已经启动
    unittest.main()
