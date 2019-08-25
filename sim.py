import random
import sys
random.seed(100)

life_expectency = 77.45         # poland's off wiki.
firtility_rate = 1.36           # poland's off wiki.
initial_population = 38420687   # poland's off wiki.
male_female_ratio = 0.94        # poland's off wiki.
birth_age = 25                  # i made it up.
years = 1000                    # i made it up.

def magic_coin(bias):
        coin = random.random()
        while coin == bias:
            coin = random.random()
        if coin < bias:
            return True
        else:
            return False

def print_stats(
    prefix,
    females, febabies, fedeaths,
    males, mababies, madeaths
):
    female_change = ' ({} new, {} deaths)'.format(febabies, fedeaths)
    male_change   = ' ({} new, {} deaths)'.format(mababies, madeaths)
    if febabies == 0 and fedeaths == 0:
        female_change = ''
    if mababies == 0 and madeaths == 0:
        male_change = ''
    print(
        '{}: {} females{} + {} males{} = {}'.format(
            prefix,
            len(females),
            female_change,
            len(males),
            male_change,
            len(females) + len(males)
        )
    )
    sys.stdout.flush()

# creating initial humans
initial_population_females = int(
        (initial_population / (male_female_ratio + 1))
        + 0.5
)
initial_population_males = initial_population - initial_population_females
total_population_females = {i:0 for i in range(0, initial_population_females)}
total_population_males = {i:0 for i in range(0, initial_population_males)}
females_done_making_babies = {}
last_human_name = len(total_population_females) + len(total_population_males)

# print initial stats
print_stats(
    'initial population',
    total_population_females,
    0,
    0,
    total_population_males,
    0,
    0,
)

# sim begin!
for year in range(1, years + 1):
    # year's overal stats
    new_babies_female = 0
    new_babies_male = 0
    dead_females = []
    dead_males = []

    # handle ladies (1st)
    for i in total_population_females:
        # person i grew 1 year older
        total_population_females[i] += 1
        
        # should person i make babies?
        if (
            total_population_females[i] >= birth_age
            and i not in females_done_making_babies
        ):
            num_of_babies = int(firtility_rate)
            if magic_coin(firtility_rate - int(firtility_rate)):
                num_of_babies += 1

            # baby's gender
            for baby in range(0, num_of_babies):
                if magic_coin(0.5):
                    new_babies_female += 1
                else:
                    new_babies_male += 1
            females_done_making_babies[i] = True

        # person i died
        if total_population_females[i] > life_expectency:
            dead_females.append(i)
    
    # handle gentlemen
    for i in total_population_males:
        # person i grew 1 year older
        total_population_males[i] += 1
        
        # person i died
        if total_population_males[i] > life_expectency:
            dead_males.append(i)

    # remove dead humans :(
    for i in dead_females:
        del total_population_females[i]
    for i in dead_males:
        del total_population_males[i]

    # create newly born humans :)
    for baby in range(0, new_babies_female):
        total_population_females[last_human_name] = 0
        last_human_name += 1
    for baby in range(0, new_babies_male):
        total_population_males[last_human_name] = 0
        last_human_name += 1

    # print stats per year
    print_stats(
        'year {}'.format(year),
        total_population_females,
        new_babies_female,
        len(dead_females),
        total_population_males,
        new_babies_male,
        len(dead_males),
    )
