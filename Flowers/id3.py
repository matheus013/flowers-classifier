import json
import random
import copy

mark = []
mid = []
database = json.loads(file('flowers.json').read())


def normalize(base):
    for i in base:
        for j in range(0, 4):
            i[j] *= 10


def cut(ref, base):
    sum = 0
    for i in base:
        sum += i[ref]
    return sum / len(base)


def training_base(base, percent):
    trained = []
    while len(trained) < percent * len(base):
        aux = random.randint(0, len(base) - 1)
        if aux in mark:
            continue
        mark.append(aux)
        trained.append(base[aux])
    mid.append([cut(0, trained), cut(1, trained), cut(2, trained), cut(3, trained)])
    # print mid
    return trained


def available(base):
    no_mark = []
    for i in range(0, 150):
        if i not in mark:
            no_mark.append(i)
    return no_mark


def unique_class(base):
    classes = []
    for i in base:
        classes.append(i[4])
    return list(set(classes))


def build_tree(base, attributes, identifier):
    classes = unique_class(base)
    if len(classes) == 1 or identifier >= 4:
        if len(classes) == 2:
            return [classes[0], classes[1]]
        if len(classes) == 0:
            return 0
        return base[0][4]
    left = []
    right = []
    for i in base:
        if i[attributes[identifier]] > mid[0][attributes[identifier]]:
            right.append(i)
        else:
            left.append(i)
    return {'l': build_tree(left, attributes, identifier + 1),
            'r': build_tree(right, attributes, identifier + 1)}


def identify(tree, instance, attributes):
    curr = copy.deepcopy(tree)
    for i in attributes:
        # print curr
        if curr == 'I. versicolor' or curr == 'I. setosa' or curr == 'I. virginica':
            return curr
        if instance[i] > mid[0][i]:
            curr = curr['r']
        else:
            curr = curr['l']
    if isinstance(curr, list):
        if len(curr) == 2:
            return curr[random.randint(0, 1)]
    return curr


def count(base):
    pop = {'I. versicolor': 0, 'I. setosa': 0, 'I. virginica': 0}
    print base[0]
    for i in base:
        pop[database[i][4]] += 1
    print "data", pop


if __name__ == '__main__':
    trained = training_base(database, 0.9)
    ava = available(database)
    tree = build_tree(trained, [0, 1, 2, 3], 0)
    result = 0
    for i in ava:
        if identify(tree, database[i], [0, 1, 2, 3]) == database[i][4]:
            result += 1
    print result / float(len(ava))
