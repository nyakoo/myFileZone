import requests,os,shutil,time
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}
print('程序已开始执行')

#需要预先自行创建txt文本文件
with open('./单课单词列表.txt','r',encoding='UTF-8-sig') as file1:
    list1 = file1.readlines()
    enlist = []

#去除无关的空格和标点
for vol in list1:
    vol = vol.replace(' ','').replace('\n','').replace('\t','').replace('\r','').replace(',','')
    enlist.append(vol)
while '' in enlist:
    enlist.remove('')

#删除该文件夹和文件夹下所有文件
try:
    shutil.rmtree('./背诵单词音频')  
except:
    pass
#新建路径文件夹
os.mkdir('./背诵单词音频') 


n = 0
for vol in enlist:
    try:
        vol = vol.replace('\n','')
        shburl = 'https://media.shanbay.com/audio/us/{}.mp3'.format(vol)
        targetpath = './背诵单词音频/{}'.format(vol) + '.mp3'
        n += 1

#显示已完成的单词
        print(vol + '  {}/{}  √'.format(n,len(enlist))) 

        with open(targetpath,'wb') as file2:
            data = requests.get(shburl,headers=headers)
            file2.write(data.content)

    except:
        continue 

print('完成了 {} 个单词，1秒后自动退出'.format(n))
time.sleep(1)