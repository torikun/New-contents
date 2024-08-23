# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11
import schedule
import requests
import time
import datetime



def measure():
    token = 'HzWhPTI0SMDCfxWUaZfcg37ME3bbf48kmh8VpfKby6x'#LINE Notifyで発行されたトークン
    url = 'https://notify-api.line.me/api/notify'#LINE NotifyのAPIのURL
    
    dt = datetime.datetime.now()#現在時刻の取得
    d1=dt.strftime('\n%Y/%m/%d  %H:%M:%S')#始めに改行を入れて見やすくする
 
    while True:#温度と湿度が測定されるまでループ
        result = instance.read()
        if result.is_valid():
            temp="Temperature: %-3.1f   ℃" % result.temperature#温度
            humi="Humidity: %-3.1f %%" % result.humidity#湿度
            break

    d2= "\n" + temp + "\n"+ humi
    ms_data =d1 + d2#現在時刻と温度、湿度の文字列をくっつける
    post_data = {'message': ms_data}#送信するメッセージ
    headers = {'Authorization': 'Bearer ' + token}
    #送信
    res = requests.post(url,
                        data=post_data,
                        headers=headers)
    print(res.text)#メッセージが送信されたかどうかの確認
 
GPIO.setmode(GPIO.BCM)
schedule.every(1).hour.do(measure)#１時間ごとにmeasureを実行する命令
 
try:
    instance = dht11.DHT11(pin=14)
    measure()#実行したときの時刻と温度、湿度をLINEに通知
    while True:
        schedule.run_pending()#schedule.every(1).minutes.do(measure)を実行
        time.sleep(1)
 
except KeyboardInterrupt:
    print("GPIO-Cleanup")
    GPIO.cleanup()

def GetTemperature():
    filename = 'dht11.data'
    infile = open(filename, 'rb')
    temperature_int_part = infile.read(2)
    temperature_dec_part = infile.read(2)
    humidity_int_part = infile.read(2)
    humidity_dec_part = infile.read(2)
    
    infile.close()

    temp_int_value = int.from_bytes(temperature_int_part, byteorder='little')
    temp_dec_value = int.from_bytes(temperature_dec_part, byteorder='little')

    sensor_data = temp_int_value + (temp_dec_value / 10)

    return sensor_data

def GetHumidity():
    filename = 'dht11.data'
    infile = open(filename, 'rb')
    temperature_int_part = infile.read(2)
    temperature_dec_part = infile.read(2)
    humidity_int_part = infile.read(2)
    humidity_dec_part = infile.read(2)
    
    infile.close()

    int_value = int.from_bytes(humidity_int_part, byteorder='little')
    dec_value = int.from_bytes(humidity_dec_part, byteorder='little')

    sensor_data = int_value + (dec_value / 10)

    return sensor_data


if __name__ == '__main__':
    temperature = GetTemperature()
    humidity = GetHumidity()

    print(temperature, '[℃], ', humidity, '[%]')

    try:
        am = ambient.Ambient(43833, '8b45280ad91e312b')
        r = am.send({'d1': temperature, 'd2': humidity})
        print('sent to ambient : ret = %d' % r.status_code)
    except requests.exceptions.RequestException as e:
        print('request failed: ', e)