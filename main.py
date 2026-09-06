print("                                     ALL MACHINES")

print("1. Straw reaper")
print("2. Paddy cleaner")
print("3. Rotter vator")
print("4. Harrow")
print("5. Potato seeder")
print("6. Tiller")
print("7. Small tiller")

machine = input("Enter machine name or number: ")

if machine == "Straw reaper" or machine == "1":
    result = "price = ₹3.2–4.0 lakh"
    print(result)
elif machine == "Paddy cleaner" or machine == "2":
    result = "price = ₹45,000–₹2 lakh+"
    print(result)
elif machine == "Rotter vator" or machine == "3":
    result = "price = ₹50,000–₹3 lakh"
    print(result)
elif machine == "Harrow" or machine == "4":
    result = "price = ₹45,000–₹3.5 lakh"
    print(result)
elif machine == "Potato seeder" or machine == "5":
    result = "price = ₹1.25–₹7.5 lakh"
    print(result)
elif machine == "Tiller" or machine == "6":
    result = "price = ₹1.6–₹3.1 lakh"
    print(result)
elif machine == "Small tiller" or machine == "7":
    result = "price = ₹10,000–₹80,000+" 
    print(result)