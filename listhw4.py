web_dev=["Raj","Som","Susheel"]
data_science=["Sudhakar","Rajshetty","Mathews"]
UI_design=["Rajesh","Babu","Ramu"]

all_participants=web_dev+data_science+UI_design

web_dev.append("Dev")
data_science.insert(1,"John")
UI_design.pop()

data_science_copy = data_science.copy()
data_science.clear()

name_lengths = [len(name) for name in data_science_copy]

is_asha_there=("Asha" in web_dev)or("Asha" in data_science_copy) or ("Asha" in UI_design)

first_participants = (
    web_dev[0],
    data_science_copy[0],
    UI_design[0]
)

print("Web development :",web_dev)
print("Data science :",data_science_copy)
print("UI design :",UI_design)
print("First 2 web developers :",web_dev[0:2])
print("Is Asha there in any list :",is_asha_there)
print("First participants :",first_participants)
