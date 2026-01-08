from bank_acc import get_details
import pytest
def test_get_details():
    Accno,Holder_name,Type,bal=get_details(12345,"John Doe","Savings",1000.50)
    Accno="012384793"
    holder_name="Jane Smith" 
    type="savings"
    balance=2500.75
    assert(get_details(Accno,holder_name,type,balance)==({'012384793'},{'Jane Smith'},{'savings'},{2500.75}))