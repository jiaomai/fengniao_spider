import requests
import json
import csv
import sys
import argparse
import os

class Easy:
    def __init__(self,args) -> None:
        self.keyword = args.keyword
        self.page = args.page
        self.file = args.file
        self.list_file = args.list_file

    def data_collection(self,url):
        headers = {"Sec-Ch-Ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"","App-Device": "H5","App-Version": "lasted","App-Fromplatform": "tencent","Mobile-Brand": "","Mobile-Model": "","Sec-Ch-Ua-Mobile": "?0","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","App-Env": "prod","Sec-Ch-Ua-Platform": "\"Windows\"","Accept": "*/*","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://m.riskbird.com/h5/pages/query/company/index/index","Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,zh;q=0.9","Connection": "close"}
        resp = requests.get(url,headers=headers)
        if "No message available" in resp.text:
            print("查询条件不满足，请修改查询关键词或查询数量")
            sys.exit()
        return resp.json()

    def data_processing(self,resp):
        data_first = resp
        data_secode = data_first['data']
        del data_first['data']
        print('-----------------------------------')
        for key in data_first.keys():
            print('[+]'+key+' : '+str(data_first[key]))
        # print(data_secode)
        return data_secode

    def data_save(self,data_secode,file):
        csv_file = open('./result/'+ file + '.csv','w+',newline='',encoding='utf-8')
        list_resp = list(data_secode[0].keys())

        # print(list_resp)
        json_writer = csv.DictWriter(csv_file, fieldnames=list_resp)
        json_writer.writeheader()  # 写入CSV表头
        for item in data_secode:
            json_writer.writerow(item) # 写入数据记录
        csv_file.close()
    
    def main(self):
        if self.keyword:
            if self.file:
                file = self.file
            else:
                file = self.keyword
            url =  'https://m.riskbird.com/prod-qbb-api/newSearch?idUser=126350&searchKey={}&pageNo=1&range={}'.format(self.keyword,self.page)
            self.data_save(self.data_processing(self.data_collection(url)),file)
        else:
            with open(self.list_file,'r',newline='',encoding='utf-8') as f:
                lines = f.readlines()
                for keyword in lines:
                    file = keyword.strip()
                    url = 'https://m.riskbird.com/prod-qbb-api/newSearch?idUser=126350&searchKey={}&pageNo=1&range={}'.format(keyword.strip(),self.page)
                    self.data_save(self.data_processing(self.data_collection(url)),file)

def mkdir_irectory():
    # 要创建的目录名称
    directory_name = 'result'

    # 获取当前工作目录
    current_directory = os.getcwd()

    # 新目录的完整路径
    new_directory_path = os.path.join(current_directory, directory_name)
    if not os.path.exists(new_directory_path):
        # 创建新目录
        os.mkdir(new_directory_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', help='Name argument')
    parser.add_argument('-p', '--page', default=10, type=int, help='Page argument')
    parser.add_argument('-f', '--file', help='file argument')
    parser.add_argument('-r', '--list_file', help='Keylist file')
    mkdir_irectory()
    args = parser.parse_args()
    # print(args)
    if not args.keyword and not args.list_file:
        print('Usage: script.py -k <keyword> -p <page> -f <file> -m <manage> -f <list_file>')
        sys.exit(1)   
    easy = Easy(args)
    easy.main()
    

if __name__=='__main__':
    try:
        main()
    except PermissionError:
        print('[-]'+"执行错误！")
        print('[-]'+"尝试关闭打开的csv导出文件")