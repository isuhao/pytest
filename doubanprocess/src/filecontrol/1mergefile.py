# encoding: utf-8
'''
Created on 2017年7月17日

@author: alibaba
'''
directName="data12"
foutIds=open('/Users/alibaba/Documents/workspace/python/alldata/'+directName+'/final_sina_id','a')
foutErr1=open('/Users/alibaba/Documents/workspace/python/alldata/'+directName+'/final_sina_err','a')
##foutErr2=open('./final_sina_err_nouser','w')
foutInfo=open('/Users/alibaba/Documents/workspace/python/alldata/'+directName+'/final_sina_info','a')
foutWeibo=open('/Users/alibaba/Documents/workspace/python/alldata/'+directName+'/final_sina_ids','a')
for i in range(0,40):
    idxstr=areastr(i)
    print idxstr
    finIds=open("../../../../alldata/"+directName+"/uid_sina_id_" + idxstr, 'r')
    rightout = open("../../../../alldata/"+directName+"/uid_sina_right_" + idxstr, 'r')
    errorout = open("../../../../alldata/"+directName+"/uid_sina_error_" + idxstr, 'r')
    sinaout = open("../../../../alldata/"+directName+"/uid_sina_info_" + idxstr, 'r')
    lines=finIds.readlines()
    foutIds.writelines(lines)
    del lines
    ##正式结果
    lines=rightout.readlines()
    foutWeibo.writelines(lines)
    del lines
    ##错误结果
    lines=errorout.readlines()
    foutErr1.writelines(lines)
    del lines
    ##微博信息
    lines=sinaout.readlines()
    foutInfo.writelines(lines)
    del lines
    finIds.close()
    rightout.close()
    errorout.close()
    sinaout.close()
foutWeibo.close()
foutInfo.close()
foutErr1.close()
##foutErr2.close()
