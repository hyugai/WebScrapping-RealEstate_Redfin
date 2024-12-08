import sys
from pathlib import Path

src_path = Path.cwd()/'src'
sys.path.append(src_path.as_posix())
sys.path.append((src_path/'real_estate').as_posix())
from real_estate.city_href import scrape_city_href 
