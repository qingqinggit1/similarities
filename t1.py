#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/1/10 2:31 下午
# @File  : t1.py
# @Author: jinxia
# @Contact : github: jinxia
# @Desc  :


# corpus = [4,5,6]
# start_id = len(corpus) if corpus else 0
# print(start_id)
#
# import pprint
# pp = pprint.PrettyPrinter(indent=2)
# info = {'key_word': ['Swagger', '轻松', '整合', '解决方案'], 'list': [{'createTime': '2023-01-10 19:20:44', 'id': '12345678922', 'projectId': '1', 'projectName': '审计中台建设项目', 'title': '1、传统方式传统方式是文档设计好之后，分别发给前端和后端人员。这样有个缺点，接口信息一旦变化，文档就需要重新发送给前后端人员。无法做到实时。所以浪费时间和精力。2、swagger方式我们的后台应用集成了swagger之后，会自动暴露出我们的接口，而且这个接口形式还通过restful风格发布的。一旦后端的接口有变化，会立刻显示出来，因此极大地提高了效率。OK，基本上一句话就可以总结他的好处，那就是后端写的api文档可以通过swagger的形式实时的发布出来，供前端人员查看。3、其他方式swagger的页面说实话长得不好看，也有一些其他的方案，不是有很多bug，就是收费。目前swagger是使用的最多的。我目前也正在做这个样的开源项目，基于swagger做出类似于其他方案的页面，而且功能更加的强大。', 'zzy_abstract': ''}, {'createTime': '2023-01-10 19:20:44', 'id': '12345678911', 'projectId': '1', 'projectName': '审计中台建设项目', 'title': '随着Spring Boot、Spring Cloud等微服务的流行，在微服务的设计下，小公司微服务工程jar小的几十个，大公司大的工程拆分jar多则几百上万个，这么多的微服务必定产生了大量的接口调用。而接口的调用就必定要写接口文档（由开发人员编写）。存在的问题：（面对多个开发人员或多个开发团队）项目开发接口众多，细节，复杂，且多样化，高质量地创建接口文档费时，费力。随着项目的进行，不可避免整改和优化，需要不断的修改接口实现，伴随着也需要同时修改接口文档，管理不方便不说，还容易出现不一致的情况。Swagger是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful风格的Web服务。实际开发过程中Swagger能够完美的与SpringBoot程序整合，组织出强大RESTful API文档，它既可以减少我们创建文档的工作量，同时也整合了说明内容在实现代码中，让维护文档和修改代码融为一体，可以让我们在修改代码逻辑的同时方便的修改文档说明。另外Swagger2还提供了强大的页面测试功能，让开发者能快速的调试每个RESTful API。', 'zzy_abstract': 'Swagger是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful风格的Web服务。实际开发过程中Swagger能够完美的与SpringBoot程序整合，组织出强大RESTful API文档，它既可以减少我们创建文档的工作量，同时也整合了说明内容在实现代码中，让维护文档和修改代码融为一体，可以让我们在修改代码逻辑的同时方便的修改文档说明'}, {'createTime': '2023-01-10 19:20:44', 'id': '12345678900', 'projectId': '1', 'projectName': '审计中台建设项目', 'title': '从最早开始的word文档，到后续的showdoc，都能减少很多沟通成本，但随之带来的问题也比较麻烦。在开发期间接口会因业务的变更频繁而变动，如果需要实时更新接口文档，这是一个费时费力的工作。为了解决上面的问题，Swagger应运而生。他可以轻松的整合进框架，并通过一系列注解生成强大的API文档。他既可以减轻编写文档的工作量，也可以保证文档的实时更新，将维护文档与修改代码融为一体，是目前较好的解决方案。常用注解', 'zzy_abstract': '为了解决上面的问题，Swagger应运而生。他可以轻松的整合进框架，并通过一系列注解生成强大的API文档。他既可以减轻编写文档的工作量，也可以保证文档的实时更新，将维护文档与修改代码融为一体，是目前较好的解决方案'}], 'qa': 'Swagger它可以轻松整合解决方案', 'qaField': 'title'}
# pp.pprint(info)

import re
text = '1、传统方式传统方式是文档设计好之后，分别发给前端和后端人员。这样有个缺点，接口信息一旦变化，文档就需要重新发送给前后端人员。无法做到实时。所以浪费时间和精力。2、swagger方式我们的后台应用集成了swagger之后，会自动暴露出我们的接口，而且这个接口形式还通过restful风格发布的。一旦后端的接口有变化，会立刻显示出来，因此极大地提高了效率。OK，基本上一句话就可以总结他的好处，那就是后端写的api文档可以通过swagger的形式实时的发布出来，供前端人员查看。3、其他方式swagger的页面说实话长得不好看，也有一些其他的方案，不是有很多bug，就是收费。目前swagger是使用的最多的。我目前也正在做这个样的开源项目，基于swagger做出类似于其他方案的页面，而且功能更加的强大。'
a = ['swagger', '轻松', '整合', '解决方案']
for one in a:
    one_list = re.findall(one, text)
    print(one_list)