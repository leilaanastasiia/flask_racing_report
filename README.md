# Flask REST API racing report
___

Training parsing data project based on Formula 1 results from Monaco in 2018. 

Stack: `Flask`, `flask_restful`, `SQLite`, `Swagger`, `pytest`, `coverage`, `argparse`

Features:
- parsing data from a logfiles
- populating a database with the data
- `report/?order=asc&format=json` views a full report data with ordering (json / xml)
- `report/drivers/?order=asc&format=json` views all info about the drivers (json / xml)
- `report/drivers/BBS` shows all data about the driver selected by his abbreviation

All resources are described with Swagger. Covered with pytest.