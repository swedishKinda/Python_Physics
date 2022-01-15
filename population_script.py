city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_1950 = 983000
pop_2000 = 8831800
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927

percentage_gr = (pop_change/pop_1927) * 100

annual_gr = percentage_gr / (2017-1927)


def population_growth(year_one, year_two, population_one, population_two):
    growth_rate = (((population_two - population_one) /
                   population_one) * 100) / (year_two - year_one)
    return growth_rate


set_one = population_growth(1927, 2017, pop_1927, pop_2017)
set_two = population_growth(1950, 2000, pop_1950, pop_2000)

report = "The population in 1927 was " + str(pop_1927) + ". The population in 2017 was " + str(pop_2017) + ". The change in population between the two years was " + str(
    pop_change) + ". As a result the annual growth rate from 1927 to 2017 was " + str(set_one) + ". Furthermore, the annual growth rate from 1950 to 2000 was " + str(set_two) + "."

print(report)