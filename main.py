from exrx_scraper.exrx_scraper import load_muscleData, MuscleGroup, Muscle

# NOTE: If muscle_data.pkl is outdated or does not exist, run exrx_scraper.py to scrape a new dataset.
muscle_groups = load_muscleData('exrx_scraper/muscle_data.pkl')


for i in range(0, 10):
    print(muscle_groups[i].name)
    for j in range(0, len(muscle_groups[i].muscles)):
        print("   ", muscle_groups[i].muscles[j].name)
