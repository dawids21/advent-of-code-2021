def apply_rules(polymers, rules, num_of_polymers):
    new_polymers = {x: 0 for x in polymers}
    for polymer in polymers:
        new_polymer = rules[polymer]
        first_polymer = polymer[0] + new_polymer
        second_polymer = new_polymer + polymer[1]
        num_of_new_polymer = polymers[polymer]
        new_polymers[first_polymer] += num_of_new_polymer
        new_polymers[second_polymer] += num_of_new_polymer
        num_of_polymers[new_polymer] += num_of_new_polymer
    return new_polymers


def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    template = ""
    rules = {}
    types_of_polymers = set()
    for i in range(len(lines)):
        if i == 0:
            template = lines[0].strip()
            types_of_polymers.update({x for x in template})
            continue
        if i == 1:
            continue
        rule = lines[i].strip().split(" -> ")
        rules[rule[0]] = rule[1]
        types_of_polymers.add(rule[1])
    polymers = {x: template.count(x) for x in rules}
    num_of_polymers = {x: template.count(x) for x in types_of_polymers}
    for i in range(40):
        polymers = apply_rules(polymers, rules, num_of_polymers)
    print(max(num_of_polymers.values()) - min(num_of_polymers.values()))


if __name__ == '__main__':
    main()
