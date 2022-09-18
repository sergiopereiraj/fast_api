from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/fastapi")

meta_data = MetaData()