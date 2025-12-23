def check_voting_eligibility():
    age = int(input("Enter your age: "))
    country = input("Enter your country: ").strip().lower()

    # Minimum voting age by country
    voting_age = {
        "india": 18,
        "usa": 18,
        "uk": 18,
        "canada": 18,
        "australia": 18
    }

    if country in voting_age:
        if age >= voting_age[country]:
            print("You are eligible to vote in", country.title())
        else:
            print("You are not eligible to vote in", country.title())
    else:
        print("Country not found in database. Check manually for eligibility.")

check_voting_eligibility()
