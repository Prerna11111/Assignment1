#How can you format a string with placeholder for a variable value.

#there is multiple way to formate string like using "%" operator , .format method, using f-string

#using % operator
name = "Prerna"
phone_number = 8754725524
print("hey %s" '\n'"How are you ?"  "\n""your number is %s" %(phone_number,name))

#using format() method
name1 = "Preeti"
phone_number1 =9936985422
print("hey {1}" 
      '\n'"How are you ?"  
      "\n""your number is {0}" .format(phone_number1,name1))