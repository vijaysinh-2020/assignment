import unittest
import requests
import json

class APITesting(unittest.TestCase):
    
    def test_create_booking_api_happy_flow(self):
        data = {
            "firstname" : "Jim",
            "lastname" : "Brown",
            "totalprice" : 111,
            "depositpaid" : False,
            "bookingdates" : {
                "checkin" : "2023-01-01",
                "checkout" : "2023-01-01"
            },
            "additionalneeds" : "Breakfast"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        r = requests.post("https://restful-booker.herokuapp.com/booking", json= data, headers= headers)
        assert r.status_code == 200
        jsonResponse = r.json()
        
        assert isinstance(jsonResponse['bookingid'], int)
    

    def test_create_booking_api_negative_flow_missing_data(self):

        missingData = {
            "firstname" : "Jim",
            "totalprice" : 111,
            "depositpaid" : False,
            "bookingdates" : {
                "checkin" : "2023-01-01",
                "checkout" : "2023-01-01"
            },
            "additionalneeds" : "Breakfast"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        r = requests.post("https://restful-booker.herokuapp.com/booking", json= missingData, headers= headers)
        
        assert r.status_code == 500 

    def test_create_booking_api_negative_flow_invalid_data(self):

        invalidData = {
            "firstname" : "Jim",
            "lastname": "Abc",
            "totalprice" : "1 Million",
            "depositpaid" : False,
            "bookingdates" : {
                "checkin" : "2023-01-01",
                "checkout" : "2021-01-01"
            },
            "additionalneeds" : "Breakfast"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        r = requests.post("https://restful-booker.herokuapp.com/booking", json= invalidData, headers= headers)
        assert r.status_code == 500 

    


if __name__ == "__main__":
    unittest.main()

        