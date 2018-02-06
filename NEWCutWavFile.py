#coding=gbk

'''
Created on 2015��12��28��

@author: Gang
'''



import wave
import numpy as np
import pylab as plt

CutTimeDef = 240 #��240ms�ض��ļ�
CutFrameNum =0
musicPrimaryName = "ׯ���� - ������"

musicPrimaryName = "��������"
FileName = ".\Music\\"+musicPrimaryName + ".wav"


def SetFileName(WavFileName):
    global  FileName
    print("SetFileName File Name is ", FileName)
    FileName = WavFileName;
def CutFile():
    global  FileName
    print("CutFile File Name is ",FileName)
    # ��wav�ļ� ��open����һ������һ��Wave_read���ʵ����ͨ���������ķ�����ȡWAV�ļ��ĸ�ʽ�����ݡ�
    f = wave.open(r"" + FileName, "rb")
    # ��ȡ��ʽ��Ϣ
    # һ���Է������е�WAV�ļ��ĸ�ʽ��Ϣ�������ص���һ����Ԫ(tuple)��������, ����λ����byte��λ��, ��
    # ��Ƶ��, ��������, ѹ������, ѹ�����͵�������waveģ��ֻ֧�ַ�ѹ�������ݣ���˿��Ժ������������Ϣ
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    CutFrameNum = framerate * CutTimeDef / 1000
    print("CutFrameNum=%d" % (CutFrameNum))

    print("nchannels=%d" % (nchannels))
    print("sampwidth=%d" % (sampwidth))
    print("framerate=%d" % (framerate))
    print("nframes=%d" % (nframes))
    str_data = f.readframes(nframes)
    f.close()  # ����������ת��������
    # ��Ҫ������������������λ������ȡ�Ķ���������ת��Ϊһ�����Լ��������
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    temp_data = wave_data.T
    # StepNum = int(nframes/200)
    StepNum = int(CutFrameNum);
    StepTotalNum = 0;
    haha = 0
    while StepTotalNum < nframes:
        print("Stemp=%d" % (haha))
        FileName = ".\MusicResult\\" + "0_" + "SampleVoice_" + str(haha) + ".wav"
        print(FileName)
        temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
        haha = haha + 1;
        StepTotalNum = haha * StepNum;

        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)  # ��WAV�ĵ�
        f = wave.open(r"" + FileName, "wb")  #
        # ����������������λ����ȡ��Ƶ��
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        # ��wav_dataת��Ϊ����������д���ļ�
        f.writeframes(temp_dataTemp.tostring())
        f.close()