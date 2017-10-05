import subprocess
import sys,string,os
import serial
from timeit import default_timer
from time import sleep

tdebt="C:\Jenkins\TDEBT_CMD_TEST\tdebt_148.exe"

#TEST Set Macaddress
def TEST_tdebt_SetMacaddress():
    DrawBorder("Start TEST_tdebt_SetMacaddress ")
    cmdStr=tdebt+" -s macaddress 001122334455"
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    print("OUTPUT: "+r+"\r\n")
    if("MacAddress=001122334455[OK]"==r): 
     print("PASS\r\n")
     DrawBorder("End TEST_tdebt_SetMacaddress ")
     return 0	
    else:
     print("FAIL\r\n")
     DrawBorder("End TEST_tdebt_SetMacaddress ")
     return 1
	
#TEST Get Macaddress
def TEST_tdebt_GetMacaddress():
    DrawBorder("Start TEST_tdebt_GetMacaddress")   
    cmdStr=tdebt+" -g macaddress "
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    print("OUTPUT: "+r+"\r\n")
    if("001122334455"==r): 
     print("PASS\r\n")
     DrawBorder("End TEST_tdebt_GetMacaddress")   
     return 0	
    else:
     DrawBorder("End TEST_tdebt_GetMacaddress")   
     print("FAIL\r\n")
     return 1

#Set Macaddress
def tdebt_SetMacaddress(val):
    r=subprocess.check_output(tdebt+" -s macaddress "+val,stderr=subprocess.STDOUT)
    print("OUTPUT: "+r)
    if("MacAddress=001122334455[OK]"==r): 
     return 0	
    else:
     return 1
	
#Get Macaddress
def tdebt_GetMacaddress():
    r=subprocess.check_output(tdebt+" -g macaddress ",stderr=subprocess.STDOUT)
    if(""!=r):
     return 0	
    else:
     return 1	 
	
def DrawBorder(title):
    print("TEST------->"+str(title))
    return

#will set the pskey value to defualts
def tdebt_pskeySet(value):
    cmdStr=tdebt+" -s pskey 7 0 26146 34833 0 "+value
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    return

	
#tdebt_pskeyClear
def tdebt_pskeyClear(value):
    cmdStr=tdebt+" -s pskey 0 00000 00000 00000 00000 00000"
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    return

#tdebt_bt_uartdisable
def tdebt_bt_uartdisable(value):
    cmdStr=tdebt+" -s bt_uartdisable"
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    return
 
 #tdebt_SetAnaFtrim
def tdebt_SetAnaFtrim(value):
    cmdStr=tdebt+" -s pskey_ana_ftrim "+value
    #print(cmdStr)
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    return

#tdebt_RadioTxData
def tdebt_RadioTxData(value):
    cmdStr=tdebt+" -s radiotxdata"
    r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    return
	
	
#AnritsuMT8852B_MeasureFrequency
def AnritsuMT8852B_MeasureFrequency(comport,pbaudrate):
    pcomport=comport
    ser = serial.Serial(port=pcomport,\
        baudrate=pbaudrate,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)    
    ser.write("CWRESULT FREQOFF\r")
    sleep(0.5)
    line = ser.readline().replace("R", "")
    ser.close()
    return float(line)


#CWMEAS<ws><channel mode><,><channel><,><gate width> ,channel,gateWidth
def AnritsuMT8852B_Set_CW_MODE(comport,pbaudrate):
    pcomport=comport
    ser = serial.Serial(port=pcomport,\
        baudrate=pbaudrate,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)
    ser.write("OPMD CWMEAS\r")
    ser.write("CWMEAS FREQ,2441e6,3e-3\r")
    print("AnritsuMT8852B is in CW MODE")
    ser.close()
    return

#AnritsuMT8852B_MeasurePower
def AnritsuMT8852B_MeasurePower(comport,pbaudrate):
    pcomport=comport
    ser = serial.Serial(port=pcomport,\
        baudrate=pbaudrate,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)
    ser.write("CWRESULT POWER\r")
    sleep(0.5)
    line = ser.readline().replace("R", "")
    #print 'MeasurePower:%f' % (float(line))
    ser.close()
    return float(line)

#AnritsuMT8852B_Reset
def AnritsuMT8852B_Reset(comport,timeout,pbaudrate):
    pcomport=comport
    ser = serial.Serial(port=pcomport,\
        baudrate=pbaudrate,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)
    print("AnritsuMT8852B_Reset:" + ser.portstr)
    ser.write("*rst\r")
    ser.close()
    
    for i in range(timeout):
        sleep(1)
    print("rebooting timeout...",i)
    return

#RunTestSuite
def RunTestSuite():
    print("Starting Test Suite TEST_TDEBT")
    error=0
    error=error+TEST_tdebt_SetMacaddress()
    error=error+TEST_tdebt_GetMacaddress()
    if(error==0):
     print("ALL TEST PASSED "+str(error))
     return 0
    else:
     print("TESTS FAIL "+str(error))
    return 1

