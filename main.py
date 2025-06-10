from extract.sql_extractor import extract_from_sqlite
from extract.api_extractor import extract_from_api
from transform.normalizer import normalize_sql_data, normalize_api_data, deduplicate_records
from load.mongo_loader import load_to_mongo

def run_etl():
    sql_data = extract_from_sqlite()
    api_data = extract_from_api()
    
    normalized_sql = normalize_sql_data(sql_data)
    normalized_api = normalize_api_data(api_data)

    combined_data = deduplicate_records(normalized_sql + normalized_api)

    load_to_mongo(combined_data)
    # combined_data = normalize_sql_data(sql_data) + normalize_api_data(api_data)
    # combined_data = deduplicate_records(combined_data)
    # load_to_mongo(combined_data)

if __name__ == "__main__":
    run_etl()
