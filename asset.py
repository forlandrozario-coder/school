initial_price = 12000000
salvage_value = 2000000
economic_life_years = 4 
years_to_calculate_value_after = 2
annual_depreciation = (initial_price - salvage_value) / economic_life_years
laptop_value_after_2_years = initial_price - (annual_depreciation * years_to_calculate_value_after)
print(f"the annual depreciation of the laptop is (RP) {annual_depreciation:,.2f}")
print(f"the value of the laptop after {years_to_calculate_value_after} years is (RP) {laptop_value_after_2_years:,.2f}")