import sys

def get_details_info(acc_no, holder_name,type,balance):
  
    return (
        f"acc_no:{ACC_NO},"
        f"holder_name:{HOLDER_NAME},"
        f"Department:{department},"
        f"Salary:{salary:.2f}"
    )
if __name__ == "__main__":
    print("=== Employee details ===")
    print(get_employee_info("John Doe","E101","IT",55000))
