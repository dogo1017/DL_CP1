#DL 1st, crew shares project

# story
print("The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.")

# inputs from user
members_of_crew = int(input("How many crew members were there (not including first mate and captain): ").strip().replace(",", ""))
amount_earned = float(input("How much was earned total: ").strip().replace(",", ""))

# number of shares each group gets
captain_share = 7 
first_mate_share = 3 
crew_shares = 1

deduction = 500 # amount of money the captain already paid
shares = amount_earned / (members_of_crew + captain_share + first_mate_share) # amount of money in each share

# total amounts earned
captain_earned = captain_share * shares
first_mate_earned = first_mate_share * shares
crew_earned = (crew_shares * shares) -deduction

# rounding
amount_earned = round(amount_earned, 2)
captain_earned = round(captain_earned, 2)
first_mate_earned = round(first_mate_earned, 2)
crew_earned = round(crew_earned, 2)

# outputs
print(f"How much was earned: {amount_earned:.2f}\n")
print(f"How many crew members are there (not including the captain and first mate): {members_of_crew}\n")
print(f"The captain gets: ${captain_earned:.2f}\n")
print(f"The first mate gets: ${first_mate_earned:.2f}\n")
print(f"Crew still needs: ${crew_earned:.2f}\n")