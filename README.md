# DAllE-ProxyCozeForVercel

## 介绍
`dalle-proxyCozeForvercel`是利用由[coze](https://www.coze.com)支持的机器人（目前是Telegram和Discord），提供免费访问OpenAI的DALL·E 3图像生成的代理服务。项目提供了一个符合OpenAI标准的API端点，允许开发者轻松地将此DALL·E 3代理服务集成到他们的应用程序中。

## [#](https://github.com/libaxuan/dalle-proxyCozeForvercel)前置


1. 所处网络需在国外
    
2. 一个 `Coze` 账号
    
3. 一个 `Discord` 账号
 
    

## [#](https://discord.gg)Discord

**Discord官网：[https://discord.com(opens new window)](https://discord.com/)**

### [#]()创建服务器

先在 Discord 首页创建服务器

![Pasted image 20240228114031.png](data%2Fimages%2FPasted%20image%2020240228114031.png)

之后 `亲自创建` ，下面随便选择的，我选的 `仅供我和我的朋友使用`
### [#]()创建Discord应用

[Discord开发者平台 (opens new window)](https://discord.com/developers/)创建1个 `Application` ，应用程序的类型为Bot

![![Pasted image 20240228101723.png](data%2Fimages%2FPasted%20image%2020240228101723.png)]

两个应用创建的步骤流程一致，都按照下面的步骤进行操作即可！确保创建完成之后保存对应的token

点击 `Bot`  再点击  `Reset Token` 获取 `Token` 复制保存到其它地方
![Pasted image 20240228102818.png](data%2Fimages%2FPasted%20image%2020240228102818.png)

> 配置对应的权限：

往下滑

**注意：**这个权限我们只需要把与coze bot进行关联的应用的权限开启即可，另外一个主动向coze bot发消息的应用无需开启！！

![Pasted image 20240228102858.png](data%2Fimages%2FPasted%20image%2020240228102858.png)

选择 bot

![Pasted image 20240228103043.png](data%2Fimages%2FPasted%20image%2020240228103043.png)

往下滑，选择权限

![Pasted image 20240228103246.png](data%2Fimages%2FPasted%20image%2020240228103246.png)

打开上图复制的链接

添加应用到频道

![Pasted image 20240228103406.png](data%2Fimages%2FPasted%20image%2020240228103406.png)

![Pasted image 20240228103422.png](data%2Fimages%2FPasted%20image%2020240228103422.png)

### [#]()**创建Coze Bot**

**Coze官网：[https://www.coze.com(opens new window)](https://www.coze.com/)**

访问 `Coze` 官网，注册账号，目前支持 `Google` 账号和手机号注册（中国大陆地区的手机号也可以）

1. 点击 `Create Bot` 创建一个Bot
2. 创建完后发布

点进去我们创建的机器人
![Pasted image 20240228103625.png](data%2Fimages%2FPasted%20image%2020240228103625.png)

选择模型
![Pasted image 20240228103741.png](data%2Fimages%2FPasted%20image%2020240228103741.png)

右上角按钮发布


选择 Discord，之后会让输入一个 token ，那个就是之前创建保存的

![Pasted image 20240228103953.png](data%2Fimages%2FPasted%20image%2020240228103953.png)

发布之后就能看到机器人在线了

![Pasted image 20240228104203.png](data%2Fimages%2FPasted%20image%2020240228104203.png)

开启`开发者模式`

![Pasted image 20240228104248.png](data%2Fimages%2FPasted%20image%2020240228104248.png)

![Pasted image 20240228104323.png](data%2Fimages%2FPasted%20image%2020240228104323.png)

复制由coze托管的机器人ID：

![Pasted image 20240228104716.png](data%2Fimages%2FPasted%20image%2020240228104716.png)

服务器id：

![Pasted image 20240228104751.png](data%2Fimages%2FPasted%20image%2020240228104751.png)

频道id：

![Pasted image 20240228104823.png](data%2Fimages%2FPasted%20image%2020240228104823.png)

## [#]()**搭建Coze代理**

使用本项目：[https://github.com/libaxuan/dalle-proxyCozeForvercel]()

使用 Pycharm 或其他工具导入项目，**启动前需要修改配置文件**

注：国内网络通不了，需配置proxy
### Python执行
如果你想直接用Python运行代理服务，你可以按照这些步骤操作：（确保你的机器上安装了Python 3.8+。）

1. 克隆仓库：
   ```bash
   git clone https://github.com/libaxuan/dalle-proxyCozeForvercel.git
   ```
2. 进入到克隆下来的目录：
   ```bash
   cd dall-e-vercel-coze
   ```
3. 安装必要的Python依赖项：
   ```bash
   pip3 install -r requirements.txt
   或者
   pip3 install -r requirements.txt --break-system-packages
   ```
4. 根据提示在项目`data/.env`文件中配置你的相关参数
   ```bash
   cp data/.env.example data/.env
   vim data/.env
   ```
5. 运行代理服务器（python或uvicorn）：
   ```bash
   # 使用python
   python main.py
   # 或使用uvicorn
   uvicorn main:api.app
   ```
代理服务现在将可以在配置的端口（默认：8000）上访问。

启动成功后，控制台会返回 `JDA` 的日志输出： `INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`

![Pasted image 20240228104608.png](data%2Fimages%2FPasted%20image%2020240228104608.png)

本地服务效果

![Pasted image 20240228105906.png](data%2Fimages%2FPasted%20image%2020240228105906.png)


## [#]()使用

接口文档基于 fastapi 生成
http://127.0.0.1:8000/docs#/
![Pasted image 20240228105030.png](data%2Fimages%2FPasted%20image%2020240228105030.png)
> 以 potman 为例子：
![Pasted image 20240228105430.png](data%2Fimages%2FPasted%20image%2020240228105430.png)

![Pasted image 20240228105659.png](data%2Fimages%2FPasted%20image%2020240228105659.png)
本地服务效果

![Pasted image 20240228105906.png](data%2Fimages%2FPasted%20image%2020240228105906.png)
本接口文档：http://127.0.0.1:8000/docs#/
![Pasted image 20240228121334.png](data%2Fimages%2FPasted%20image%2020240228121334.png)
```
curl --location 'http://127.0.0.1:8000/v1/images/generations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 0000' \
--data '{
    "prompt": "A Tesla car",
    "model": "dall-e-3",
    "n": 1,
    "quality": "standard",
    "response_format": "url",
    "size": "1024x1024",
    "style": "vivid",
    "user": "free-dall-e-user",
    "platform": "discord"
}'
```
   ## 以下是响应：
   ```bash
   {
    "data": [
        {
            "url": "https://p16-flow-sign-sg.ciciai.com/ocean-cloud-tos-sg/0bd6f6938a13493793e203eaf0b2048b.png~tplv-0es2k971ck-image.png?rk3s=18ea6f23&x-expires=1740624837&x-signature=13QAXDddM8smC7t6rJ0OPMvfXOc%3D",
            "revised_prompt": "A Tesla car"
        }
    ]
}
  ```
## 支持

### [技术交流-discord](https://discord.gg/CJqT93bz)
### [技术交流vx](https://m.qpic.cn/psc?/V504mQ6B3aNgg24a240d0gcbdb0Ts5fz/ruAMsa53pVQWN7FLK88i5qZeucLMKtT5QNvZcgyjfMczuKC08kkaUO.pkQ4TtUM.DKkGBSIvKkBNeMKbZ5MyOv0.XIJ47ojxLC2r32Nj7iQ!/b&bo=*AL6A*wC.gMBByA!&rf=viewer_4)
### [技术交流vx qun](https://iili.io/JGyUgn4.jpg)


## 免责声明

该项目是`开源`的，仅用于学习目的。不得用于任何非法活动。

<details><summary>📝 License</summary>
</details>

This project is [MIT](./LICENSE.txt) licensed.
Copyright © 2023 [dalle-proxyCozeForvercel]

---
