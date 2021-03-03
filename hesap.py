import requests
import json

def getDollarValue(base="USD"):
    apiUrl = f"https://api.exchangeratesapi.io/latest?base={base}"
    response = requests.get(apiUrl)
    dictionary = json.loads(response.content)
    tryValue = dictionary["rates"]["TRY"]

    return float(tryValue)


def getEthereumValue():
    apiKey = "6c4a6306eec5fe0bc5a6f17b7bdfff1a"
    url = f"https://api.nomics.com/v1/currencies/ticker?key={apiKey}&ids=ETH"
    response = requests.get(url)
    dictionary = json.loads(response.content)
    ethereumPrice = float(dictionary[0]["price"])
    return ethereumPrice


def profit(mhs):
    dailyProfitMh =  0.0054 * 0.01 * mhs * getEthereumValue()
    monthlyProfitForRig = 6 *  dailyProfitMh * 30 * getDollarValue()
    return monthlyProfitForRig
    

def gpuForMining(mhs,watt):
    electricityPerKWh = 0.2309
    wattToKwh = watt * 0.001
    dailyEnergyForRig = (6 * wattToKwh ) * 24
    monthlyEnergyForRig = 30 * dailyEnergyForRig
    activeEnergyPrice = monthlyEnergyForRig * electricityPerKWh
    totalEnergyPrice = calculateTax(monthlyEnergyForRig,activeEnergyPrice)
    totalProfits = profit(mhs)
    netIncome = totalProfits - totalEnergyPrice
    print(f"Toplam Enerji Maliyeti 6'lı rig için {totalEnergyPrice}\nMaliyetler Hariç Toplam Kazanılan Para {totalProfits}\nNet Kazanç {netIncome}")


def calculateTax(kwatt, activeEnergyPrice):
    dagitimBedeli = kwatt * 0.1304
    enerjifonu = kwatt * 0.0023
    trtpayi = kwatt * 0.0046
    elTuketimVer = kwatt * 0.0115
    taxWithoutKdv = (activeEnergyPrice + enerjifonu + trtpayi + elTuketimVer + dagitimBedeli)
    kdv = taxWithoutKdv * 0.18
    totalTaxes = taxWithoutKdv + kdv
    return totalTaxes


