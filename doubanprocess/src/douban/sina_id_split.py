# encoding: utf-8
'''
Created on 2017年7月13日

@author: alibaba
'''
##每个文件的数据大小
filesize=151
dirName="data9"

fin = open("/Users/alibaba/Documents/workspace/python/pytest/doubanprocess/uid_sina_id_new3", 'r')
fileCt=0
totalCt=1
fout=open("/Users/alibaba/Documents/workspace/python/alldata/"+dirName+"/uid_sina_id_"+areastr(fileCt),'w')
for line in fin.readlines():
    totalCt+=1
    fout.write(line)
    fout.flush()
    if totalCt==filesize:
        fout.close()
        totalCt=1
        fileCt+=1
        fout=open("/Users/alibaba/Documents/workspace/python/alldata/"+dirName+"/uid_sina_id_"+areastr(fileCt),'w')
fout.close()
fin.close()