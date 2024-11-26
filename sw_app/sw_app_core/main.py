from interpreter import Interpreter
from equation_reader import EquationReader
from message_ingestor.ingestor_factory import IngestorFactory
from message_production.producer_factory import ProducerFactory
import time
import requests 

def main():

    url = "http://127.0.0.1:8000/interpreter/"
    data_file = "D:/Projects_Product/Session1_Django/sw_app/test_data.txt"

    """Fetching the data"""
    ingestor_factory = IngestorFactory(data_file)
    file_ingestor =  ingestor_factory.get_data_ingestor()
    data_list = file_ingestor.read_data(data_file)
    
    """Fetching the expressions from the kpi model"""
    try:
        kpi_url = url + "kpi/"  
        response = requests.get(kpi_url)
        response.raise_for_status()
        kpis = response.json() 
    except Exception as e:
        print(f"Error fetching KPIs: {e}")


    for data in data_list:
        asset_id = data["asset_id"]
        value = data["value"]
        
        for kpi in kpis:
            """Fetching the equation from the config file"""
            expression = kpi["expression"]
            reader = EquationReader()
            equation = reader.resolve_variables(expression, data["value"])
            """ Sending the equation to be calculated"""
            interpreter = Interpreter(equation)
            result = interpreter.interpret()

            """Send the result back to django"""
            try:
                kpi_asset_url = url + "kpiasset/"
                body = {
                    "asset_id": asset_id,
                    "kpi_id": kpi["id"],
                    "result": str(result)
                }
                res_response = requests.post(kpi_asset_url, json=body)
                res_response.raise_for_status()
                print(f"Successfully saved result for asset {asset_id}: {result}")
            except Exception as e:
                print(f"Error saving result: {e}")
            
            # """ Saving the new value in the database """
            # data["value"] = result
            # data_factory = ProducerFactory("sqlite")
            # data_reader = data_factory.get_data_producer()
            # data_reader.create_table()
            # data_reader.save(data)
            
            #time.sleep(5)


if __name__ == '__main__':
    main()
