import time

import requests
import sqlUtils
import random
# total: 2322621
# total_pages: 116132

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": "Bearer",
    "businessId": "1",
    "Connection": "keep-alive",
    "content-type": "application/json",
    "Host": "xt.guxitk.com",
    "platformType": "weixin",
    "Referer": "https://servicewechat.com/wxf260eb6bd46deaab/devtools/page-frame.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "showType": "1",
    "User-Agent": "Mozilla/5.0(iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.06.2401020 MicroMessenger/8.0.5 Language/zh_CN webview/"
};

# 获取用户列表
def getUsers(page):
    print("当前爬取页面",page)
    data = {};
    url = "https://xt.guxitk.com/api/merchant/authorList?pageSize=20&pageNum="+str(page)
    response = requests.get(url, headers=headers)
    print(response);
    # 检查请求是否成功
    if response.status_code == 200:
        data1 = response.json()  # 获取响应的 JSON 数据
        data = data1['data']["records"]
        for item in data:
            print(item)
            sqlUtils.addImgUser(item["id"],item["artworks_num"],item["audit_status"],item["avatar"],item["business_id"],item["client_sort"],item["created_at"],item["hot_value"],item["is_recommend"],item["like_num"],item["merchant_id"],item["mini_sort"],item["name"],item["recommend_sort"],item["show_make"],item["sort"],item["user_id"]);
        if(len(data)==20):
            random_number = random.randint(1, 5)
            print("睡眠秒钟数",random_number);
            time.sleep(random_number)  # 暂停1秒钟
            getUsers(page+1);
        else:
            print("最后页面数",page,"用户数",len(data))
    else:
        print("请求失败，状态码：", response.status_code)
# 获取图片列表
def getImages(merchant_id,user_id,author_id,pageNum,pageSize,sqlIndex,id1):
    print("用户ID",user_id,"页数",pageNum,"数据库下表",sqlIndex);
    dataTxt="merchant_id="+merchant_id+"&user_id="+user_id+"&author_id="+author_id+"&pageNum="+str(pageNum)+"&pageSize="+str(pageSize)+"&sort_type=1&type=";
    url="https://xt.guxitk.com/api/artworks/artworksListByAuthorId?"+dataTxt;
    response = requests.get(url, headers=headers)
    # 检查请求是否成功
    if response.status_code == 200:
        data1 = response.json()  # 获取响应的 JSON 数据
        data = data1['data']["records"]
        print("总数据---", data1);
        print("当前页获取到的图片数量",len(data));
        for item in data:
            print("图片数据开始-->",item);
            sqlUtils.yxtkGetImgInfo(item["id"],item["user_id"],item["merchant_id"],item["like_num"],item["cover_url"],item["audit_status"],item["type"]);
        if(len(data)==32):
            random_number = random.randint(1, 5)
            print("睡眠秒钟数", random_number);
            time.sleep(random_number)  # 暂停1秒钟
            getImages(merchant_id, user_id, author_id, pageNum+1, pageSize, sqlIndex,id1);
        else:
            # 修改爬取标志
            sqlUtils.updateUser(id1);

            getUserNoGet();
    else:
        print("请求失败，状态码：", response.status_code)


def getImages1_(merchant_id,user_id,author_id,pageNum,pageSize,sqlIndex,id1):
    print("用户ID",user_id,"页数",pageNum,"数据库下表",sqlIndex);
    dataTxt="merchant_id="+merchant_id+"&user_id="+user_id+"&author_id="+author_id+"&pageNum="+str(pageNum)+"&pageSize="+str(pageSize)+"&sort_type=1&type=";
    url="https://xt.guxitk.com/api/artworks/artworksListByAuthorId?"+dataTxt;
    response = requests.get(url, headers=headers)
    # 检查请求是否成功
    if response.status_code == 200:
        data1 = response.json()  # 获取响应的 JSON 数据
        data = data1['data']["records"]
        print("总数据---", data1);
        print("当前页获取到的图片数量",len(data));
        for item in data:
            print("图片数据开始-->",item);
            sqlUtils.yxtkGetImgInfo(item["id"],item["user_id"],item["merchant_id"],item["like_num"],item["cover_url"],item["audit_status"],item["type"]);
        if(len(data)==32):
            random_number = random.randint(1, 5)
            print("睡眠秒钟数", random_number);
            time.sleep(random_number)  # 暂停1秒钟
            getImages(merchant_id, user_id, author_id, pageNum+1, pageSize, sqlIndex,id1);
        else:
            # 修改爬取标志
            sqlUtils.updateUser(id1);

            getUserNoGet();
    else:
        print("请求失败，状态码：", response.status_code)

def getUserNoGet():
    userList=sqlUtils.getUserNoGetImgs();
    for index,row in enumerate(userList):
        print("",row)
        # print(row[11], row[18], row[0],1,32)

        random_number = random.randint(1, 5)
        print("睡眠秒钟数", random_number);
        time.sleep(random_number)  # 暂停1秒钟

        author_id=getAuto(str(row[11]), str(row[18]),str(row[0]));
        print("author_id--授权ID",author_id);
        if(author_id!=-1):
            getImages(str(row[11]), str(row[18]),str(author_id),1,32,index,row[0]);
        else:
            sqlUtils.updateUser(row[0]);
            getUserNoGet();
    # if(len(userList)==100):
    #     getUserNoGet();

# 获取autoid
def getAuto(merchant_id,user_id,id1):
    url="https://xt.guxitk.com/api/merchant/authorInfoById?merchant_id="+str(merchant_id)+"&user_id="+str(user_id)+"&id="+str(id1)+"&code=";
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data1 = response.json()  # 获取响应的 JSON 数据
        data = data1['data']["info"]['codeInfo']
        if(len(data)>0):
            data = data1['data']["info"]['codeInfo'][0]['author_id']
            return data;
        else:
            return -1;
    else:
        print("请求失败，状态码：", response.status_code)
        return -1;


if __name__ == "__main__":
    # getUserNoGet();
    # getUsers(108);
    # getImages();
    # merchant_id=19426&user_id=33265264&author_id=23835&pageNum=1&pageSize=32&sort_type=1&type=
    getImages1_('19426',33265264,);
