import os
import azure.functions as func
import pandas as pd
import adlfs
import json
import openpyxl
def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "POST":


        connection_string = os.getenv("connection_string")
        container = req.get_json()['container']
        blob_path = req.get_json()['blob_path']
        storage_account = req.get_json()['storage_account']
        path = f"az://{container}/{blob_path}"
        storage_options = {
            "connection_string":connection_string,
            'account_name': storage_account
        }
        df = pd.read_csv(path, storage_options=storage_options)
        # df = pd.read_excel(path,storage_options=storage_options,engine="openpyxl",sheet_name="FoodSales")
        print(df.head())
        res = {
            "message":f"Successfully validates file and uploaded to path: {blob_path}"
        }
        return func.HttpResponse(json.dumps(res))
    else:
        return (json.dumps({"message":"Failed to validate the file , Please fill the form again"}))
 