# old-land-flask-api
# API说明
* 点赞和取消点赞接口需要携带token
* token必须通过小程序的code换取
* 无论是提交数据还是返回数据只支持json
* API遵从严格的HTTP动作并采用标准的 Http Status Code 作为响应状态，建议采用HTTP状态码作为Api调用是否成功的标识,具体异常请通过错误码判断

# 返回码
 - HTTP状态码
 
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


- 错误码

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

