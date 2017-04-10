# -*- coding: utf-8 -*-
#########################################################################
# Programm  : Avantes spectro python library for UNIX/LINUX system      #
# Path      : /home/Pi/control_commands/avaspec.py                      #
#                                                                       #
# Objectif  : POO library                                               #
#                                                                       #
# Author    : Samuel Marrazzo                                           #
# Date      : 05/09/2014                                                #
# Version   : Initiale version v0.5                                     #
#########################################################################

import numpy as np
import time
import usb.core as usbc
from consts import *
from dtype import *
import avtype as av
from matplotlib import pyplot as plot
from scipy.optimize import leastsq


def lorentzian(x,p):
    numerator =  (p[0]**2 )
    denominator = ( x - (p[1]) )**2 + p[0]**2
    y = p[2]*(numerator/denominator)
    return y

def residuals(p,y,x):
    err = y - lorentzian(x,p)
    return err


def array4toUintX(ar):
	out= ar[0]	
	for i in range(np.size(ar) - 1):
		out = out<<8|ar[i]
	return	out

def swapSingle(f1In):
    a = np.array(f1In,dtype='f4')
    a.dtype = np.dtype(('u1',4))
    a = a[::-1]
    f1Out = np.array(a)
    f1Out.dtype = np.dtype('f4')
    return f1Out[0]

def swap32(x):
    return (((x << 24) & 0xFF000000) |
            ((x <<  8) & 0x00FF0000) |
            ((x >>  8) & 0x0000FF00) |
            ((x >> 24) & 0x000000FF))
            
def swap16(x):
    return (((x <<  8) & 0xFF00)|((x >>  8) & 0x00FF))

class AS5216:
    
    
    def __init__(self):
        self.Device = usbc.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT)
        self.getVersionInfo()
        self.getDeviceConfig()
        self.buffin = np.zeros(63483,'u1')

    def __del__(self):
        self.Device.reset()
        return False    
    
    def writeAvs(self,cmd):
        if self.Device.write(ADR_WRITE,cmd,TIMEOUT) != len(cmd) :
            print "Bulk write failed"  
            return False
        return True

    def GET_ERROR(self,data=None):
        if data is None:
            print ERR_CODE[self.buffin[5]]
        if data[4] == 0x00:
            print ERR_CODE[data[5]]
            
    def readAvs(self,cmd,buff):
        
        return True
    
    """ Getters """
    
    def getDeviceConfig(self):
        self.writeAvs(GET_DEVICE_CONFIGURATION)
        self.DevCon = av.DeviceConfigType(np.array(self.Device.read(ADR_READ,DeviceConfigType.itemsize,TIMEOUT),dtype='u1'))
        self.NrPixels = swap16(self.DevCon.Detector.NrPixels)
        fit = self.DevCon.Detector.aFit
        fit[0] = swapSingle(fit[0])
        fit[1] = swapSingle(fit[1])
        fit[2] = swapSingle(fit[2])
        fit[3] = swapSingle(fit[3])
        fit[4] = swapSingle(fit[4])
        self.Lambda = lambda x: fit[0] + fit[1]*x*1.0 + fit[2]*(x**2)*1.0 +fit[3]*(x**3)*1.0 + fit[4]*(x**4)*1.0


    
    def getStoredMeas(self):
        self.writeAvs(GET_STORED_MEAS)        
            
        self.Spectrum = np.zeros(self.NrPixels,dtype='f8')
        self.sonySingleMeas = av.sony_single_measdatatype()
        request_size = sony_single_measdatatype.itemsize
        self.buffin[:request_size] = self.Device.read(ADR_READ,request_size,TIMEOUT)
        
        if self.buffin[4] == 0xB0:
            self.sonySingleMeas.copy(self.buffin[:request_size])
            for i in range(self.NrPixels):
                self.Spectrum[i]=swap16(self.sonySingleMeas.pixels[i])
            return True
        else:
            self.GET_ERROR()
            return False
        
    def getAvgStoredMeas(self):
        self.writeAvs(GET_AVG_STORED_MEAS) 
        
        self.Spectrum = np.zeros(self.NrPixels,dtype='f8')
        self.sonyMultiMeas  = av.sony_multi_measdatatype()
        request_size = sony_multi_measdatatype.itemsize
        self.buffin[:request_size] = self.Device.read(ADR_READ,request_size,TIMEOUT)
        
        if self.buffin[4] == 0xB1:
            self.sonyMultiMeas.copy(self.buffin[:request_size])
            if self.NrAvg != swap16(self.sonyMultiMeas.averages):
                print "Error in Number of Averages"
            for i in range(self.NrPixels):
                self.Spectrum[i]=swap32(self.sonyMultiMeas.pixels[i])/self.NrAv
            return True
        else:
            self.GET_ERROR()
            return False

    
    def getDigitalIn(self):
        
        return None
        
    def getAnalogIn(self):
        
        return None

    def getVersionInfo(self):
        self.writeAvs(GET_IDENT)
        self.AvsId = av.AvsIdentityType(np.array(self.Device.read(ADR_READ,AvsIdentityType.itemsize,TIMEOUT),dtype='u1'))
    
    def getResetReason(self):
        
        return None
        
    def getIdent(self):
        
        return None
        
    def getFile(self):
        
        return None
        
    def getFileLen(self):
        
        return None
        
    def getFirstFile(self):
        
        return None
        
    def getNextFile(self):
        
        return None
           
    
    """ """
    
    """ Setters """
        
    def setDeviceConfig(self):
        
        return None
    
    def setSDCard(self):
        
        return None
    
    def setAnalogOut(self):
        
        return None
          
    def setDigitalOut(self):
        
        return None          
   
    def setPWM(self):
        
        return None
        
    def setSyncMaster(self):
        
        return None
        
    def setTriggerMode(self):
        
        return None
        
        
    def setPrescanMode(self):
        
        return None
    """ """

    """ Other Methods """
   
    def PrepareMeasurement(self,
                           startPixel = 0,
                           stopPixel = 0,
                           IntegrationTime = 50,
                           IntegrationDelay =0,
                           NrAverages = 1,
                           NrOfScans = 1,
                           DarkCorrection = None,
                           Smoothing = None,
                           SatDetection = 0,
                           Trigger = None,
                           Control = None,
                           Prescan =0):
                               
        self.NrOfScans = np.short(NrOfScans)
        self.NrAvg = np.uint32(NrAverages)        
        
        self.PrepareMeasData = av.SendMeasConfigType()
        self.PrepareMeasData.prefix = PREPARE_MEASUREMENT
        self.PrepareMeasData.Meas.StartPixel = swap16(startPixel)
        if stopPixel:
            self.PrepareMeasData.Meas.StopPixel = swap16(stopPixel-1)
            self.aqNrPix = stopPixel - startPixel
            self.waveLength = self.Lambda(np.linspace(startPixel,stopPixel-1,self.aqNrPix))
        else:
            self.PrepareMeasData.Meas.StopPixel = swap16(self.NrPixels-1)
            self.aqNrPix = self.NrPixels -startPixel
            self.waveLength = self.Lambda(np.linspace(startPixel,self.NrPixels-1,self.aqNrPix))
        self.PrepareMeasData.Meas.IntegrationTime = swapSingle(IntegrationTime*1.0)
        
        
        
        self.PrepareMeasData.Meas.IntegrationDelay = swap32(IntegrationDelay)
        self.PrepareMeasData.Meas.NrAverages = swap32(NrAverages)
        if DarkCorrection is not None :
            self.PrepareMeasData.Meas.CorDynDark.Enable = DarkCorrection
        else:
            self.PrepareMeasData.Meas.CorDynDark.Enable =0
            self.PrepareMeasData.Meas.CorDynDark.ForgetPercentage = 0
        
        if Smoothing is not None :
            self.PrepareMeasData.Meas.Smoothing = Smoothing
        else:
            self.PrepareMeasData.Meas.Smoothing.SmoothPix = 0
            self.PrepareMeasData.Meas.Smoothing.SmoothModel = 0    
        
        self.PrepareMeasData.Meas.SaturationDetection = SatDetection
        
        if Trigger is not None :
            self.PrepareMeasData.Meas.Trigger = Trigger
        else:   
            self.PrepareMeasData.Meas.Trigger.Mode = 0
            self.PrepareMeasData.Meas.Trigger.Source =0
            self.PrepareMeasData.Meas.Trigger.SourceType = 0

        if Control is not None :
            self.PrepareMeasData.Meas.Control = Control
        else:
            self.PrepareMeasData.Meas.Control.StrobeControl = 0
            self.PrepareMeasData.Meas.Control.LaserDelay = 0
            self.PrepareMeasData.Meas.Control.LaserWidth= 0
            self.PrepareMeasData.Meas.Control.LaserWaveLength = 0
            self.PrepareMeasData.Meas.Control.StoreToRam = 0
        
        
        self.PMD = self.PrepareMeasData.asArrayUint8()
        
        self.writeAvs(self.PMD)
        #self.readAvs()
        self.buffin[:6] = self.Device.read(ADR_READ,self.buffin.size,TIMEOUT)
        
        if self.buffin[4] != 0x85:
            print "Error in prepare_measurement"
        
        self.writeAvs(SET_PRE_SCAN(Prescan))        
        self.buffin[:6] = self.Device.read(ADR_READ,self.buffin.size,TIMEOUT)
        
        
        self.Spectrum = np.zeros(self.aqNrPix,dtype='f8')
        self.sonySingleMeas = av.sony_single_measdatatype()
        self.sonyMultiMeas  = av.sony_multi_measdatatype()
        
        if self.NrAvg <= 1 :
            self.request_size = sony_single_measdatatype(self.aqNrPix).itemsize
        else:
            self.request_size = sony_multi_measdatatype(self.aqNrPix).itemsize

    
        

    def startMeasurement(self,v=False):

        
        
        if self.Device.write(ADR_WRITE,START_MEASUREMENT(self.NrOfScans),TIMEOUT) < 0:
            print "Bulk write failed"
        
        self.buffin[:6] = self.Device.read(ADR_READ,self.buffin.size,TIMEOUT)
        
        if self.buffin[4] != 0x86:
            print "Error in Start_measurement"
            return False
        measnr = 0
        while measnr < self.NrOfScans :
            start = time.time()
            self.buffin[:self.request_size] = self.Device.read(ADR_READ,self.request_size,TIMEOUT)
            if self.buffin[4] == 0xB0:
                self.sonySingleMeas.copy(self.buffin[:self.request_size],self.aqNrPix)
                for i in range(self.aqNrPix):
                    self.Spectrum[i]=swap16(self.sonySingleMeas.pixels[i])
            elif self.buffin[4] == 0xB1:
                self.sonyMultiMeas.copy(self.buffin[:self.request_size],self.aqNrPix)
                if self.NrAvg != swap16(self.sonyMultiMeas.averages):
                    print "Error in Number of Averages"
                for i in range(self.aqNrPix):
                    self.Spectrum[i]=swap32(self.sonyMultiMeas.pixels[i])/self.NrAvg
        
            measnr +=1
            if measnr < self.NrOfScans:
                if self.Device.write(ADR_WRITE,ACKNOWLEDGE,TIMEOUT) < 0:
                    print "Writing acknowledgement to COM1 failed"
            end = time.time()
            tot2 = end - start
            if v :            
                print " Data copy = "+str(tot2*1000)+"ms"

    def stopMeasurement(self):
       self.writeAvs(STOP_MEASUREMENT)
       
       if self.Device.read(ADR_READ,6,TIMEOUT)[4] != 0X8F:
           print "Error in stopping measurement"
       return None





    def startMeasurementToRAM(self):
        
        if self.Device.write(ADR_WRITE,START_MEASUREMENT(self.NrOfScans),TIMEOUT) < 0:
            print "Bulk write failed"
        
        self.buffin[:6] = self.Device.read(ADR_READ,self.buffin.size,TIMEOUT)
        
        if self.buffin[4] != 0x86:
            print "Error in Start_measurement"
            return False
        measnr = 0
        while measnr < self.NrOfScans :
            start = time.time()
            self.buffin[:self.request_size] = self.Device.read(ADR_READ,self.request_size,TIMEOUT)
            if self.buffin[4] == 0xB0:
                self.sonySingleMeas.copy(self.buffin[:self.request_size],self.aqNrPix)
                for i in range(self.aqNrPix):
                    self.Spectrum[i]=swap16(self.sonySingleMeas.pixels[i])
            elif self.buffin[4] == 0xB1:
                self.sonyMultiMeas.copy(self.buffin[:self.request_size],self.aqNrPix)
                if self.NrAvg != swap16(self.sonyMultiMeas.averages):
                    print "Error in Number of Averages"
                for i in range(self.aqNrPix):
                    self.Spectrum[i]=swap32(self.sonyMultiMeas.pixels[i])/self.NrAvg
        
            measnr +=1
            if measnr < self.NrOfScans:
                if self.Device.write(ADR_WRITE,ACKNOWLEDGE,TIMEOUT) < 0:
                    print "Writing acknowledgement to COM1 failed"
            end = time.time()
            tot2 = end - start
            print " Data copy = "+str(tot2*1000)+"ms"
        
        return 1





   
    def autoFit(self,bg_low,bg_high,hwhm,peak):
        
        x = self.waveLength
        y = self.Spectrum
        
        ind_bg_low = (x > min(x)) & (x < bg_low)
        ind_bg_high = (x > bg_high) & (x < max(x))
        
        x_bg = np.concatenate((x[ind_bg_low],x[ind_bg_high]))
        y_bg = np.concatenate((y[ind_bg_low],y[ind_bg_high]))
        
        m, c = np.polyfit(x_bg, y_bg, 1)
        
        # removing fitted background # 
        background = m*x + c
        y_bg_corr = y - background
        #pylab.plot(x,y_bg_corr)
        
        #########################################################################
        ############################# FITTING DATA ## ###########################
        
        # initial values #
        p = [hwhm,peak,self.Spectrum.max()]  # [hwhm, peak center, intensity] #
        
        # optimization # 
        pbest = leastsq(residuals,p,args=(y_bg_corr,x),full_output=1)
        best_parameters = pbest[0]
        
        # fit to data #
        self.fit = lorentzian(x,best_parameters)
        return None
   
    def specialMeasurement(self):
       
       return None
       
    def deleteFile(self):
       
       return None
       
    def saveSpectraToSDCard(self):
       
       return None
       
    def useHighResAdc(self):
        
        return None

    def getTemp(self,Trig,xmin=964,xmax=974,p=[0.5,968.35,1],minlim=20000,maxlim=65000, v=False):
        T  = lambda x: 38.46*x**2 + 141.9*x - 216.87
        self.startMeasurement()
        self.stopMeasurement() 
        maxSpectrum = self.Spectrum.max()
        if maxSpectrum < minlim :
            self.PrepareMeasurement(NrOfScans=1,IntegrationTime=1000,NrAverages=1,Trigger=Trig,startPixel=820,stopPixel=1100)
            self.startMeasurement()
            self.stopMeasurement() 
        elif maxSpectrum > maxlim :
            self.PrepareMeasurement(NrOfScans=1,IntegrationTime=10,NrAverages=1,Trigger=Trig,startPixel=820,stopPixel=1100)
            self.startMeasurement()
            self.stopMeasurement() 
        y = (self.Spectrum/maxSpectrum)
        ind_bg_low = (self.waveLength > min(self.waveLength)) & (self.waveLength < xmin)
        ind_bg_high = (self.waveLength > xmax) & (self.waveLength < max(self.waveLength))
        x_bg = np.concatenate((self.waveLength[ind_bg_low],self.waveLength[ind_bg_high]))
        y_bg = np.concatenate((y[ind_bg_low],y[ind_bg_high]))
        m, c = np.polyfit(x_bg, y_bg, 1)
        background = m*self.waveLength + c
        y_bg_corr = y - background
        
        pbest = leastsq(residuals,p,args=(y_bg_corr,self.waveLength),full_output=1)
        self.dL = pbest[0][0]
        self.Temp = T(pbest[0][0])
        if v :
            print "Temp Crystal = "+str(self.Temp)+"  dL = "+str(self.dL)
 
""" """

    
    



