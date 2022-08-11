from fastapi import FastAPI
from sqlalchemy import create_engine
from decouple import config
import sys
sys.path.insert(0, '/home/lelet/selenium_linux/')
from extract import run_extraction
from datalake.utils import add_all_additional_info, add_all_homepage


app = FastAPI()
engine = create_engine(config('POSTGRES_URI'))


@app.get('/')
def home():
    return {'hello': 'world'}

@app.get('/scrapes')
async def scrapes():

    clean_table, clean_fund = run_extraction()
    add_all_homepage(clean_table, engine)
    add_all_additional_info(clean_fund, engine)
    return {"hello": "scrapes"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port=3000, reload=True, proxy_headers=True)