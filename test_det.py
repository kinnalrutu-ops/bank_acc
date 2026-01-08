import pytest
from bank_acc import get_details_info

def test_details():
   
    acc_no = "012345678"
    holder_name = "abc"
     type = "savings"
    balance = 55000
    
    expected_output = (
        "Account No:012345678,"
        "holder_name:abc,"
        "type:savings,"
        "balance:55000"
    )

    assert get_bank_info(acc_no, holder_name, type, balance) == expected_output
