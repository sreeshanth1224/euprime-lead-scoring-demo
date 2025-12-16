# Lead Scoring Demo for EUprime


leads = [
    ["Asha", "Engineer", "Biotech", "USA", "Series A", "Yes"],
    ["Rahul", "Director", "Software", "India", "Seed", "No"],
    ["John", "Manager", "Biotech", "USA", "Series B", "Yes"],
    ["Maya", "Intern", "Biotech", "USA", "Series C", "No"]
]


results = []


for lead in leads:
    score = 0


    if lead[1] == "Director":
        score = score + 30


    if lead[2] == "Biotech":
        score = score + 20


    if lead[3] == "USA":
        score = score + 10


    if lead[4] == "Series B" or lead[4] == "Series C":
        score = score + 20


    if lead[5] == "Yes":
        score = score + 20


    results.append([lead[0], score])


for r in results:
    print("Name:", r[0], "| Score:", r[1])


# Create CSV file
file = open("lead_scores.csv", "w")
file.write("Name,Score\n")


for r in results:
    file.write(r[0] + "," + str(r[1]) + "\n")


file.close()


print("CSV file created successfully")