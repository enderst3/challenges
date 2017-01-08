'''
In a small town the population is 1000 at the beginning of a year.

the population regularly increases by 2 percent per yearn and moreover 50 new inhabitants
come to live in the town.

How many years does the town need to see its population great or equal to 1200 inhabitants?

solve(start_pop, additional, delta, target)
in: solve(1000, 50, 2, 1200) => out: 3 years
'''

def small_town():

    start_pop = 1000
    pop_increase = .02
    new_comer = 50
    target_pop = 1200
    current_pop = ((start_pop*pop_increase)+new_comer)+start_pop
    yearly_increase = (current_pop*pop_increase)+new_comer
    count = 1

    while current_pop < target_pop:
        current_pop = current_pop+yearly_increase
        count += 1

    print(count)

small_town()
