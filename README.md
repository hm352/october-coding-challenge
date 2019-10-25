# october-coding-challenge
Build an API that retrieves a companies phone number when supplied a company name

# Setup

`$ pip install -r requirements.txt`

# Run server 

`$ python api.py`

# Submit Company Number Request 

`$ curl https://127.0.0.1:5000 -X POST -H application/contenJSON -d '{"company": "COMPANY NAME"}'`

# Run tests

Requires requirements.txt to have been installed

`$ pytest test_functional.py`

# Other Considerations outside of scope
