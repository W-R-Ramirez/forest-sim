from random import random, randrange
from time import sleep

N = 10
lumberjacks = .1
bears = .02
trees = .5

number_of_lumberjacks = int((N**2)*lumberjacks)
number_of_bears = int((N**2)*bears)
number_of_trees = int((N**2)*trees)

jack_list = ["Jack"]*number_of_lumberjacks
bear_list = ["Bear"]*number_of_bears
tree_list = ["Tree"]*number_of_trees

lumber = 0
maw = 0
date = 0

class forest:
    def __init__(self):
        self.jacks_working = number_of_lumberjacks
        self.bears_wandering = number_of_bears
        self.trees_being = number_of_trees

        self.date = 0
        self.new_tree_monthly = 0
        self.new_tree_yearly = 0
        self.lumber_monthly = 0
        self.lumber_yearly = 0
        self.bear_attacks_monthly = 0
        self.bear_attacks_yearly = 0
    def new_tree(self):
        self.new_tree_monthly = self.new_tree_monthly + 1
        self.new_tree_yearly = self.new_tree_yearly + 1
        self.trees_being = self.trees_being + 1
    def new_hire(self):
        self.jacks_working = self.jacks_working + 1
    def chop_chop(self):
        self.lumber_monthly = self.lumber_monthly + 1
        self.lumber_yearly = self.lumber_yearly + 1
        self.trees_being = self.trees_being - 1
    def attack_attack(self):
        self.bear_attacks_monthly = self.bear_attacks_monthly + 1
        self.bear_attacks_yearly = self.bear_attacks_yearly + 1
        self.jacks_working = self.jacks_working - 1
    def time(self):
        self.date = self.date + 1
        if self.date%12 == 0:
            self.check_yearly()
        digits_in_date = len(str(self.date))
        if  digits_in_date == 1:
            month = "000"+str(self.date)
        elif digits_in_date == 2:
            month = "00"+str(self.date)
        elif digits_in_date == 3:
            month = "0" + str(self.date)
        else:
            month = str(self.date)
        if self.new_tree_monthly:
            #print "Month " + month + ": " + str(self.new_tree_monthly) + " new saplings made."
            self.new_tree_monthly = 0
        if self.lumber_monthly:
            #print "Month " + month + ": " + str(self.lumber_monthly) + " pieces of lumber harvaster."
            self.lumber_monthly = 0
        if self.bear_attacks_monthly:
            #print "Month " + month + ": " + str(self.bear_attacks_monthly) + " lumberjacks attacked"
            self.bear_attacks_monthly = 0

        

    def check_yearly(self):
        """ Hire/fire new lumberjacks, and send the zoo after bears/make new bears.
            Also, don't forget the other shit, naming the total new trees, total cut down, 
            and total number of bear attacks."""
        year = self.date/12
        digits_in_year = len(str(year))
        if digits_in_year == 1:
            year = "Year 00" + str(year) + ": "
        elif digits_in_year == 2:
            year = "Year 0" + str(year) + ": "
        else:
            year = "Year" + str(year) + ": "
        
        jacks_hired = False
        bears_sent_away = False
        if len(str(self.lumber_yearly)) > 1:
            num_hired = int(str(self.lumber_yearly)[0])
        else:
            num_hired = 0
        if self.jacks_working <= self.lumber_yearly:
            for i in range(num_hired + 1):
                self.jacks_working = self.jacks_working + 1
                jacks_hired = True
                print "JACK HireD"
                place_things(["Jack"])
        else:
            if self.jacks_working > 1:
                self.jacks_working = self.jacks_working - 1
                remove_things("Jack")
                print "HACK Fired"
        if self.bear_attacks_yearly:
            if self.bears_wandering > 1:
                bears_sent_away = True
                self.bears_wandering = self.bears_wandering - 1
                remove_things("Bear")
                print "BEAR CAUSGT"
        else:
            self.bears_wandering = self.bears_wandering + 1
            place_things(["Bear"])
            print "BEAR ADDED"
        if jacks_hired:
            if bears_sent_away:
                print year + str(num_hired + 1) + " Lumberjack was hired, 1 bear was captured by the zoo"
            else:
                print year + str(num_hired + 1) + " Lumberjack was hired, 1 bear was born"
        else:
            if bears_sent_away:
                print year + "1 Lumberjack was fired, 1 bear was captured by the zoo"
            else:
                print year + "1 Lumberjack was fired, 1 bear was born"

        print year + str(self.new_tree_yearly) + " new saplings made this year, " + str(self.lumber_yearly) + " trees cut down this year, " + str(self.bear_attacks_yearly) + " bear attacks this year"
        print year + "There are " + str(self.jacks_working) + " Lumberjacks, " + str(self.bears_wandering) + " Bears, " + str(self.trees_being) + " Trees."
        test()
        self.new_tree_yearly = 0
        self.lumber_yearly = 0
        self.bear_attacks_yearly = 0

class plot:
    def __init__(self, pos, identity):
        self.identity = identity
        self.occupied = False
        self.warning = False
        self.stop = False
        self.pos = pos
        self.occupation = "____"
        self.age = 0
        x,y = pos
        self.x,self.y = pos
        top = identity - N
        top_left = identity - (N+1)
        top_right = identity - (N-1)
        left = identity - 1
        right = identity + 1
        bottom_left = identity + (N-1)
        bottom_right = identity + (N+1)
        bottom = identity + N
        if (x == 0 or x == N-1) and (y == 0 or y == N-1):
            self.numb_adj = 3
            if x == 0 and y == 0:
                self.adjs = [right, bottom_right, bottom]
            elif x == 0 and y == N-1:
                self.adjs = [right, top_right, top]
            elif x == N-1 and y == 0:
                self.adjs = [left, bottom_left, bottom]
            elif x == N-1 and y == N-1:
                self.adjs = [left, top_left, top]
        elif x == 0 or x == N-1 or y == 0 or y == N-1:
            self.numb_adj = 5
            if x == 0:
                self.adjs = [top, top_right, right, bottom_right, bottom]
            elif x == N-1:
                self.adjs = [top, top_left, left, bottom_left, bottom]
            elif y == 0:
                self.adjs = [left, bottom_left, bottom, bottom_right, right]
            elif y == N-1:
                self.adjs = [left, top_left, top, top_right, right]
        else:
            self.numb_adj = 8
            self.adjs = [top, top_left, top_right, left, right, bottom_left, bottom_right, bottom]

    def change_occupation(self, to_what):
        if to_what == "____":
            self.occupied = False
            self.age = 0
        else:
            self.occupied = True
        self.occupation = to_what

    # Returns True if there is at least one open space, false otherwise.
    def test_adj(self, plots):
        self.filled = []
        self.empty = []
        for spot in self.adjs:
            if plots["Plot"+str(spot)].occupied:
                self.filled.append(spot)
            else:
                self.empty.append(spot)
        if len(self.filled) == len(self.adjs):
            return False
        else:
            return True

    def collision(self, mover, moved, forest):
        if mover.occupation == "Bear":
            if moved.occupation == "Tree":
                moved.occupation = "Beee"
                mover.occupation = "____"
                mover.occupied = False
            elif moved.occupation == "Jack":
                forest.attack_attack()
                moved.occupation = "Bear"
                mover.occupation = "____"
                mover.occupied = False
                mover.stop = True
            elif moved.occupation == "Bear" or moved.occupation == "Beee":
                if not mover.warning:
                    mover.warning = True
                else:
                    mover.stop = True

        elif mover.occupation == "Jack":
            if moved.occupation == "Tree":
                if moved.age >= 12:
                    forest.chop_chop()
                    mover.occupation = "____"
                    mover.occupied = False
                    moved.occupation = "Jack"
                    moved.age = 0
                    mover.stop = True
            elif moved.occupation == "Bear" or moved.occupation == "Beee":
                forest.attack_attack()
                mover.occupied = False
                mover.occupation = "____"
                mover.stop = True
            elif moved.occupation == "Jack":
                if not moved.warning:
                    mover.warning = True
                else:
                    mover.stop = True

        elif mover.occupation == "Beee":
            if moved.occupation == "Tree":
                moved.occupation == "Beee"
                mover.occupation == "Tree"
            elif moved.occupation == "Bear":
                if not mover.warning:
                    mover.warning = True
                else:
                    mover.stop = True
            elif moved.occupation == "Jack":
                forest.attack_attack()
                moved.occupation = "Bear"
                mover.occupation = "Tree"


    def wander(self, plots, plot, forest):
        self.test_adj(plots)
        i = self.adjs[randrange(self.numb_adj)]
        if i in self.empty:
            if self.occupation == "Beee":
                plots["Plot"+str(i)].change_occupation("Bear")
                self.occupation = "Tree"
            else:
                plots["Plot"+str(i)].change_occupation(plot.occupation)
                self.occupation = "____"
                self.occupied = False
               
        else:
            self.collision(plot, plots["Plot"+str(i)], forest)
        
identity = 0
plots = {}
for i in range(N):
    for j in range(N):
        identity = identity + 1
        title = "Plot"+str(identity)
        pos = (j,i)
        plots[title] = plot(pos, identity)


def place_things(type_list):
    if forest.jacks_working + forest.bears_wandering + forest.trees_being < 100:
        while type_list:
            i = randrange(1,N**2+1)
            plot = plots["Plot"+str(i)]
            if not plot.occupied:
                if type_list:
                    placed = type_list.pop()
                    plot.change_occupation(placed)
                if plot.occupation == "Tree":
                    plot.age = 65

def remove_things(identity):
    if identity == "Jack":
        amount = forest.jacks_working
    elif identity == "Bear":
        amount = forest.bears_wandering
    else:
        amount = forest.trees_being
    if amount > 1:
        thing = randrange(0, amount)
        i = []
        for n in range(1,101):

            if plots["Plot"+str(n)].occupation == identity:
                i.append(n)
        plots["Plot"+str(i[thing])].change_occupation("____")  

forest = forest()

place_things(jack_list)
place_things(bear_list)
place_things(tree_list)



def step(plots, forest):


    for plot in plots.itervalues():
        if plot.occupation == "Jack":
            for i in range(3):
                if not plot.stop:
                    plot.wander(plots, plot, forest)
        elif "Bear" == plot.occupation:
            for i in range(5):
                if not plot.stop:
                    plot.wander(plots, plot, forest)
        elif "Tree" == plot.occupation or "Beee" == plot.occupation:
            plot.age = plot.age + 1
            if plot.test_adj(plots):
                if plot.age >= 12 and plot.age < 120:
                    if random() < .1:
                        forest.new_tree()
                        plots["Plot"+str(plot.empty[randrange(len(plot.empty))])].change_occupation("Tree")
                elif plot.age >= 120:
                    if random() < .2:
                        forest.new_tree()
                        plots["Plot"+str(plot.empty[randrange(len(plot.empty))])].change_occupation("Tree")
                    
            if "Beee" == plot.occupation:
                for i in range(5):
                    if not plot.stop:
                        plot.wander(plots, plot, forest)
        plot.stop = False
    forest.time()


def print_forest():
    for i in range(1,N**2,N):
        print plots["Plot"+str(i)].occupation, plots["Plot"+str(i+1)].occupation, plots["Plot"+str(i+2)].occupation, plots["Plot"+str(i+3)].occupation, plots["Plot"+str(i+4)].occupation, plots["Plot"+str(i+5)].occupation, plots["Plot"+str(i+6)].occupation, plots["Plot"+str(i+7)].occupation, plots["Plot"+str(i+8)].occupation, plots["Plot"+str(i+9)].occupation
        print ""







def test():
    j=0
    t=0
    b=0
    a=0
    for i in range(1,N**2+1):
        if plots["Plot"+str(i)].occupation == "Jack":
            j = j+1
            a = a+1
        elif plots["Plot"+str(i)].occupation == "Bear":
            b = b+ 1
            a = a+1
        elif plots["Plot"+str(i)].occupation == "Beee":
            t = t+1
            b = b+1
            a = a+1
        elif plots["Plot"+str(i)].occupation == "Tree":
            t = t+1
            a = a+1
        else:
            a = a+1

    print "there are " + str(j) + " jacks, " + str(t) + " trees, and " + str(b) + "bears"

for i in range(480):
    step(plots, forest)
