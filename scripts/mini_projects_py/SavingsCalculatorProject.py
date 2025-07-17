# --- Display a greeting ---
greeting = "Hello "
name = "Mauricio"
print(greeting + name)

# --- Calculate the yearly income ---


hourly_wage = 15
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
weeks_per_year = 48
income_per_year = weeks_per_year * income_per_week
print(name + "'s yearly income is:")
print(income_per_year)


# --- Calculate the yearly spend ---

spend_per_week = 250
spend_per_year = spend_per_week * 52
print(name + "'s yearly spend is:")
print(spend_per_year)


# --- Calculate the yearly savings ---
savings_per_year = income_per_year - spend_per_year
print(name + "'s yearly savings:")
print(savings_per_year)