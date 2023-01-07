import time

start_time = time.perf_counter()

# Execute the code here

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Time elapsed: {:.2f} seconds".format(elapsed_time))

#opencpvid test


def test_openCovid_window(self):
    openCovid()
    self.assertIsInstance(covidWindow, tk.Tk)
    self.assertEqual(covidWindow.geometry(), '500x500')

#total daily cases

def test_openCovid_totalDailyCases(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsNotNone(covidData)


#clean covid data

def test_openCovid_cleanCovidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(cleanCovidData, pd.DataFrame)
        self.assertEqual(list(cleanCovidData.columns), ['areaName', 'date', 'newCasesBySpecimenDate-0_4', 'newCasesBySpecimenDate-5_9', 'newCasesBySpecimenDate-10_14', 'newCasesBySpecimenDate-15_19', 'newCasesBySpecimenDate-20_24', 'newCasesBySpecimenDate-25_29', 'newCasesBySpecimenDate-30_34', 'newCasesBySpecimenDate-35_39', 'newCasesBySpecimenDate-40_44', 'newCasesBySpecimenDate-45_49', 'newCasesBySpecimenDate-50_54', 'newCasesBySpecimenDate-55_59', 'newCasesBySpecimenDate-60_64', 'newCasesBySpecimenDate-65_69', 'newCasesBySpecimenDate-70_74', 'newCasesBySpecimenDate-75_79', 'newCasesBySpecimenDate-80_84', 'newCasesBySpecimenDate-85_89', 'newCasesBySpec


#sum covid data

def test_openCovid_sumCovidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(sumCovidData, pd.Series)
        self.assertEqual(sumCovidData.name, 'Total number of cases daily')

#Test Covid data 

def test_openCovid_cleanCovidData_date(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(cleanCovidData['Month'], pd.Series)
        self.assertIsInstance(cleanCovidData['Week'], pd.Series)
        self.assertIsInstance(cleanCovidData['Day'], pd.Series)

#test first thirty days function 

def test_openCovid_hartlepoolFirst30Days(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(hartlepoolFirst30Days, pd.DataFrame)
        self.assertEqual(len(hartlepoolFirst30Days), 30)
        self.assertEqual(list(hartlepoolFirst30Days.columns), ['areaName', 'date', 'newCasesBySpecimen

#open_file function 

def test_changeInCasesOverTimeAndLocation_open_file(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()

#Test that the covidData DataFrame is created correctly:
def test_changeInCasesOverTimeAndLocation_covidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()
            self.assertIsInstance(covidData, pd.DataFrame)
            self.assertEqual(covidData.index.name, 'date')

#Test that the cleanCovidData DataFrame is created correctly:


def test_changeInCasesOverTimeAndLocation_cleanCovidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()
            self.assertIsInstance(cleanCovidData, pd.DataFrame)
           
#