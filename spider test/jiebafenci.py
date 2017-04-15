#!/usr/bin/python
#-*- encoding:utf-8 -*-
import jieba

def splitSentence(inputFile,outputFile):
    fin=open(inputFile,'r')
    fout=open(outputFile,'w')

    for eachLine in fin:
        line=eachLine.strip().decode('utf-8','ignore')

        worldList=list(jieba.cut(line))
        outStr=''
        for word in worldList:
            outStr +=word
            outStr +='/'
        fout.write(outStr.strip().encode('utf-8')+'\n')

    fin.close()
    fout.close()
splitSentence('myInput.txt','myOutput.txt')