import requests
GET_SINGLE_STUD_URL = "http://127.0.0.1:8000/api/get-student/{}/"
GET_ALL_STUDS = "http://127.0.0.1:8000/api/get-all-students/"
CREATE_STUD = "http://127.0.0.1:8000/api/create-student/"
CRUD_OPERATION = "http://127.0.0.1:8000/api/all-operation/"
# CRUD_OPERATION = "http://127.0.0.1:8000/api/stud-class-api/"
# CRUD_OPERATION = "http://127.0.0.1:8000/api/func-stud-api/"







def get_single_stud(id):
    response = requests.get(GET_SINGLE_STUD_URL.format(id))
    python_dict = response.json()  # json to python dict
    # print(python_dict)

# get_single_stud(2)

def get_all_student():
    # response = requests.get(GET_ALL_STUDS)
    response = requests.request("GET", GET_ALL_STUDS)
    python_dict = response.json()  # json to python dict
    # print(python_dict)

# get_all_student()

def create_student(data):
    response = requests.post(CREATE_STUD, json=data)
    print(response.status_code)
    print(response.text)  # json data
    # print(response.content)  # bytes data

d = {"name": "Arun", "age": 24, "marks": 99, "adress": "Kashmir"}
# create_student(d)


data = {"id": 1}
# response = requests.get(CRUD_OPERATION, json=data)
# print(response.text) # json
# print(response.json()) # python dict

# response = requests.get(CRUD_OPERATION, json={})
# print(response.json()) # python dict

# def get_single_data_or_all_data(data={}):
#     if data.get("id"):
#         response = requests.get(CRUD_OPERATION, json=data)
#     else:
#         response = requests.get(CRUD_OPERATION, json={})
#     print(response.json()) # python dict
#
# get_single_data_or_all_data({})



def create_student(data):
    response = requests.post(CRUD_OPERATION, json=data)
    # print(response.status_code)
    # print(response.text)  # json data
    print(response.json())  # json data

    # print(response.content)  # bytes data


# create_student({"name": "ASHWINI", "age": 24, "marks": 99, "adress": "Pune"})

def update_student(data):
    response = requests.request("PUT", CRUD_OPERATION, json=data)
    print(response.json())  # json data


update_student({"id": 5, "name": "AKASH", "age": 28, "adress": "Mumbai", "marks": 56})
#



# def update_student(payload):
#     response = requests.request("PATCH", CRUD_OPERATION, json=payload)
#     print(response.json())  # json data


# update_student({"id": 8, "name": "ABKBKJVJV"})














