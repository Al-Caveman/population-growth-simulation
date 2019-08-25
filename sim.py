import random
random.seed(0)

life_expectency = 77.45         # poland's
firtility_rate = 1.32           # poland's
initial_population_males = 10   # i made it up.
initial_population_females = 10 # i made it up.
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

# sim begin!
total_population_males = [0 for i in range(0, initial_population_males)]
total_population_females = [0 for i in range(0, initial_population_females)]
female_done_making_bies = {}

# print initial stats
print(
    'initial population: {}'.format(
        initial_population_males + initial_population_females
    )
)
for year in range(1, years + 1):
    # handle ladies (1st)
    for i in range(0, len(total_population_females)):
        # person i grew 1 year old
        total_population_females[i] += 1
        
        # person i made babies
        if i not in female_done_making_bies:
            num_of_babies = int(firtility_rate)
            print('{} made {} babis'.format(i, num_of_babies))
            if magic_coin(firtility_rate - num_of_babies):
                num_of_babies += 1
            # baby's gender
            for baby in range(0, num_of_babies):
                if magic_coin(0.5): # female - ladies 1st again
                    total_population_females.append(0)
                else: # male
                    total_population_males.append(0)
            female_done_making_bies[1] = True

        # person i died
        if total_population_females[i] > life_expectency:
            total_population_females.pop(i)

    # handle gentlemen
    for i in range(0, len(total_population_males)):
        # person i grew 1 year old
        total_population_males[i] += 1
        
        # person i died
        if total_population_males[i] > life_expectency:
            total_population_males.pop(i)

    # print stats per year
    print(
        'total population: {}'.format(
            len(total_population_males) + len(total_population_females)
        )
    )
