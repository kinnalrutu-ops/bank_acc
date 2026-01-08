import sys

def get_details_info(acc_no, holder_name,type,balance):
  
    return (
        f"acc_no:{acc_no},"
        f"holder_name:{holder_name},"
        f"type:{type},"
        f"balance:{balance}"
    )
if __name__ == "__main__":
    print(get_details_info("012345678","abc","savings",55000))
