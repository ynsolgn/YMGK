import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel("C:/Users/yunus/Desktop/normalize_gecensene.xlsx")
data2=pd.read_excel("C:/Users/yunus/Desktop/normalize_covid19.xlsx")


data["PM10"] = data["PM10 ( µg/m³ )"].astype("float")
data["SO2"] = data["SO2 ( µg/m³ )"].astype("float")
data["O3"] = data["O3 ( µg/m³ )"].astype("float")
data["NO2"] = data["NO2 ( µg/m³ )"].astype("float")
data["NOX"] = data["NOX ( µg/m³ )"].astype("float")

data2["PM10"] = data2["PM10 ( µg/m³ )"].astype("float")
data2["SO2"] = data2["SO2 ( µg/m³ )"].astype('float')
data2["O3"] = data2["O3 ( µg/m³ )"].astype("float")
data2["NO2"] = data2["NO2 ( µg/m³ )"].astype("float")
data2["NOX"] = data2["NOX ( µg/m³ )"].astype("float")

plt.figure(figsize=(40,20))
plt.subplot(2,3,1)   
plt.plot(data.Tarih,data.PM10,color="blue",linewidth=1,linestyle="-",marker="*",markersize=1,label="PM10-Korona Yok",alpha=0.9)
plt.plot(data2.Tarih,data2.PM10,color="red",linewidth=1,linestyle="-",marker="*", markersize=1,label="PM10-Korona Var",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("PM10 Oranı")
plt.title("Kocaeli PM10 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,3,2)   
plt.plot(data.Tarih,data.SO2,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="SO2-Korona Yok",alpha=0.9)
plt.plot(data2.Tarih,data2.SO2,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="SO2-Korona Var",alpha=0.9)

plt.xlabel("Tarih")
plt.ylabel("SO2 Oranı")
plt.title("Kocaeli SO2 Grafiği")
plt.grid()
plt.legend()

plt.subplot(2,3,3)   
plt.plot(data.Tarih,data.O3,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="O3-Korona Yok",alpha=0.9)
plt.plot(data2.Tarih,data2.O3,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="O3-Korona Var",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("O3 Oranı")
plt.title("Kocaeli O3 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,3,4)
plt.plot(data.Tarih,data.NO2,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="NO2-Korona Yok",alpha=0.9)
plt.plot(data2.Tarih,data2.NO2,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="NO2-Korona Var",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("NO2 Oranı")
plt.title("Kocaeli NO2 Grafiği")
plt.grid()
plt.legend()

plt.subplot(2,3,5)
plt.plot(data.Tarih,data.NOX,color="blue",linewidth=1,linestyle="-",marker="*",markersize=3,label="NOX-Korona Yok",alpha=0.9)
plt.plot(data2.Tarih,data2.NOX,color="red",linewidth=1,linestyle="-",marker="*",markersize=3,label="NOX-Korona Var",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("NOX Oranı")
plt.title("Kocaeli NOX Grafiği")
plt.grid()
plt.legend()



plt.show()