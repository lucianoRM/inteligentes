import itertools

keys = {}
possible_values = {}
values_relationships = {}


def hash_value(index,value):
    return '{:d}{:s}'.format(index,value)

#possible values for every column
def create_key_index(line):
    values = line.split(',')
    for i in xrange(len(values)):
        keys[i] = values[i].rstrip('\n')

def load_relationship(v1,v2):
    if not values_relationships.has_key(v1):
        values_relationships[v1] = {v2:1}
    else:
        if v2 not in values_relationships[v1]:
            values_relationships[v1][v2] = 1
        else:
            values_relationships[v1][v2] += 1


def load_relationships(line):
    values = line.split(',')
    values = [value.rstrip('\n') for value in values]
    hashed_values = []
    for i in xrange(len(values)):
        hashed_values.append(hash_value(i,values[i]))
    for combination in itertools.combinations(hashed_values,2):
        load_relationship(combination[0], combination[1])
        #load_relationship(combination[1], combination[0])

def load_value(index, value):
    key = keys[index]
    value = value.rstrip('\n')
    if not possible_values.has_key(key):
        possible_values[key] = {value:1}
    else:
        if not possible_values[key].has_key(value):
            possible_values[key][value] = 1
        else:
            possible_values[key][value] += 1

def load_line(line):
    values = line.split(',')
    for i in xrange(len(values)):
        load_value(i, values[i])

#open file
f = open('mushrooms.csv', 'r')
first_line = f.readline()
create_key_index(first_line)
print keys
for line in f:
    load_line(line)
    load_relationships(line)

for key in possible_values.keys():
    print key
    values_str = []
    for value in possible_values[key].keys():
        values_str.append(value + " : " + str(possible_values[key][value]))
    print ','.join(values_str)

print "\n############################\n"
for key in values_relationships.keys():
    print key
    vr = values_relationships[key]
    vr = sorted(vr.items(), key=lambda t: t[1])
    for value in vr:
        print "\t" + value[0] + " : " + str(value[1])

f.close()

