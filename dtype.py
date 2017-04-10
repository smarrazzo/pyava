import numpy as np
from consts import *

""" Data type for Avantes spectra """
#       ControlSettingsType size 16 bytes   0x10
ControlSettingsType = np.dtype({
            'names' :[
                    'StrobeControl',
                    'LaserDelay',
                    'LaserWidth',
                    'LaserWaveLength',
                    'StoreToRam'],
            'formats': [
                    'u2',
                    'u4',
                    'u4',
                    'f4',
                    'u2']})
       
#      DarkCorrectionType size 2 Bytes    0x02             
DarkCorrectionType = np.dtype({
            'names' :[
                    'Enable',
                    'ForgetPercentage'],
            'formats': [
                    'u1',
                    'u1']})
                              
#       DetectorType    size 188 Bytes  0xBC
DetectorType = np.dtype({
            'names' :[
                    'SensorType',
                    'NrPixels',
                    'aFit',
                    'NLEnable',
                    'aNLCorrect',
                    'aLowNLCounts',
                    'aHighNLCounts',
                    'Gain',
                    'Reserved',
                    'Offset',
                    'ExtOffset',
                    'DefectivePixels'],
            'formats':[
                    'u1',
                    'u2',
                    ('f4',NR_WAVELEN_POL_COEF),
                    'b',
                    ('f8',NR_NONLIN_POL_COEF),
                    'f8',
                    'f8',
                    ('f4',MAX_VIDEO_CHANNELS),
                    'f4',
                    ('f4',MAX_VIDEO_CHANNELS),
                    'f4',
                    ('u2',NR_DEFECTIVE_PIXELS)]})

#       SmoothingType size 3 Bytes  0x03
SmoothingType = np.dtype({
            'names' :[
                    'SmoothPix',
                    'SmoothModel'],
            'formats':[
                    'u2',
                    'u1']})


#       SpectrumCalibrationType Size 16391 Bytes 0x4007
SpectrumCalibrationType = np.dtype({
            'names' :[
                    'Smoothing',
                    'CalInttime',
                    'aCalibConvers'],
            'formats': [
                    SmoothingType,
                    'f4',
                    ('f4',MAX_NR_PIXELS)]})


#       IrradianceType Size 5 Bytes     0x05
IrradianceType = np.dtype({
            'names' :[
                    'IntensityCalib',
                    'CalibrationType',
                    'FiberDiameter'],
            'formats': [
                    SpectrumCalibrationType,
                    'u1',
                    'u4']})

#       TriggerType Size 3 Bytes    0x03
TriggerType = np.dtype({
            'names' :[
                    'Mode',
                    'Source',
                    'SourceType'],
            'formats':[
                    'u1',
                    'u1',
                    'u1']})

#       MeasConfigType Size 41 Bytes 0x29
MeasConfigType = np.dtype({
            'names' :[
                    'StartPixel',
                    'StopPixel',
                    'IntegrationTime',
                    'IntegrationDelay',
                    'NrAverages',
                    'CorDynDark',
                    'Smoothing',
                    'SaturationDetection',
                    'Trigger',
                    'Control'],
            'formats':[
                    'u2',
                    'u2',
                    'f4',
                    'u4',
                    'u4',
                    DarkCorrectionType,
                    SmoothingType,
                    'u1',
                    TriggerType,
                    ControlSettingsType]})

#       SendMeasConfigType Size 47 Bytes 0x2F
SendMeasConfigType = np.dtype({
            'names' :[
                    'prefix',
                    'Meas'],
            'formats': [
                    ('u1',SIZE_PREFIX),
                    MeasConfigType]})

#       TimeStampType Size 4 Bytes  0x04
TimeStampType = np.dtype({
            'names' :[
                    'Date',
                    'Time'],
            'formats':[
                    'u2',
                    'u2']})

#       SDCardType Size 12 Bytes 0x0C
SDCardType = np.dtype({
            'names' :[
                    'Enable',
                    'SpectrumType',
                    'aFileRootName',
                    'TimeStamp'],
            'formats':[
                    'b',
                    'u1',
                    'a'+str(ROOT_NAME_LEN),
                    TimeStampType]})

#       SpectrumCorrectionType Size 16384 Bytes 0x4000
SpectrumCorrectionType = np.dtype([('aSpectrumCorrect','f4',MAX_NR_PIXELS)])


#       StandAloneType Size 56 Bytes 0x38
StandAloneType = np.dtype({
            'names' :[
                    'Enable',
                    'Meas',
                    'Nmsr',
                    'SDCard'],
            'formats':[
                    'b',
                    MeasConfigType,
                    'i2',
                    SDCardType]})

#       TempSensorType size 20 Bytes    0x14
TempSensorType = np.dtype([('aFit','f4',NR_TEMP_POL_COEF)])

#       TecControlType Size 13 Bytes 0x0D
TecControlType = np.dtype({
            'names' :[
                    'Enable',
                    'Setpoint',
                    'aFit'],
            'formats':[
                    'b',
                    'f4',
                    ('f4',NR_DAC_POL_COEF)]})

#       ProcessControlType Size 96 Bytes 0x60
ProcessControlType = np.dtype({
            'names' :[
                    'AnalogLow',
                    'AnalogHigh',
                    'DigitalLow',
                    'DigitalHigh'],
            'formats': [
                    ('f4',2),
                    ('f4',2),
                    ('f4',10),
                    ('f4',10)]})

""" """
SETTINGS_RESERVED_LEN   = 62*1024 -  (np.dtype('u4').itemsize + np.dtype('u2').itemsize + np.dtype('u2').itemsize + USER_ID_LEN + DetectorType.itemsize + IrradianceType.itemsize + SpectrumCalibrationType.itemsize + SpectrumCorrectionType.itemsize + StandAloneType.itemsize + TempSensorType.itemsize*MAX_TEMP_SENSORS + TecControlType.itemsize + ProcessControlType.itemsize)
""" """

#       DeviceConfigType Size 63490 Bytes   0xF802
DeviceConfigType = np.dtype({
            'names' :[
                    'prefix',
                    'Len',
                    'ConfigVersion',
                    'aUserFriendlyId',
                    'Detector',
                    'Irradiance',
                    'Reflectance',
                    'SpectrumCorrect',
                    'StandAlone',
                    'aTemperature',
                    'TecControl',
                    'ProcessControl',
                    'aReserved'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u2',
                    'u2',
                    'a'+str(USER_ID_LEN),
                    DetectorType,
                    IrradianceType,
                    SpectrumCalibrationType,
                    SpectrumCorrectionType,
                    StandAloneType,
                    (TempSensorType,MAX_TEMP_SENSORS),
                    TecControlType,
                    ProcessControlType,
                    ('u1',SETTINGS_RESERVED_LEN)]})
     
#       AvsIdentityType Size 92 Bytes   0X5C
AvsIdentityType = np.dtype({
            'names' :[
                    'prefix',
                    'SwVersion',
                    'FPGAVersion',
                    'HwVersion',
                    'SerialNumber',
                    'UserFriendlyName',
                    'Status'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u4',
                    'u4' ,'u4',
                    'a'+str(AVS_SERIAL_LEN),
                    'a'+str(USER_ID_LEN),
                    'u1']})

#       sony_multi_measdatatype Size 14656 Bytes 0X3940

def sony_multi_measdatatype(nPix=None):
    if nPix is None :
        return np.dtype({
            'names' :[
                    'prefix',
                    'timestamp',
                    'averages',
                    'deadpix',
                    'pixels'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u4',
                    'u2',
                    ('u4',MEAS_DEAD_PIX),
                    ('u4',MEAS_PIXELS)]})
    else :
        return np.dtype({
            'names' :[
                    'prefix',
                    'timestamp',
                    'averages',
                    'deadpix',
                    'pixels'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u4',
                    'u2',
                    ('u4',MEAS_DEAD_PIX),
                    ('u4',nPix)]})

#       sony_single_measdatatype Size 7332 Bytes 0x1CA4
def sony_single_measdatatype(nPix = None):
    if nPix is None:
        return np.dtype({
            'names' :[
                    'prefix',
                    'timestamp',
                    'deadpix',
                    'pixels'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u4' ,
                    ('u2',MEAS_DEAD_PIX),
                    ('u2',MEAS_PIXELS)]})
    else :
        return np.dtype({
            'names' :[
                    'prefix',
                    'timestamp',
                    'deadpix',
                    'pixels'],
            'formats':[
                    'a'+str(SIZE_PREFIX),
                    'u4' ,
                    ('u2',MEAS_DEAD_PIX),
                    ('u2',nPix)]}) 
                    
                    
                    

""" Command instruction """
"""     Getters         """
    

GET_DEVICE_CONFIGURATION    = [0x20,0x00,0x02,0x00,0x01,0x00]
GET_STORED_MEAS             = [0x20,0x00,0x02,0x00,0x07,0x00]
GET_AVG_STORED_MEAS         = [0x20,0x00,0x02,0x00,0x08,0x00]

def GET_DIGITAL_IN(InputId) :
    return                    [0x20,0x00,0x03,0x00,0x0A,0x00,InputId]
    
def GET_ANALOG_IN(AnputId) :
    return                    [0x20,0x00,0x03,0x00,0x0C,0x00,AnputId]
    
GET_VERSION_INFO            = [0x20,0x00,0x02,0x00,0x0E,0x00]
GET_RESET_REASON            = [0x20,0x00,0x02,0x00,0x12,0x00]
GET_IDENT                   = [0x20,0x00,0x02,0x00,0x13,0x00]

GET_FILE                    = [0x20,0x00,0x10,0x00,0x14,0x00] # 0x10 a verifier
GET_FILE_LEN                = [0x20,0x00,0x10,0x00,0x15,0x00] # 0x10 a verifier
GET_FIRST_FILE              = [0x20,0x00,0x02,0x00,0x16,0x00]
GET_NEXT_FILE               = [0x20,0x00,0x10,0x00,0x17,0x00] # 0x10 a verifier

"""     Setters         """
SET_DEVICE_CONFIGURATION    = [0x20,0x00,0xFE,0xF7,0x02,0x00] # SIZE 0xF7FE
SET_SD_CARD                 = [0x20,0x00,0x0E,0x00,0x09,0x00]

SET_DIGITAL_OUT             = [0x20,0x00,0x04,0x00,0x0B,0x00]
SET_ANALOG_OUT              = [0x20,0x00,0x05,0x00,0x0D,0x00]

SET_PWM                     = [0x20,0x00,0x08,0x00,0x10,0x00]
SET_SYNC_MASTER             = [0x20,0x00,0x03,0x00,0x19,0x00] # 0x03 a verifier
SET_TRIGGER_MODE            = [0x20,0x00,0x05,0x00,0x1A,0x00] 

def SET_PRE_SCAN(ON_OFF):
    return                    [0x20,0x00,0x03,0x00,0x1C,0x00,ON_OFF]

"""     Others          """
PREPARE_MEASUREMENT         = [0x20,0x00,0x2B,0x00,0x05,0x00]

def START_MEASUREMENT(l_NrOfScans) :
    return [0x20,0x00,0x04,0x00,0x06,0x00,l_NrOfScans & 0xFF, l_NrOfScans >> 8]
ACKNOWLEDGE                 = [0x21,0x00,0x02,0x00,0xC0,0x00]
STOP_MEASUREMENT            = [0x20,0x00,0x02,0x00,0x0F,0x00]
#SPECIAL_MEASUREMENT         = [0x20,0x00,0x,0x00,0x11,0x00]
DELETE_FILE                 = [0x20,0x00,0x10,0x00,0x18,0x00]
""" """
