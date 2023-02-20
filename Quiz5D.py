# CS 303E Quiz 5D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Exit Roads
def exitRoads(roads, cities):
    set1 = set()
    dict1 = {}
    for city in cities:
        set1.add(city)

    for road in roads:
        if road[0] in set1 and road[1] not in set1:
            dict1[road] = True
        else:
            dict1[road] = False

    return dict1



# Problem 2: Recursive Duplicate Non Alphanumeric
def dupeNonAlphanumeric(s):

    if len(s) == 0:
        return s

    if not s[0].isalnum():
        return str(s[0]) + str(s[0]) + str(dupeNonAlphanumeric(str(s[1:])))

    return str(s[0]) + str(dupeNonAlphanumeric(s[1:]))



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

  # print(exitRoads({('Austin', 'Houston'), ('Houston', 'Austin'), ('Austin', 'Dallas'), ('San Antonio', 'El Paso'), ('Houston', 'Dallas'), ('Houston', 'Galveston')}, {'Houston', 'Austin'}))
  # print(exitRoads({('Austin', 'Houston'), ('Houston', 'Austin'), ('Dallas', 'Austin')}, set()))
  # print(exitRoads({('swamp', 'jungle'), ('desert', 'tundra'), ('coast', 'plains')}, {'desert', 'coast', 'swamp', 'sea'}))


  # print(dupeNonAlphanumeric("1+2=3 & I'm sure of it!"))
  # print(dupeNonAlphanumeric("Thanksgiving break in 3 days LET'S GOO!!!"))
  # print(dupeNonAlphanumeric("    ahaha lol POGxD!!!"))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT