import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import json
import requests


def openCovid():
    covidWindow = tk.Tk()
    covidWindow.geometry("500x500")

    def totalDailyCases():
        # read file
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file3 = open_file()
        covidData = pd.read_csv(file3, index_col=0, parse_dates=["date"])
        # slcice table
        cleanCovidData = covidData.loc[
            :, "areaName":"newCasesBySpecimenDate-unassigned"
        ]
        sumCovidData = cleanCovidData.sum(
            axis=1, numeric_only=True
        )  # sum all new cases for different age range
        cleanCovidData[
            "Total number of cases daily"
        ] = sumCovidData  # create new column
        cleanCovidData["Month"] = cleanCovidData["date"].dt.month  # get month
        cleanCovidData["Week"] = cleanCovidData["date"].dt.week  # get week
        cleanCovidData["Day"] = cleanCovidData["date"].dt.day  # get Day

        hartlepoolFirst30Days = cleanCovidData[0:30]  # select hartlepool result
        hartlepoolFirst30Days.plot(
            kind="bar",
            y="Total number of cases daily",
            x="Day",
            title="Hartlepool number of cases in first 30 days",
        )

        plt.show()

    def totalWeeklyCases():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file4 = open_file()
        covidData = pd.read_csv(file4, index_col=0, parse_dates=["date"])

        cleanCovidData = covidData.loc[
            :, "areaName":"newCasesBySpecimenDate-unassigned"
        ]
        sumCovidData = cleanCovidData.sum(axis=1, numeric_only=True)
        cleanCovidData["Total number of cases daily"] = sumCovidData
        cleanCovidData["Month"] = cleanCovidData["date"].dt.month
        cleanCovidData["Week"] = cleanCovidData["date"].dt.week
        cleanCovidData["Day"] = cleanCovidData["date"].dt.day
        cleanCovidData["Total number of cases daily"] = sumCovidData
        hartlepoolFirst30Weeks = cleanCovidData[0:210]
        hartlepoolFirst30Weeks.plot(
            kind="box",
            y="Total number of cases daily",
            x="Week",
            title="Hartlepool number of cases in first 30 weeks",
        )

        plt.show()

    def totalMonthlyCases():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file5 = open_file()
        covidData = pd.read_csv(file5, index_col=0, parse_dates=["date"])

        cleanCovidData = covidData.loc[
            :, "areaName":"newCasesBySpecimenDate-unassigned"
        ]
        sumCovidData = cleanCovidData.sum(axis=1, numeric_only=True)
        cleanCovidData["Total number of cases daily"] = sumCovidData
        cleanCovidData["Month"] = cleanCovidData["date"].dt.month
        cleanCovidData["Week"] = cleanCovidData["date"].dt.week
        cleanCovidData["Day"] = cleanCovidData["date"].dt.day
        cleanCovidData["Total number of cases daily"] = sumCovidData
        hartlepoolFirst5Months = cleanCovidData[0:210]
        hartlepoolFirst5Months.plot(
            kind="area",
            y="Total number of cases daily",
            x="Month",
            title="Hartlepool number of cases in first 30 weeks",
        )

        plt.show()

    def changeInCasesOverTimeAndLocation():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file2 = open_file()
        covidData = pd.read_csv(file2, index_col=0, parse_dates=["date"])

        cleanCovidData = covidData[
            [
                "areaName",
                "date",
                "newCasesBySpecimenDate-0_4",
                "newCasesBySpecimenDate-5_9",
                "newCasesBySpecimenDate-10_14",
                "newCasesBySpecimenDate-15_19",
                "newCasesBySpecimenDate-20_24",
                "newCasesBySpecimenDate-25_29",
                "newCasesBySpecimenDate-30_34",
                "newCasesBySpecimenDate-35_39",
                "newCasesBySpecimenDate-40_44",
                "newCasesBySpecimenDate-45_49",
                "newCasesBySpecimenDate-50_54",
                "newCasesBySpecimenDate-55_59",
                "newCasesBySpecimenDate-60_64",
                "newCasesBySpecimenDate-65_69",
                "newCasesBySpecimenDate-70_74",
                "newCasesBySpecimenDate-75_79",
                "newCasesBySpecimenDate-80_84",
                "newCasesBySpecimenDate-85_89",
                "newCasesBySpecimenDate-90+",
                "newCasesBySpecimenDate-unassigned",
            ]
        ].copy()
        sliceTable = cleanCovidData[0:1800]
        sumCovidData = sliceTable.sum(axis=1, numeric_only=True)
        sliceTable["Total number of cases"] = sumCovidData
        sliceTable["Daily_cases"] = sliceTable["date"].dt.day
        highestAreaDf = (
            sliceTable.groupby(["Daily_cases", "areaName"]).sum().unstack()
        )  # .sort_values('Total number of cases', ascending = False)
        highestAreaDf.plot(kind="bar", y="Total number of cases", figsize=(14, 7))
        plt.show()
        return

    def comapareAreas():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file2 = open_file()
        covidDataa = pd.read_csv(file2, index_col=0, parse_dates=["date"])
        covidDataa.drop_duplicates()
        valueNull = covidDataa.isnull().sum()

        rollingRateTable = covidDataa.drop(
            [
                "newCasesBySpecimenDate-0_4",
                "newCasesBySpecimenDate-0_59",
                "newCasesBySpecimenDate-10_14",
                "newCasesBySpecimenDate-15_19",
                "newCasesBySpecimenDate-20_24",
                "newCasesBySpecimenDate-25_29",
                "newCasesBySpecimenDate-30_34",
                "newCasesBySpecimenDate-35_39",
                "newCasesBySpecimenDate-40_44",
                "newCasesBySpecimenDate-45_49",
                "newCasesBySpecimenDate-50_54",
                "newCasesBySpecimenDate-55_59",
                "newCasesBySpecimenDate-5_9",
                "newCasesBySpecimenDate-60+",
                "newCasesBySpecimenDate-60_64",
                "newCasesBySpecimenDate-65_69",
                "newCasesBySpecimenDate-70_74",
                "newCasesBySpecimenDate-75_79",
                "newCasesBySpecimenDate-80_84",
                "newCasesBySpecimenDate-85_89",
                "newCasesBySpecimenDate-90+",
                "newCasesBySpecimenDate-unassigned",
                "newCasesBySpecimenDateRollingSum-0_4",
                "newCasesBySpecimenDateRollingSum-0_59",
                "newCasesBySpecimenDateRollingSum-10_14",
                "newCasesBySpecimenDateRollingSum-15_19",
                "newCasesBySpecimenDateRollingSum-20_24",
                "newCasesBySpecimenDateRollingSum-25_29",
                "newCasesBySpecimenDateRollingSum-30_34",
                "newCasesBySpecimenDateRollingSum-35_39",
                "newCasesBySpecimenDateRollingSum-40_44",
                "newCasesBySpecimenDateRollingSum-45_49",
                "newCasesBySpecimenDateRollingSum-50_54",
                "newCasesBySpecimenDateRollingSum-55_59",
                "newCasesBySpecimenDateRollingSum-5_9",
                "newCasesBySpecimenDateRollingSum-60+",
                "newCasesBySpecimenDateRollingSum-60_64",
                "newCasesBySpecimenDateRollingSum-65_69",
                "newCasesBySpecimenDateRollingSum-70_74",
                "newCasesBySpecimenDateRollingSum-75_79",
                "newCasesBySpecimenDateRollingSum-80_84",
                "newCasesBySpecimenDateRollingSum-85_89",
                "newCasesBySpecimenDateRollingSum-90+",
                "newCasesBySpecimenDateRollingSum-unassigned",
            ],
            axis=1,
            inplace=False,
        )
        rollingRateTable["Week"] = rollingRateTable["date"].dt.month
        hattlepoolTable = rollingRateTable[0:231]
        middlesBroughTable = rollingRateTable[232:462]
        redcarAndClevelandTable = rollingRateTable[463:699]
        stockton_on_teesTable = rollingRateTable[701:900]
        total_rate = hattlepoolTable.sum(axis=1, numeric_only=True)
        hattlepoolTable["TotalRollingRate"] = total_rate
        totalRateMiddlesbrough = middlesBroughTable.sum(axis=1, numeric_only=True)
        middlesBroughTable["TotalRollingRate"] = totalRateMiddlesbrough
        totalRedcarAndClevelandTable = redcarAndClevelandTable.sum(
            axis=1, numeric_only=True
        )
        redcarAndClevelandTable["TotalRollingRate"] = totalRedcarAndClevelandTable
        fig, (ax0, ax1, ax2) = plt.subplots(
            nrows=1, ncols=3, sharey=True, figsize=(10, 66)
        )
        hattlepoolTable.plot(kind="barh", y="TotalRollingRate", x="Week", ax=ax0)
        middlesBroughTable.plot(kind="barh", y="TotalRollingRate", x="Week", ax=ax1)
        redcarAndClevelandTable.plot(
            kind="barh", y="TotalRollingRate", x="Week", ax=ax2
        )
        ax0.set(title="Hattlepool Daily Cases", xlabel="rolling rate", ylabel="time")
        ax1.set(title="Middlesbrough Daily Cases", xlabel="rolling rate", ylabel="time")
        ax2.set(
            title="Redcar and Cleveland Daily Cases",
            xlabel="rolling rate",
            ylabel="time",
        )
        plt.show()

    def areasWithHighestRollingRates():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file6 = open_file()
        covidData = pd.read_csv(file6, index_col=0, parse_dates=["date"])

        cleanCovidData = covidData[
            [
                "areaName",
                "date",
                "newCasesBySpecimenDateRollingRate-10_14",
                "newCasesBySpecimenDateRollingRate-15_19",
                "newCasesBySpecimenDateRollingRate-20_24",
                "newCasesBySpecimenDateRollingRate-25_29",
                "newCasesBySpecimenDateRollingRate-30_34",
                "newCasesBySpecimenDateRollingRate-35_39",
                "newCasesBySpecimenDateRollingRate-40_44",
                "newCasesBySpecimenDateRollingRate-45_49",
                "newCasesBySpecimenDateRollingRate-50_54",
                "newCasesBySpecimenDateRollingRate-55_59",
                "newCasesBySpecimenDateRollingRate-60_64",
                "newCasesBySpecimenDateRollingRate-65_69",
                "newCasesBySpecimenDateRollingRate-70_74",
                "newCasesBySpecimenDateRollingRate-75_79",
                "newCasesBySpecimenDateRollingRate-80_84",
                "newCasesBySpecimenDateRollingRate-85_89",
                "newCasesBySpecimenDateRollingRate-90+",
            ]
        ]
        tableSection = cleanCovidData[100:1800]
        sumCovidData = tableSection.sum(axis=1, numeric_only=True)
        tableSection["Total number of cases"] = sumCovidData
        tableSection["Week_case"] = tableSection["date"].dt.isocalendar().week
        highestAreaDf = tableSection.groupby(["Week_case", "areaName"]).sum().unstack()
        highestAreaDf.plot(kind="bar", y="Total number of cases", figsize=(14, 7))
        plt.show()

    def compareAreasCumulativeSum():
        def open_file():

            file = filedialog.askopenfile(filetypes=[("Python Files", "*.csv")])
            return file

        file7 = open_file()
        covidData = pd.read_csv(file7, index_col=0, parse_dates=["date"])

        covidData.drop_duplicates()
        valueNull = covidData.isnull().sum()
        cumulativeSumTable = covidData.drop(
            [
                "newCasesBySpecimenDate-0_4",
                "newCasesBySpecimenDate-0_59",
                "newCasesBySpecimenDate-10_14",
                "newCasesBySpecimenDate-15_19",
                "newCasesBySpecimenDate-20_24",
                "newCasesBySpecimenDate-25_29",
                "newCasesBySpecimenDate-30_34",
                "newCasesBySpecimenDate-35_39",
                "newCasesBySpecimenDate-40_44",
                "newCasesBySpecimenDate-45_49",
                "newCasesBySpecimenDate-50_54",
                "newCasesBySpecimenDate-55_59",
                "newCasesBySpecimenDate-5_9",
                "newCasesBySpecimenDate-60+",
                "newCasesBySpecimenDate-60_64",
                "newCasesBySpecimenDate-65_69",
                "newCasesBySpecimenDate-70_74",
                "newCasesBySpecimenDate-75_79",
                "newCasesBySpecimenDate-80_84",
                "newCasesBySpecimenDate-85_89",
                "newCasesBySpecimenDate-90+",
                "newCasesBySpecimenDate-unassigned",
                "newCasesBySpecimenDateRollingRate-0_4",
                "newCasesBySpecimenDateRollingRate-0_59",
                "newCasesBySpecimenDateRollingRate-10_14",
                "newCasesBySpecimenDateRollingRate-15_19",
                "newCasesBySpecimenDateRollingRate-20_24",
                "newCasesBySpecimenDateRollingRate-25_29",
                "newCasesBySpecimenDateRollingRate-30_34",
                "newCasesBySpecimenDateRollingRate-35_39",
                "newCasesBySpecimenDateRollingRate-40_44",
                "newCasesBySpecimenDateRollingRate-45_49",
                "newCasesBySpecimenDateRollingRate-50_54",
                "newCasesBySpecimenDateRollingRate-55_59",
                "newCasesBySpecimenDateRollingRate-5_9",
                "newCasesBySpecimenDateRollingRate-60+",
                "newCasesBySpecimenDateRollingRate-60_64",
                "newCasesBySpecimenDateRollingRate-65_69",
                "newCasesBySpecimenDateRollingRate-70_74",
                "newCasesBySpecimenDateRollingRate-75_79",
                "newCasesBySpecimenDateRollingRate-80_84",
                "newCasesBySpecimenDateRollingRate-85_89",
                "newCasesBySpecimenDateRollingRate-90+",
            ],
            axis=1,
            inplace=False,
        )
        cumulativeSumTable["Week"] = cumulativeSumTable["date"].dt.isocalendar().week
        # get darlington cumulative sum
        darlingtonTable = cumulativeSumTable[940:1180]
        # get halton cumulative sum
        haltonTable = cumulativeSumTable[1181:1415]
        # get stockton on tees cumulative sum
        stocktonOnTeesTable = cumulativeSumTable[701:939]

        # get darlington rolling rate accross all ages
        darlingtonTotalRate = darlingtonTable.sum(axis=1, numeric_only=True)
        darlingtonTable["TotalRollingRate"] = darlingtonTotalRate
        # get halton rolling rate accross all ages
        totalRateHalton = haltonTable.sum(axis=1, numeric_only=True)
        haltonTable["TotalRollingRate"] = totalRateHalton
        # get stockton on tees rolling rate accross all ages
        totalStocktononTeesTable = stocktonOnTeesTable.sum(axis=1, numeric_only=True)
        stocktonOnTeesTable["TotalRollingRate"] = totalStocktononTeesTable
        # create 3 plots to display results
        fig, (ax0, ax1, ax2) = plt.subplots(
            nrows=1, ncols=3, sharey=True, figsize=(10, 66)
        )
        darlingtonTable.plot(kind="hist", y="TotalRollingRate", x="Week", ax=ax0)
        haltonTable.plot(kind="hist", y="TotalRollingRate", x="Week", ax=ax1)
        stocktonOnTeesTable.plot(kind="hist", y="TotalRollingRate", x="Week", ax=ax2)
        ax0.set(title="Darlington Daily Cases", xlabel="Cumulative sum", ylabel="time")
        ax1.set(title="Halton Daily Cases", xlabel="Cumulative sum", ylabel="time")
        ax2.set(
            title="Stockton on Tees Daily Cases", xlabel="Cumulative sum", ylabel="time"
        )
        plt.show()

    # create buttons
    ttk.Button(
        covidWindow,
        text="Change in cases over date and location",
        command=changeInCasesOverTimeAndLocation,
    ).place(x=230, y=100)
    ttk.Button(covidWindow, text="Compare areas", command=comapareAreas).place(
        relx=0, rely=0.13
    )
    ttk.Button(covidWindow, text="Daily cases", command=totalDailyCases).place(
        relx=0, rely=0.26
    )
    ttk.Button(covidWindow, text="Weekly cases", command=totalWeeklyCases).place(
        relx=0, rely=0.39
    )
    ttk.Button(covidWindow, text="Monthly cases", command=totalMonthlyCases).place(
        relx=0, rely=0.52
    )
    ttk.Button(
        covidWindow,
        text="Rolling rate over time and area",
        command=areasWithHighestRollingRates,
    ).place(relx=0, rely=0.67)
    ttk.Button(
        covidWindow, text="Compare cumulative sum", command=compareAreasCumulativeSum
    ).place(relx=0.5, rely=0.67)

    covidWindow.mainloop()


def openStopnSearch():
    snsWindow = tk.Tk()
    snsWindow.geometry("500x500")

    def showClevelandNorthumbriaOutcome():
        northumbriaUrl = (
            "https://data.police.uk/api/stops-force?force=northumbria&date=2021-06"
        )
        clevelandUrl = (
            "https://data.police.uk/api/stops-force?force=cleveland&date=2021-06"
        )
        with urllib.request.urlopen(clevelandUrl) as resp1:
            clevelandData = resp1.read()
        with urllib.request.urlopen(northumbriaUrl) as resp2:
            northumbriaData = resp2.read()
        # Read and load data in panada dataframe
        jsonFormatCleveland = json.loads(clevelandData)
        clevelandDataset = pd.json_normalize(jsonFormatCleveland)
        jsonFormatNorthumbria = json.loads(northumbriaData)
        northumbriaDataset = pd.json_normalize(jsonFormatNorthumbria)
        # create datetime column
        clevelandDataset["datetime"] = pd.to_datetime(
            clevelandDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        northumbriaDataset["datetime"] = pd.to_datetime(
            northumbriaDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        # create month column
        clevelandDataset["months"] = clevelandDataset["datetime"].dt.month
        northumbriaDataset["months"] = northumbriaDataset["datetime"].dt.month
        # group by outcome and age range
        northumbriaAgeRange = (
            northumbriaDataset.groupby(["outcome", "age_range"]).sum().unstack()
        )
        clevelandAgeRange = (
            clevelandDataset.groupby(["outcome", "age_range"]).sum().unstack()
        )
        fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharex=True, figsize=(10, 10))
        clevelandAgeRange.plot(kind="bar", y="months", ax=ax0)
        northumbriaAgeRange.plot(kind="bar", y="months", ax=ax1)
        ax0.set(title="Cleveland result", xlabel="outcome", ylabel="time")
        ax1.set(title="Northumbria result", xlabel="outcome", ylabel="time")
        plt.show()

    def getUrl(areaString, dateObj):
        return "https://data.police.uk/api/stops-force?force={}&date={}".format(
            areaString, dateObj
        )

    def showBreakdownForSummer():
        # save urls
        northumbriaUrl_06_2021 = getUrl("northumbria", "2021-06")
        northumbriaUrl_07_2021 = getUrl("northumbria", "2021-07")
        northumbriaUrl_08_2021 = getUrl("northumbria", "2021-08")
        clevelandUrl_06_2021 = getUrl("cleveland", "2021-06")
        clevelandUrl_07_2021 = getUrl("cleveland", "2021-07")
        clevelandUrl_08_2021 = getUrl("cleveland", "2021-08")
        # Api call to read data for northumbria
        with urllib.request.urlopen(northumbriaUrl_06_2021) as resp1:
            northumbriaJuneData = resp1.read()
        with urllib.request.urlopen(northumbriaUrl_07_2021) as resp2:
            northumbriaJulyData = resp2.read()
        with urllib.request.urlopen(northumbriaUrl_08_2021) as resp3:
            northumbriaAugustData = resp3.read()
        # Api call to read data for cleveland
        with urllib.request.urlopen(clevelandUrl_06_2021) as resp4:
            clevelandJuneData = resp4.read()
        with urllib.request.urlopen(clevelandUrl_07_2021) as resp5:
            clevelandJulyData = resp5.read()
        with urllib.request.urlopen(clevelandUrl_08_2021) as resp6:
            clevelandAugustData = resp6.read()
        # Read and load data in panada dataframe
        json_format_cleveland_june = json.loads(clevelandJuneData)
        clevelandJuneDataset = pd.json_normalize(json_format_cleveland_june)
        json_format_cleveland_july = json.loads(clevelandJulyData)
        clevelandJulyDataset = pd.json_normalize(json_format_cleveland_july)
        json_format_cleveland_august = json.loads(clevelandAugustData)
        clevelandAugustDataset = pd.json_normalize(json_format_cleveland_august)
        # print(clevelandJuneDataset)

        # Read and load data in panada dataframe
        json_format_northumbria_june = json.loads(northumbriaJuneData)
        northumbriaJuneDataset = pd.json_normalize(json_format_northumbria_june)
        json_format_northumbria_july = json.loads(northumbriaJulyData)
        northumbriaJulyDataset = pd.json_normalize(json_format_northumbria_july)
        json_format_northumbria_august = json.loads(northumbriaAugustData)
        northumbriaAugustDataset = pd.json_normalize(json_format_northumbria_august)
        northumbriaJuneDataset["datetime"] = northumbriaJuneDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])
        northumbriaJulyDataset["datetime"] = northumbriaJulyDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])
        northumbriaAugustDataset["datetime"] = northumbriaAugustDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])

        clevelandJuneDataset["datetime"] = clevelandJuneDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])
        clevelandJulyDataset["datetime"] = clevelandJulyDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])
        clevelandAugustDataset["datetime"] = clevelandAugustDataset.filter(
            ["datetime"]
        ).applymap(lambda x: x[: x.find("T")])
        clevelandJuneDataset["datetime"] = pd.to_datetime(
            clevelandJuneDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        clevelandJulyDataset["datetime"] = pd.to_datetime(
            clevelandJulyDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        clevelandAugustDataset["datetime"] = pd.to_datetime(
            clevelandAugustDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        northumbriaJuneDataset["datetime"] = pd.to_datetime(
            northumbriaJuneDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        northumbriaJulyDataset["datetime"] = pd.to_datetime(
            northumbriaJulyDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        northumbriaAugustDataset["datetime"] = pd.to_datetime(
            northumbriaAugustDataset["datetime"], format="%Y/%m/%d"
        ).sort_values(ascending=True)
        # add week column
        clevelandJuneDataset["week"] = clevelandJuneDataset["datetime"].dt.week
        clevelandJulyDataset["week"] = clevelandJulyDataset["datetime"].dt.week
        clevelandAugustDataset["week"] = clevelandAugustDataset["datetime"].dt.week
        northumbriaJuneDataset["week"] = northumbriaJuneDataset["datetime"].dt.week
        northumbriaJulyDataset["week"] = northumbriaJulyDataset["datetime"].dt.week
        northumbriaAugustDataset["week"] = northumbriaAugustDataset["datetime"].dt.week
        clevelandSummerData = [
            clevelandJuneDataset,
            clevelandJulyDataset,
            clevelandAugustDataset,
        ]
        clevelandData = pd.concat(clevelandSummerData)
        # group table
        clevelandPoliceData = (
            clevelandData.groupby(["week", "self_defined_ethnicity"]).count().unstack()
        )
        clevelandPoliceData.plot(kind="area", y="involved_person", figsize=(80, 80))
        plt.show()

    def showArrestBreakdownAcrossYears():
        # save urls
        northumbriaUrl_04_2021 = getUrl("northumbria", "2021-03")
        northumbriaUrl_04_2020 = getUrl("northumbria", "2020-04")
        # northumbriaUrl_08_2021 = getUrl("northumbria", "2021-08")
        # clevelandUrl_06_2021   = getUrl("cleveland", "2021-06")
        # clevelandUrl_07_2021   = getUrl("cleveland", "2021-07")
        # clevelandUrl_08_2021   = getUrl("cleveland", "2021-08")
        # Api call to read data for northumbria
        with urllib.request.urlopen(northumbriaUrl_04_2021) as resp1:
            northumbria2021Data = resp1.read()
        with urllib.request.urlopen(northumbriaUrl_04_2020) as resp2:
            northumbria2020Data = resp2.read()
            # Api call to read data for cleveland

            # Read and load data in panada dataframe
            jsonFormatNorthumbria2021Data = json.loads(northumbria2021Data)
            northumbria2021Dataset = pd.json_normalize(jsonFormatNorthumbria2021Data)
            jsonFormatNorthumbria2020Data = json.loads(northumbria2020Data)
            northumbria2020Dataset = pd.json_normalize(jsonFormatNorthumbria2020Data)
            # print(clevelandJuneDataset)

            # Read and load data in panada dataframe
            northumbria2021Dataset["datetime"] = northumbria2021Dataset.filter(
                ["datetime"]
            ).applymap(lambda x: x[: x.find("T")])
            northumbria2020Dataset["datetime"] = northumbria2020Dataset.filter(
                ["datetime"]
            ).applymap(lambda x: x[: x.find("T")])
            northumbria2021Dataset["datetime"] = pd.to_datetime(
                northumbria2021Dataset["datetime"], format="%Y/%m/%d"
            ).sort_values(ascending=True)
            northumbria2020Dataset["datetime"] = pd.to_datetime(
                northumbria2020Dataset["datetime"], format="%Y/%m/%d"
            ).sort_values(ascending=True)
            # add week column
            northumbria2021Dataset["week"] = northumbria2021Dataset["datetime"].dt.day
            northumbria2020Dataset["week"] = northumbria2020Dataset["datetime"].dt.day
            # group table
            northumbriaData0 = (
                northumbria2021Dataset.groupby(["outcome", "self_defined_ethnicity"])
                .mean()
                .unstack()
            )
            northumbriaData1 = (
                northumbria2020Dataset.groupby(["outcome", "self_defined_ethnicity"])
                .mean()
                .unstack()
            )
            fig, (ax0, ax1) = plt.subplots(
                nrows=2, ncols=1, sharey=True, figsize=(30, 10)
            )
            northumbriaData0.plot(kind="hist", y="week", ax=ax0)
            northumbriaData1.plot(kind="hist", y="week", ax=ax1)

            ax0.set(title="2021 record", xlabel="", ylabel="time")
            ax1.set(title="2020 record", xlabel="", ylabel="time")
            plt.show()

    def showBreakdownAcrossYears():
        # save urls
        northumbriaUrl_04_2021 = getUrl("northumbria", "2021-03")
        northumbriaUrl_04_2020 = getUrl("northumbria", "2020-04")
        # Api call to read data for northumbria
        with urllib.request.urlopen(northumbriaUrl_04_2021) as resp1:
            northumbria2021Data = resp1.read()
        with urllib.request.urlopen(northumbriaUrl_04_2020) as resp2:
            northumbria2020Data = resp2.read()
            # Api call to read data for cleveland

            # Read and load data in panada dataframe
            jsonFormatNorthumbria2021Data = json.loads(northumbria2021Data)
            northumbria2021Dataset = pd.json_normalize(jsonFormatNorthumbria2021Data)
            jsonFormatNorthumbria2020Data = json.loads(northumbria2020Data)
            northumbria2020Dataset = pd.json_normalize(jsonFormatNorthumbria2020Data)
            # print(clevelandJuneDataset)

            # Read and load data in panada dataframe
            northumbria2021Dataset["datetime"] = northumbria2021Dataset.filter(
                ["datetime"]
            ).applymap(lambda x: x[: x.find("T")])
            northumbria2020Dataset["datetime"] = northumbria2020Dataset.filter(
                ["datetime"]
            ).applymap(lambda x: x[: x.find("T")])
            northumbria2021Dataset["datetime"] = pd.to_datetime(
                northumbria2021Dataset["datetime"], format="%Y/%m/%d"
            ).sort_values(ascending=True)
            northumbria2020Dataset["datetime"] = pd.to_datetime(
                northumbria2020Dataset["datetime"], format="%Y/%m/%d"
            ).sort_values(ascending=True)
            # add week column
            northumbria2021Dataset["day"] = northumbria2021Dataset["datetime"].dt.day
            northumbria2020Dataset["day"] = northumbria2020Dataset["datetime"].dt.day
            # group table
            northumbriaData0 = (
                northumbria2021Dataset.groupby(["age_range", "gender"]).std().unstack()
            )
            northumbriaData1 = (
                northumbria2020Dataset.groupby(["age_range", "gender"]).std().unstack()
            )
            fig, (ax0, ax1) = plt.subplots(
                nrows=2, ncols=1, sharey=True, figsize=(10, 10)
            )
            northumbriaData0.plot(kind="barh", y="day", ax=ax0)
            northumbriaData1.plot(kind="barh", y="day", ax=ax1)

            ax0.set(title="2021 record", xlabel="Time ", ylabel="Age range ")
            ax1.set(title="2020 record", xlabel="Time ", ylabel="Age range ")
            plt.show()

    ttk.Button(
        snsWindow,
        text="cleveland and northumbria arrests record",
        command=showClevelandNorthumbriaOutcome,
    ).place(relx=0, rely=0.13)
    ttk.Button(
        snsWindow,
        text="breakdown of cleveland force based on ethnicity",
        command=showBreakdownForSummer,
    ).place(relx=0, rely=0.4)
    ttk.Button(
        snsWindow,
        text="compare arrest between 2020 and 2021",
        command=showArrestBreakdownAcrossYears,
    ).place(relx=0, rely=0.65)
    ttk.Button(
        snsWindow,
        text="compare stops by age and gender between 2020 and 2021",
        command=showBreakdownAcrossYears,
    ).place(relx=0, rely=0.85)

    snsWindow.mainloop()


root = tk.Tk()
root.geometry("500x500")
covidButton = tk.Button(root, text="Open covid window", command=openCovid)
stopNsearchBtn = tk.Button(
    root, text="view police stop and search", command=openStopnSearch
)
covidButton.pack()
stopNsearchBtn.pack()
root.mainloop()
