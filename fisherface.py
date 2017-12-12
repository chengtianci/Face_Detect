#coding:utf-8
from numpy import *
from numpy import linalg as la
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import knn
import pdb

rows = 112
cols =92
ClassNum = 40
tol_num = 10
train_samplesize = 10
train = range(1,train_samplesize)
Eigen_num = 40
train_tol = 400
imagesize=cols*rows
def loadImageSet():
    FaceMat = mat(zeros((train_tol,imagesize)))
    label = mat(zeros((1,train_tol)))
    m=0
    for i in range(1,ClassNum+1):
        for j in range(1,train_samplesize+1):
            try:
                 img = cv2.imread('D:\PyCharm\PyCharmProjects\ORL\s'+str(i)+'_'+str(j)+'.bmp',0)
            except:
                print 'load %s failed'%i

            FaceMat[m,:] = mat(img).flatten()
            label[:,m] = i
            m = m + 1
    return FaceMat,label

def Eigenface(FaceMat,Eigen_num):
    NN,Train_num = shape(FaceMat)
    Mean_Image = mean(FaceMat,1)#参数为1，对各行求均值
    diffTrain = FaceMat - Mean_Image

    # V = mat(zeros((200,40)))
    eigvals, eigVects = linalg.eig(mat((diffTrain.T * diffTrain)/(Train_num-1)))
    eigSortIndex = argsort(-eigvals)  # 从大到小排序，默认从小到大，参数为负表示降序
    V = mat(eigVects[:, eigSortIndex[:Eigen_num]])#取特征向量的前四十维
    # print shape(eigvals)
    #print shape(V)
    #取前40大的特征值

    for i in range(1,Eigen_num+1):
        disc_value = mat(eigvals[eigSortIndex[:i]])


    disc_set = mat(zeros((NN,Eigen_num)))

    Train_set = diffTrain / sqrt(Train_num - 1)
    for k in range(0, Eigen_num):
        a = Train_set * V[:,k] #a为10000*1
        b =float (1/sqrt(disc_value[:,k]))
        disc_set[:,k] = b*a
    disc_set = real(disc_set)

    return disc_set,disc_value,Mean_Image

if __name__ == '__main__':
    FaceMat,label = loadImageSet()
    FaceMat_set = FaceMat.T
    disc_set,disc_value,MeanImage = Eigenface(FaceMat_set,Eigen_num)
    #训练样本的第一次投影
    train_pro = disc_set.T*FaceMat.T
    # print shape(disc_set.T)
    # print shape(train_pro)
    #训练样本总体均值及每类均值
    total_mean = mean(train_pro,1)
    EachClassMean = mat(zeros((Eigen_num,ClassNum)))
    EachClassNum = mat(zeros((1,ClassNum)))
    m=0
    temp = mat(zeros((Eigen_num,train_samplesize+1)))
    for i in range(1,ClassNum+1):
        for j in range(1,train_samplesize+1):
            temp[:,j]= train_pro[:,m]
            m=m+1
        EachClassMean[:,i-1] = mean(temp,1)

    #构造Fai_b,Fai_w,计算Sb，Sw

    Fai_b = mat(zeros((Eigen_num,ClassNum)))#每一类
    Fai_w = mat(zeros((Eigen_num,train_tol)))#总类

    #计算类间差
    temp1 = EachClassMean - total_mean
    Fai_b = sqrt(train_samplesize)*temp1

    # print EachClassMean[:,0]
    # print EachClassMean[:,1]
    #计算类内差
    for i in range(0,train_tol):
        Fai_w[:,i] = train_pro[:,i] - EachClassMean[:,int(label[0,i])-1]

    Sb = Fai_b*Fai_b.T
    Sw = Fai_w*Fai_w.T


    LDA_dim = ClassNum-1

    eig_val,eig_vec = linalg.eig(Sw.I*Sb)

    eigSortIndex = argsort(-eig_val)  # 从大到小排序，默认从小到大，参数为负表示降序
    W_LDA = mat(eig_vec[:, eigSortIndex[:LDA_dim]])  # 取LDA方向

    #训练样本再次投影
    train_final = W_LDA.T*train_pro

    #调用knn邻近分类器
    newImg = cv2.imread('D:\PyCharm\PyCharmProjects\s1_5.bmp',0)
    newImg = mat(newImg).flatten().T
    newImg_pro = disc_set.T*newImg
    newImg_final = W_LDA.T*newImg_pro

    Class = knn.classify0(newImg_final.T,train_final.T,label.T,7)
    print Class