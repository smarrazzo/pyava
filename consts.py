
USER_ID_LEN             = 64;
NR_WAVELEN_POL_COEF     = 5;
NR_NONLIN_POL_COEF      = 8;
NR_DEFECTIVE_PIXELS     = 30;
MAX_NR_PIXELS           = 4096;
MEAS_DEAD_PIX           = 13;# 18
MEAS_PIXELS             = 3648;
SIZE_PREFIX             = 6;
NR_TEMP_POL_COEF        = 5;
MAX_TEMP_SENSORS        = 3;
ROOT_NAME_LEN           = 6;
AVS_SERIAL_LEN          = 9; # 10
MAX_PIXEL_VALUE         = 0xFFFC;
MAX_VIDEO_CHANNELS      = 2;
MAX_LASER_WIDTH         = 0xFFFF;
HW_TRIGGER_MODE		   = 1;
SW_TRIGGER_MODE	    	   = 0;
EDGE_TRIGGER_SOURCE     = 0;
LEVEL_TRIGGER_SOURCE	   = 1;
MAX_TRIGGER_MODE        = 1;
MAX_TRIGGER_SOURCE      = 1;
MAX_TRIGGER_SOURCE_TYPE = 1;
MAX_INTEGRATION_TIME    = 600000;
SAT_DISABLE_DET         = 0;
SAT_ENABLE_DET          = 1;
SAT_PEAK_INVERSION      = 2;
NR_DAC_POL_COEF         = 2;
TIMEOUT                 = 1000000;
ADR_WRITE               = 0x02;
ADR_READ                = 0x86;
ID_VENDOR               = 0x1992;
ID_PRODUCT              = 0x0667;

ERR_CODE = [
            'CODE 0x00 : UNKNOW',
            'CODE 0x01 : INVALID PARAMETER',
            'CODE 0x02 : INVALID PASSWORD',
            'CODE 0x03 : INVALID COMMAND',
            'CODE 0x04 : INVALID SIZE',
            'CODE 0x05 : MEASUREMENT PENDING',
            'CODE 0x06 : INVALID PIXEL RANGE',
            'CODE 0x07 : INVALID INTEGRATION TIME',
            'CODE 0x08 : OPERATION NOT SUPPORTED',
            'CODE 0x09 : INVALID COMBINATION',
            'CODE 0x0A : NO BUFFER AVAIBLE',
            'CODE 0x0B : NO SPECTRA AVAIBLE',
            'CODE 0x0C : INVALID STATE',
            'CODE 0x0D : UNEXPECTED DMA INT',
            'CODE 0x0E : INVALID FPGA FILE'
]

SENSOR_TYPE = ['RESERVED',
          'Hams 8378-256',
          'Hams 8378-1024',
          'ILX554',
          'Hams 9201',
          'Toshiba TCD 1304',
          'TSL 1301',
          'TSL 1401',
          'Hams 8378-512',
          'Hams 9840']

