import numpy as np
from consts import *
import dtype

""" Data type for Avantes spectra """
class ControlSettingsType:
    def __init__(self,data=None):
       if data is None :
           self.StrobeControl       = None
           self.LaserDelay          = None
           self.LaserWidth          = None
           self.LaserWaveLength     = None
           self.StoreToRam          = None
       else :
           if (data.dtype != dtype.ControlSettingsType) and (data.size == np.dtype(dtype.ControlSettingsType).itemsize):
                data.dtype = dtype.ControlSettingsType
           self.StrobeControl       = data['StrobeControl'][0]
           self.LaserDelay          = data['LaserDelay'][0]
           self.LaserWidth          = data['LaserWidth'][0]
           self.LaserWaveLength     = data['LaserWaveLength'][0]
           self.StoreToRam          = data['StoreToRam'][0]

    def copy(self,data):
        if (data.dtype != dtype.ControlSettingsType) and (data.size == np.dtype(dtype.ControlSettingsType).itemsize):
            data.dtype = dtype.ControlSettingsType
        self.StrobeControl       = data['StrobeControl'][0]
        self.LaserDelay          = data['LaserDelay'][0]
        self.LaserWidth          = data['LaserWidth'][0]
        self.LaserWaveLength     = data['LaserWaveLength'][0]
        self.StoreToRam          = data['StoreToRam'][0]
    
    def __del__(self):
        
        return 1

    def asArray(self):
        return np.array((self.StrobeControl,self.LaserDelay,self.LaserWidth,self.LaserWaveLength,self.StoreToRam),dtype=dtype.ControlSettingsType)

    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.ControlSettingsType.itemsize))
        return arr


class DarkCorrectionType:
    def __init__(self,data=None):
        if data is None :
            self.Enable              = None
            self.ForgetPercentage    = None
        else:
            if (data.dtype != dtype.DarkCorrectionType) and (data.size == np.dtype(dtype.DarkCorrectionType).itemsize):
               data.dtype = dtype.DarkCorrectionType
            self.Enable              = data['Enable'][0]
            self.ForgetPercentage    = data['ForgetPercentage'][0]
    
    def copy(self,data):
        if (data.dtype != dtype.DarkCorrectionType) and (data.size == np.dtype(dtype.DarkCorrectionType).itemsize):
           data.dtype = dtype.DarkCorrectionType
        self.Enable              = data['Enable'][0]
        self.ForgetPercentage    = data['ForgetPercentage'][0]
       
    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Enable, self.ForgetPercentage),dtype=dtype.DarkCorrectionType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.DarkCorrectionType.itemsize))
        return arr

class DetectorType:
    def __init__(self,data=None):
        if data is None :       
           self.SensorType          = None
           self.NrPixels            = None
           self.aFit                = None
           self.NLEnable            = None
           self.aNLCorrect          = None
           self.aLowNLCounts        = None
           self.aHighNLCounts       = None
           self.Gain                = None
           self.Reserved            = None
           self.Offset              = None
           self.ExtOffset           = None
           self.DefectivePixels     = None        
        else:
           if (data.dtype != dtype.DetectorType) and (data.size == np.dtype(dtype.DetectorType).itemsize):
               data.dtype = dtype.DetectorType
           self.SensorType          = data['SensorType'][0]
           self.NrPixels            = data['NrPixels'][0]
           self.aFit                = data['aFit'][0]
           self.NLEnable            = data['NLEnable'][0]
           self.aNLCorrect          = data['aNLCorrect'][0]
           self.aLowNLCounts        = data['aLowNLCounts'][0]
           self.aHighNLCounts       = data['aHighNLCounts'][0]
           self.Gain                = data['Gain'][0]
           self.Reserved            = data['Reserved'][0]
           self.Offset              = data['Offset'][0]
           self.ExtOffset           = data['ExtOffset'][0]
           self.DefectivePixels     = data['DefectivePixels'][0]

    def copy(self,data):
        if (data.dtype != dtype.DetectorType) and (data.size == np.dtype(dtype.DetectorType).itemsize):
            data.dtype = dtype.DetectorType
        self.SensorType          = data['SensorType'][0]
        self.NrPixels            = data['NrPixels'][0]
        self.aFit                = data['aFit'][0]
        self.NLEnable            = data['NLEnable'][0]
        self.aNLCorrect          = data['aNLCorrect'][0]
        self.aLowNLCounts        = data['aLowNLCounts'][0]
        self.aHighNLCounts       = data['aHighNLCounts'][0]
        self.Gain                = data['Gain'][0]
        self.Reserved            = data['Reserved'][0]
        self.Offset              = data['Offset'][0]
        self.ExtOffset           = data['ExtOffset'][0]
        self.DefectivePixels     = data['DefectivePixels'][0]


    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.SensorType, self.NrPixels, self.aFit, self.NLEnable, self.aNLCorrect, self.aLowNLCounts, self.aHighNLCounts, self.Gain, self.Reserved, self.Offset, self.ExtOffset, self.DefectivePixels),dtype=dtype.DetectorType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.DetectorType.itemsize))
        return arr



class SmoothingType:
    def __init__(self,data=None):
        if data is None :
           self.SmoothPix           = None
           self.SmoothModel         = None        
        else:
           if (data.dtype != dtype.SmoothingType) and (data.size == np.dtype(dtype.SmoothingType).itemsize):
               data.dtype = dtype.SmoothingType
           self.SmoothPix           = data['SmoothPix'][0]
           self.SmoothModel         = data['SmoothModel'][0]

    def copy(self,data):
        if (data.dtype != dtype.SmoothingType) and (data.size == np.dtype(dtype.SmoothingType).itemsize):
            data.dtype = dtype.SmoothingType
        self.SmoothPix           = data['SmoothPix'][0]
        self.SmoothModel         = data['SmoothModel'][0]


    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.SmoothPix, self.SmoothModel),dtype=dtype.SmoothingType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.SmoothingType.itemsize))
        return arr

class SpectrumCalibrationType:
    def __init__(self,data=None):
        if data is None :
           self.Smoothing           = SmoothingType()
           self.CalInttime          = None
           self.aCalibConvers       = None        
        else:    
           if (data.dtype != dtype.SpectrumCalibrationType) and (data.size == np.dtype(dtype.SpectrumCalibrationType).itemsize):
               data.dtype = dtype.SpectrumCalibrationType
           self.Smoothing           = SmoothingType(data['Smoothing'])
           self.CalInttime          = data['CalInttime'][0]
           self.aCalibConvers       = data['aCalibConvers'][0]

    def copy(self,data):
        if (data.dtype != dtype.SpectrumCalibrationType) and (data.size == np.dtype(dtype.SpectrumCalibrationType).itemsize):
            data.dtype = dtype.SpectrumCalibrationType
        self.Smoothing           = SmoothingType(data['Smoothing'])
        self.CalInttime          = data['CalInttime'][0]
        self.aCalibConvers       = data['aCalibConvers'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Smoothing.asArray(), self.CalInttime, self.aCalibConvers),dtype=dtype.SpectrumCalibrationType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.SpectrumCalibrationType.itemsize))
        return arr

class IrradianceType:
    def __init__(self,data=None):
        if data is None :
           self.IntensityCalib      = SpectrumCalibrationType()
           self.CalibrationType     = None
           self.FiberDiameter       = None        
        else:    
           if (data.dtype != dtype.IrradianceType) and (data.size == np.dtype(dtype.IrradianceType).itemsize):
               data.dtype = dtype.IrradianceType
           self.IntensityCalib      = SpectrumCalibrationType(data['IntensityCalib'])
           self.CalibrationType     = data['CalibrationType'][0]
           self.FiberDiameter       = data['FiberDiameter'][0]

    def copy(self,data):
        if (data.dtype != dtype.IrradianceType) and (data.size == np.dtype(dtype.IrradianceType).itemsize):
            data.dtype = dtype.IrradianceType
        self.IntensityCalib      = SpectrumCalibrationType(data['IntensityCalib'])
        self.CalibrationType     = data['CalibrationType'][0]
        self.FiberDiameter       = data['FiberDiameter'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.IntensityCalib.asArray(), self.CalibrationType, self.FiberDiameter),dtype=dtype.IrradianceType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.IrradianceType.itemsize))
        return arr

class TriggerType:
    def __init__(self,data=None): 
        if data is None :
           self.Mode                = None
           self.Source              = None
           self.SourceType          = None        
        else:        
           if (data.dtype != dtype.TriggerType) and (data.size == np.dtype(dtype.TriggerType).itemsize):
               data.dtype = dtype.TriggerType
           self.Mode                = data['Mode'][0]
           self.Source              = data['Source'][0]
           self.SourceType          = data['SourceType'][0]

    def copy(self,data):
        if (data.dtype != dtype.TriggerType) and (data.size == np.dtype(dtype.TriggerType).itemsize):
            data.dtype = dtype.TriggerType
        self.Mode                = data['Mode'][0]
        self.Source              = data['Source'][0]
        self.SourceType          = data['SourceType'][0]
  
    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Mode, self.Source, self.SourceType),dtype=dtype.TriggerType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.TriggerType.itemsize))
        return arr

class MeasConfigType:
    def __init__(self,data=None):   
        if data is None :
           self.StartPixel          = None
           self.StopPixel           = None
           self.IntegrationTime     = None
           self.IntegrationDelay    = None
           self.NrAverages          = None
           self.CorDynDark          = DarkCorrectionType()
           self.Smoothing           = SmoothingType()
           self.SaturationDetection = None
           self.Trigger             = TriggerType()
           self.Control             = ControlSettingsType()        
        else:        
           if (data.dtype != dtype.MeasConfigType) and (data.size == np.dtype(dtype.MeasConfigType).itemsize):
               data.dtype = dtype.MeasConfigType
           self.StartPixel          = data['StartPixel'][0]
           self.StopPixel           = data['StopPixel'][0]
           self.IntegrationTime     = data['IntegrationTime'][0]
           self.IntegrationDelay    = data['IntegrationDelay'][0]
           self.NrAverages          = data['NrAverages'][0]
           self.CorDynDark          = DarkCorrectionType(data['CorDynDark'])
           self.Smoothing           = SmoothingType(data['Smoothing'])
           self.SaturationDetection = data['SaturationDetection'][0]
           self.Trigger             = TriggerType(data['Trigger'])
           self.Control             = ControlSettingsType(data['Control'])

    def copy(self,data):
        if (data.dtype != dtype.MeasConfigType) and (data.size == np.dtype(dtype.MeasConfigType).itemsize):
            data.dtype = dtype.MeasConfigType
        self.StartPixel          = data['StartPixel'][0]
        self.StopPixel           = data['StopPixel'][0]
        self.IntegrationTime     = data['IntegrationTime'][0]
        self.IntegrationDelay    = data['IntegrationDelay'][0]
        self.NrAverages          = data['NrAverages'][0]
        self.CorDynDark          = DarkCorrectionType(data['CorDynDark'])
        self.Smoothing           = SmoothingType(data['Smoothing'])
        self.SaturationDetection = data['SaturationDetection'][0]
        self.Trigger             = TriggerType(data['Trigger'])
        self.Control             = ControlSettingsType(data['Control'])

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.StartPixel, self.StopPixel, self.IntegrationTime, self.IntegrationDelay, self.NrAverages, self.CorDynDark.asArray(), self.Smoothing.asArray(), self.SaturationDetection, self.Trigger.asArray(), self.Control.asArray()),dtype=dtype.MeasConfigType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.MeasConfigType.itemsize))
        return arr

class SendMeasConfigType:
    def __init__(self,data=None):
        if data is None :
           self.prefix              = None
           self.Meas                = MeasConfigType()
        else:
           if (data.dtype != dtype.SendMeasConfigType) and (data.size == np.dtype(dtype.SendMeasConfigType).itemsize):
               data.dtype = dtype.SendMeasConfigType
           self.prefix              = data['prefix'][0]
           self.Meas                = MeasConfigType(data['Meas'])
           
    def copy(self,data):
        if (data.dtype != dtype.SendMeasConfigType) and (data.size == np.dtype(dtype.SendMeasConfigType).itemsize):
            data.dtype = dtype.SendMeasConfigType
        self.prefix              = data['prefix'][0]
        self.Meas                = MeasConfigType(data['Meas'])

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.prefix, self.Meas.asArray()),dtype=dtype.SendMeasConfigType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.SendMeasConfigType.itemsize))
        return arr


class TimeStampType:
    def __init__(self,data=None):
        if data is None :
           self.Date                = None
           self.Time                = None        
        else:        
           if (data.dtype != dtype.TimeStampType) and (data.size == np.dtype(dtype.TimeStampType).itemsize):
               data.dtype = dtype.TimeStampType
           self.Date                = data['Date'][0]
           self.Time                = data['Time'][0]

    def copy(self,data):
        if (data.dtype != dtype.TimeStampType) and (data.size == np.dtype(dtype.TimeStampType).itemsize):
            data.dtype = dtype.TimeStampType
        self.Date                = data['Date'][0]
        self.Time                = data['Time'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Date, self.Time),dtype=dtype.TimeStampType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.TimeStampType.itemsize))
        return arr

class SDCardType:
    def __init__(self,data=None):
        if data is None :
           self.Enable              = None
           self.SpectrumType        = None
           self.aFileRootName       = None
           self.TimeStamp           = TimeStampType()        
        else:        
           if (data.dtype != dtype.SDCardType) and (data.size == np.dtype(dtype.SDCardType).itemsize):
               data.dtype = dtype.SDCardType
           self.Enable              = data['Enable'][0]
           self.SpectrumType        = data['SpectrumType'][0]
           self.aFileRootName       = data['aFileRootName'][0]
           self.TimeStamp           = TimeStampType(data['TimeStamp'])

    def copy(self,data):
        if (data.dtype != dtype.SDCardType) and (data.size == np.dtype(dtype.SDCardType).itemsize):
            data.dtype = dtype.SDCardType
        self.Enable              = data['Enable'][0]
        self.SpectrumType        = data['SpectrumType'][0]
        self.aFileRootName       = data['aFileRootName'][0]
        self.TimeStamp           = TimeStampType(data['TimeStamp'])

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Enable, self.SpectrumType, self.aFileRootName, self.TimeStamp.asArray()),dtype=dtype.SDCardType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.SDCardType.itemsize))
        return arr


class SpectrumCorrectionType:
    def __init__(self,data=None):
        if data is None :
            self.aSpectrumCorrect    = None
        else:        
            if (data.dtype != dtype.SpectrumCorrectionType) and (data.size == np.dtype(dtype.SpectrumCorrectionType).itemsize):
                data.dtype = dtype.SpectrumCorrectionType
            self.aSpectrumCorrect    = data['aSpectrumCorrect'][0]
            
    def copy(self,data):
        if (data.dtype != dtype.SpectrumCorrectionType) and (data.size == np.dtype(dtype.SpectrumCorrectionType).itemsize):
            data.dtype = dtype.SpectrumCorrectionType
        self.aSpectrumCorrect    = data['aSpectrumCorrect'][0]            
            
    def __del__(self):
        return 1
    
    def asArray(self):
        return self.aSpectrumCorrect
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.SpectrumCorrectionType.itemsize))
        return arr


class StandAloneType:
    def __init__(self,data=None):
        if data is None :
           self.Enable              = None
           self.Meas                = MeasConfigType()
           self.Nmsr                = None
           self.SDCard              = SDCardType()        
        else:
           if (data.dtype != dtype.StandAloneType) and (data.size == np.dtype(dtype.StandAloneType).itemsize):
               data.dtype = dtype.StandAloneType
           self.Enable              = data['Enable'][0]
           self.Meas                = MeasConfigType(data['Meas'])
           self.Nmsr                = data['Nmsr'][0]
           self.SDCard              = SDCardType(data['SDCard'])

    def copy(self,data):
        if (data.dtype != dtype.StandAloneType) and (data.size == np.dtype(dtype.StandAloneType).itemsize):
            data.dtype = dtype.StandAloneType
        self.Enable              = data['Enable'][0]
        self.Meas                = MeasConfigType(data['Meas'])
        self.Nmsr                = data['Nmsr'][0]
        self.SDCard              = SDCardType(data['SDCard'])

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Enable, self.Meas.asArray(), self.Nmsr, self.SDCard.asArray()),dtype=dtype.StandAloneType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.StandAloneType.itemsize))
        return arr

class TempSensorType:
    def __init__(self,data=None):
        if data is None :
            self.aFit                = None
        else:
            if (data.dtype != dtype.TempSensorType) and (data.size == np.dtype(dtype.TempSensorType).itemsize):
                data.dtype = dtype.TempSensorType
            if data['aFit'].size == 1 :
                self.aFit                = data['aFit'][0]
            else :
                self.aFit                = data['aFit']

    def copy(self,data):
        if (data.dtype != dtype.TempSensorType) and (data.size == np.dtype(dtype.TempSensorType).itemsize):
            data.dtype = dtype.TempSensorType
        if data['aFit'].size == 1 :
            self.aFit                = data['aFit'][0]
        else :
            self.aFit                = data['aFit']


    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array(self.aFit)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype('u1')
        return arr


class TecControlType:
    def __init__(self,data=None):
        if data is None :
           self.Enable              = None
           self.Setpoint            = None
           self.aFit                = None        
        else:        
           if (data.dtype != dtype.TecControlType) and (data.size == np.dtype(dtype.TecControlType).itemsize):
               data.dtype = dtype.TecControlType
           self.Enable              = data['Enable'][0]
           self.Setpoint            = data['Setpoint'][0]
           self.aFit                = data['aFit'][0]

    def copy(self,data):
        if (data.dtype != dtype.TecControlType) and (data.size == np.dtype(dtype.TecControlType).itemsize):
               data.dtype = dtype.TecControlType
        self.Enable              = data['Enable'][0]
        self.Setpoint            = data['Setpoint'][0]
        self.aFit                = data['aFit'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.Enable, self.Setpoint, self.aFit),dtype=dtype.TecControlType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.TecControlType.itemsize))
        return arr

class ProcessControlType:
    def __init__(self,data=None): 
        if data is None :
           self.AnalogLow           = None
           self.AnalogHigh          = None
           self.DigitalLow          = None
           self.DigitalHigh         = None        
        else:        
           if (data.dtype != dtype.ProcessControlType) and (data.size == np.dtype(dtype.ProcessControlType).itemsize):
               data.dtype = dtype.ProcessControlType
           self.AnalogLow           = data['AnalogLow'][0]
           self.AnalogHigh          = data['AnalogHigh'][0]
           self.DigitalLow          = data['DigitalLow'][0]
           self.DigitalHigh         = data['DigitalHigh'][0]

    def copy(self,data):
        if (data.dtype != dtype.ProcessControlType) and (data.size == np.dtype(dtype.ProcessControlType).itemsize):
            data.dtype = dtype.ProcessControlType
        self.AnalogLow           = data['AnalogLow'][0]
        self.AnalogHigh          = data['AnalogHigh'][0]
        self.DigitalLow          = data['DigitalLow'][0]
        self.DigitalHigh         = data['DigitalHigh'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.AnalogLow, self.AnalogHigh, self.DigitalLow, self.DigitalHigh),dtype=dtype.ProcessControlType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.ProcessControlType.itemsize))
        return arr

class DeviceConfigType:
    def __init__(self,data=None):
        if data is None :
           self.prefix              = None
           self.Len                 = None
           self.ConfigVersion       = None
           self.aUserFriendlyId     = None
           self.Detector            = DetectorType()
           self.Irradiance          = IrradianceType()
           self.Reflectance         = SpectrumCalibrationType()
           self.SpectrumCorrect     = SpectrumCorrectionType()
           self.StandAlone          = StandAloneType()
           
           self.aTemperature        = []
           self.aTemperature.append(TempSensorType())
               
           self.TecControl          = TecControlType()
           self.ProcessControl      = ProcessControlType()
           self.aReserved           = None
        else:        
           if (data.dtype != dtype.DeviceConfigType) and (data.size == np.dtype(dtype.DeviceConfigType).itemsize):
               data.dtype = dtype.DeviceConfigType
           self.prefix              = data['prefix'][0]
           self.Len                 = data['Len'][0]
           self.ConfigVersion       = data['ConfigVersion'][0]
           self.aUserFriendlyId     = data['aUserFriendlyId'][0]
           self.Detector            = DetectorType(data['Detector'])
           self.Irradiance          = IrradianceType(data['Irradiance'])
           self.Reflectance         = SpectrumCalibrationType(data['Reflectance'])
           self.SpectrumCorrect     = SpectrumCorrectionType(data['SpectrumCorrect'])
           self.StandAlone          = StandAloneType(data['StandAlone'])
           
           self.aTemperature        = []
           for i in range(data['aTemperature'][0].size):
               self.aTemperature.append(TempSensorType(data['aTemperature'][0][i]))
               
           self.TecControl          = TecControlType(data['TecControl'])
           self.ProcessControl      = ProcessControlType(data['ProcessControl'])
           self.aReserved           = data['aReserved'][0]

    def copy(self,data):
        
        if (data.dtype != dtype.DeviceConfigType) and (data.size == np.dtype(dtype.DeviceConfigType).itemsize):
            data.dtype = dtype.DeviceConfigType
        self.prefix              = data['prefix'][0]
        self.Len                 = data['Len'][0]
        self.ConfigVersion       = data['ConfigVersion'][0]
        self.aUserFriendlyId     = data['aUserFriendlyId'][0]
        self.Detector            = DetectorType(data['Detector'])
        self.Irradiance          = IrradianceType(data['Irradiance'])
        self.Reflectance         = SpectrumCalibrationType(data['Reflectance'])
        self.SpectrumCorrect     = SpectrumCorrectionType(data['SpectrumCorrect'])
        self.StandAlone          = StandAloneType(data['StandAlone'])
           
        self.aTemperature        = []
        for i in range(data['aTemperature'][0].size):
            self.aTemperature.append(TempSensorType(data['aTemperature'][0][i]))
               
        self.TecControl          = TecControlType(data['TecControl'])
        self.ProcessControl      = ProcessControlType(data['ProcessControl'])
        self.aReserved           = data['aReserved'][0]

    def tempAsArray(self):
        a = self.aTemperature[0].aFit       
        for i in range(len(self.aTemperature)-1):
            a = np.concatenate((a,self.aTemperature[i+1].aFit),axis=0)
        a.dtype = dtype.TempSensorType
        return a

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.prefix, self.Len, self.ConfigVersion, self.aUserFriendlyId, self.Detector.asArray(), self.Irradiance.asArray(), self.Reflectance.asArray(), self.SpectrumCorrect.asArray(), self.StandAlone.asArray(), self.tempAsArray(), self.TecControl.asArray(), self.ProcessControl.asArray(), self.aReserved),dtype=dtype.DeviceConfigType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.DeviceConfigType.itemsize))
        return arr

class AvsIdentityType:
    def __init__(self,data=None):
        if data is None :
           self.prefix              = None
           self.SwVersion           = None
           self.FPGAVersion         = None
           self.HwVersion           = None
           self.SerialNumber        = None
           self.UserFriendlyName    = None
           self.Status              = None        
        else:        
           if (data.dtype != dtype.AvsIdentityType) and (data.size == np.dtype(dtype.AvsIdentityType).itemsize):
               data.dtype = dtype.AvsIdentityType
           self.prefix              = data['prefix'][0]
           self.SwVersion           = data['SwVersion'][0]
           self.FPGAVersion         = data['FPGAVersion'][0]
           self.HwVersion           = data['HwVersion'][0]
           self.SerialNumber        = data['SerialNumber'][0]
           self.UserFriendlyName    = data['UserFriendlyName'][0]
           self.Status              = data['Status'][0]

    def copy(self,data):
        if (data.dtype != dtype.AvsIdentityType) and (data.size == np.dtype(dtype.AvsIdentityType).itemsize):
            data.dtype = dtype.AvsIdentityType
        self.prefix              = data['prefix'][0]
        self.SwVersion           = data['SwVersion'][0]
        self.FPGAVersion         = data['FPGAVersion'][0]
        self.HwVersion           = data['HwVersion'][0]
        self.SerialNumber        = data['SerialNumber'][0]
        self.UserFriendlyName    = data['UserFriendlyName'][0]
        self.Status              = data['Status'][0]

    def __del__(self):
        return 1
    
    def asArray(self):
        return np.array((self.prefix, self.SwVersion, self.FPGAVersion, self.HwVersion, self.SerialNumber, self.UserFriendlyName, self.Status),dtype=dtype.AvsIdentityType)
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.AvsIdentityType.itemsize))
        return arr
        
        
class sony_single_measdatatype:
    def __init__(self,data=None,nPix=None):
        if data is None :
            self.prefix             = np.zeros(SIZE_PREFIX,dtype='B')
            self.timestamp          = None
            self.deadpix            = np.zeros(MEAS_DEAD_PIX,dtype='u2')
            if nPix is None:
                self.pixels             = np.zeros(MEAS_PIXELS,dtype='u2')
            else :
                self.pixels             = np.zeros(nPix,dtype='u2')
        else:
            if (data.dtype != dtype.sony_single_measdatatype(nPix)) and (data.size == np.dtype(dtype.sony_single_measdatatype(nPix)).itemsize):
                   data.dtype = dtype.sony_single_measdatatype(nPix)
            self.prefix             = data['prefix'][0]
            self.timestamp          = data['timestamp'][0]
            self.deadpix            = data['deadpix'][0]
            self.pixels             = data['pixels'][0]
            
    def __del__(self):
        return 1
        
    def copy(self,data,nPix=None):
        if (data.dtype != dtype.sony_single_measdatatype(nPix)) and (data.size == np.dtype(dtype.sony_single_measdatatype(nPix)).itemsize):
                   data.dtype = dtype.sony_single_measdatatype(nPix)
        self.prefix             = data['prefix'][0]
        self.timestamp          = data['timestamp'][0]
        self.deadpix            = data['deadpix'][0]
        self.pixels             = data['pixels'][0]
        
    def asArray(self):
        return np.array((self.prefix,self.timestamp,self.deadpix,self.pixels),dtype=dtype.sony_single_measdatatype(self.pixels.size))
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.sony_single_measdatatype(self.pixels.size).itemsize))
        return arr  
        
class sony_multi_measdatatype:
    def __init__(self,data=None,nPix=None):
        if data is None :
            self.prefix             = np.zeros(SIZE_PREFIX,dtype='B')
            self.timestamp          = None
            self.averages           = None
            self.deadpix            = np.zeros(MEAS_DEAD_PIX,dtype='u4')
            if nPix is None:
                self.pixels             = np.zeros(MEAS_PIXELS,dtype='u4')
            else :
                self.pixels             = np.zeros(nPix,dtype='u4')
        else:
            if (data.dtype != dtype.sony_multi_measdatatype(nPix)) and (data.size == np.dtype(dtype.sony_multi_measdatatype(nPix)).itemsize):
                   data.dtype = dtype.sony_multi_measdatatype(nPix)
            self.prefix             = data['prefix'][0]
            self.timestamp          = data['timestamp'][0]
            self.averages           = data['averages'][0]
            self.deadpix            = data['deadpix'][0]
            self.pixels             = data['pixels'][0]
            
    def __del__(self):
        return 1
        
    def copy(self,data,nPix=None):
        if (data.dtype != dtype.sony_multi_measdatatype(nPix)) and (data.size == np.dtype(dtype.sony_multi_measdatatype(nPix)).itemsize):
                   data.dtype = dtype.sony_multi_measdatatype(nPix)
        self.prefix             = data['prefix'][0]
        self.timestamp          = data['timestamp'][0]
        self.averages           = data['averages'][0]
        self.deadpix            = data['deadpix'][0]
        self.pixels             = data['pixels'][0]        

    def asArray(self):
        return np.array((self.prefix,self.timestamp,self.averages,self.deadpix,self.pixels),dtype=dtype.sony_multi_measdatatype(self.pixels.size))
        
    def asArrayUint8(self):
        arr = self.asArray()
        arr.dtype = np.dtype(('u1',dtype.sony_multi_measdatatype(self.pixels.size).itemsize))
        return arr  
        