# coding=utf-8
import airsim

if __name__ == '__main__':
    # 连接到AirSim
    client = airsim.VehicleClient()
    client.confirmConnection()

    # 设置打开天气控制
    client.simEnableWeather(True)

    # 范围为0到1，1表示最强
    client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 1)
