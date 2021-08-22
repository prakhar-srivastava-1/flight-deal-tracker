from data_manager import DataManager

# get all data from sheet
dm = DataManager()
dm.initialise_service()
dm.read_records()
dm.write_codes(entries=[["TESTING", "TESTING", "TESTING", "TESTING",
                        "TESTING", "TESTING", "TESTING", "TESTING", "TESTING"]])
