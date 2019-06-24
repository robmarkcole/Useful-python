"""
Run the notebook on a schedule and save in notebook_outputs folder (placed in .gitignore).
"""
import schedule
import time
import papermill as pm
import datetime

notebook_name = 'my_notebook'

def job():
    now_str = datetime.datetime.now().strftime("%H_%M_%S")
    print(f"Running notebook at {now_str}")
    pm.execute_notebook(
        f'{notebook_name}.ipynb',
        f"notebooks/{notebook_name}_{now_str}.ipynb"
    )


# schedule.every().hour.do(job)
schedule.every().minute.do(job)

# Everyt second check for job to run
while True:
    schedule.run_pending()
    time.sleep(1)