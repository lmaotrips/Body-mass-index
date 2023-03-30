# its a body mass index
weight = float(input("what is your weight on the earth kg: ?"))
height = float(input("what is your height on the earth m: ?"))
bmi = round(weight / height ** 2)
if bmi < 18:
  print(f"your bmi is {bmi}, you are under weight.")
elif bmi < 25:
  print(f"your bmi is {bmi}, you are a cuteee.")
elif bmi <30:
  print(f"your bmi  is {bmi}, you are overweight.")
elif bmi <35:
  print(f"your bmi is {bmi}, you are obese.")
else:
  print(f"your bmi is {bmi}, you are clinically obese,")