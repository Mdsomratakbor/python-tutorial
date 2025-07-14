def run():
     print("\n-- Logical Conditions --")
     age = 20
     has_id = True

     if age>=18 and has_id:
          print("Allowed to enter")
     else:
          print("Not allowed")

     is_student = True
     is_staff = True

     if is_student or is_staff:
        print("Eligible for discount")

     if not is_student:
        print("Not a student")
