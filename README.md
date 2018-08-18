# old-land-flask-api
# API说明
* 点赞和取消点赞接口需要携带token
* token必须通过小程序的code换取
* 无论是提交数据还是返回数据只支持json
* API遵从严格的HTTP动作并采用标准的 Http Status Code 作为响应状态，建议采用HTTP状态码作为Api调用是否成功的标识,具体异常请通过错误码判断

- [返回码](README.md#返回码)
    * [HTTP 状态码](README.md#HTTP状态码)
    * [错误码(error_code)](README.md#错误码)

- [期刊](README.md#期刊)
    * [获取最新一期](README.md#获取最新一期)
    * [获取当前一期的下一期](README.md#获取当前一期的下一期)
    * [获取某一期详细信息](README.md#获取某一期详细信息)
    * [获取当前一期的上一期](README.md#获取当前一期的上一期)
    * [获取点赞信息](README.md#获取点赞信息)
    * [获取我喜欢的期刊](README.md#获取我喜欢的期刊)

- [书籍](README.md#书籍)
    * [获取热门书籍(概要)](README.md#获取热门书籍(概要))
    * [获取书籍短评](README.md#获取热门书籍短评)
    * [获取喜欢书籍数量](README.md#获取喜欢书籍数量)
    * [获取书籍点赞情况](README.md#获取书籍点赞情况)
    * [新增短评](README.md#新书短评)
    * [获取热搜关键字](README.md#获取热搜关键字)
    * [书籍搜索](README.md#书籍搜索)
    * [获取书籍详细信息](README.md#获取书籍详细信息)

- [点赞](README.md#点赞)
    * [进行点赞](README.md#进行点赞)
    * [取消点赞](README.md#取消点赞)
    
- [小程序登录](README.md#小程序登录)
    * [获取token](README.md#获取token)
    * [验证token](README.md#验证token)


# 返回码
 ## HTTP状态码
 
|     状态码   |     含义                  |    说明           |
| ----------- | ------------------------ | ----------------- |
|  200        | OK                       |  请求成功           |
|  201        | CREATED                  |  创建成功           |
|  202        | ACCEPTED                 |  更新成功           |
|  204        | NO CONTENT               |  删除成功           |
|  301        | MOVED PERMANENTLY        |  永久重定向         |
|  400        | BAD REQUEST              |  请求包含不支持的参数 |
|  401        | UNAUTHORIZED             |  未授权             |
|  403        | FORBIDDEN                |  被禁止访问          |
|  404        | NOT FOUND                |  请求的资源不存在     |
|  413        | REQUIRED LENGTH TOO LARGE|  上传的File体积太大  |
|  500        | INTERNAL SERVER ERROR    |  内部错误           |


## 错误码

请以错误码来判断具体的错误，不要以文字描述作为判断的依据

>100x 通用类型:

|错误码      |      含义           |
|-----------|--------------------|
|0          | OK, 成功            |
|1000       | 输入参数错误         |
|1001       | 输入的json格式不正确  |
|1002       | 找不到资源           |
|1003       | 未知错误             |
|1004       | 禁止访问             |
|1005       | 不正确的开发者key     |
|1006       | 服务器内部错误        |


>200x 点赞类型

|错误码   |         含义     |
|--------|-----------------|
|2000    |    你已经点过赞了 |
|2001	 |	你还没点过赞    |


>300x 期刊类型

|错误码     |       含义       |
|----------|-----------------|
|3000      |  该期内容不存在    |
    
    
# 期刊

## 获取最新一期
URL:  
>GET    /classic/latest

Response 200:
```json
{
    "content": "人生不能像做菜，把所有的材料准备好才下锅",
    "fav_nums": 2,
    "id": 8,
    "image": "http://127.0.0.1:5000/v1/movie.2.png",
    "index": 8,
    "like_status": 0,
    "pubdate": "2018-08-14",
    "title": "李安《饮食男女》",
    "type": 100
}
```

Response_description:
* content：期刊内容
* fav_nums: 点赞次数
* image: 图片
* index: 期号
* like_status: 是否点赞
* pubdate: 发布日期
* title: 期刊题目
* type: 期刊类型,这里的类型分为:100 电影 200 音乐 300 句子
* id: 期刊在数据中序号，供点赞使用
* 返回期刊的详细信息

## 获取当前一期的下一期
URL:
>GET   /classic/<int:index>/next

>demo  /classic/2/next

Parameters:

* id：id号,必填,必须是正整数

Response 200:
```json
{
    "content": "你陪我不如蝉夏 越过城市喧嚣",
    "fav_nums": 0,
    "id": 3,
    "image": "http://127.0.0.1:5000/v1/music.2.png",
    "index": 3,
    "like_status": 0,
    "pubdate": "2018-08-14",
    "title": "花弼《纸短情长》",
    "type": 200,
    "url": "http://music.163.com/song/media/outer/url?id=557581284.mp3"
}
```

## 获取某一期详细信息
URL:
>GET   /classic/<int:type>/<int:id>

>demo   /classic/200/1

Parameters:

* id：id号,必填,必须是正整数
* type: 类型号，必填，为100,200,300的一种，分别表示电影，音乐，句子

Response 200:
```json
{
    "content": "岁月长，衣裳薄",
    "fav_nums": 0,
    "id": 1,
    "image": "http://127.0.0.1:5000/v1/music.1.png",
    "index": 1,
    "like_status": 0,
    "pubdate": "2018-08-14",
    "title": "杨千嬅《再见二丁目》",
    "type": 200,
    "url": "http://music.163.com/song/media/outer/url?id=557581284.mp3"
}
```

## 获取当前一期的上一期
URL:
>GET   /classic/<int:index>/next

>demo /classic/5/next

Parameters:
* id：id号,必填,必须是正整数

Response 200:
```json
{
    "content": "在变换的生命里，岁月原来是最大的小偷",
    "fav_nums": 0,
    "id": 4,
    "image": "http://127.0.0.1:5000/v1/movie.1.png",
    "index": 4,
    "like_status": 0,
    "pubdate": "2018-08-14",
    "title": "罗启锐《岁月神偷》",
    "type": 100
}
```

## 获取点赞信息

URL:
>GET   /classic/<int:type>/<int:id>/favor

>demo /classic/200/7/favor

Parameters:

* id：id号,必填,必须是正整数
* type: 类型号，必填，为100,200,300的一种，分别表示电影，音乐，句子
* token: 通过 Basic Auth方式传递 username: eyJhbGciOiJIUzI1NiIsImlhdCI6MTUzNDUxODQ0MCwiZXhwIjoxNTM3MTEwNDQwfQ.eyJ1aWQiOjEsInR5cGUiOjIwMCwic2NvcGUiOiJVc2VyU2NvcGUifQ.S1YoU30kgUIwYRgyCVeDgL2VvYcTlmeGph6P9Vd2irg, password: ''

Response 200:

```json
{
    "fav_nums": 2,
    "id": 7,
    "like_status": 1
}
```

## 获取我喜欢的期刊
URL:
>GET   /classic/favor

Parameters:
* token

Response 200:

```json
[
    {
        "content": "人生不能像做菜，把所有的材料准备好才下锅",
        "fav_nums": 2,
        "id": 8,
        "image": "http://127.0.0.1:5000/v1/movie.2.png",
        "index": 8,
        "like_status": 1,
        "pubdate": "2018-08-14",
        "title": "李安《饮食男女》",
        "type": 100
    },
    {
        "content": "谁念过 千字文章 秋收冬已藏",
        "fav_nums": 2,
        "id": 7,
        "image": "http://127.0.0.1:5000/v1/music.4.png",
        "index": 7,
        "like_status": 1,
        "pubdate": "2018-08-14",
        "title": "不才《参商》",
        "type": 200,
        "url": "http://music.163.com/song/media/outer/url?id=557581284.mp3"
    },
    {
        "content": "谁念过 千字文章 秋收冬已藏",
        "fav_nums": 2,
        "id": 7,
        "image": "http://127.0.0.1:5000/v1/music.4.png",
        "index": 7,
        "like_status": 1,
        "pubdate": "2018-08-14",
        "title": "不才《参商》",
        "type": 200,
        "url": "http://music.163.com/song/media/outer/url?id=557581284.mp3"
    }
]
```