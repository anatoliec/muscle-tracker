from exrx_scraper.exrx_scraper import load_muscleData, save_muscleData, scrape_muscleData

AllMuscles = scrape_muscleData()
save_muscleData('muscledata.pkl', AllMuscles)
del AllMuscles
AllMuscles = load_muscleData('muscledata.pkl')
