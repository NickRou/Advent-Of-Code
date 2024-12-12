from typing import List

def parse_input(filename: str) -> (List[str], List[str]):
    with open(filename, 'r') as f:
        ret_val = f.read().split("\n\n")
        rules = ret_val[0].splitlines()
        updates = ret_val[1].splitlines()
    f.close()
    return rules, updates

def update_rule_map(rule_map: dict, key, value):
    if key in rule_map:
        rule_map[key].add(value)
    else:
        rule_map[key] = {value}

def get_correct_updates(rules: List[str], updates: List[str]) -> int:
    """
    75|47: 75 must come before 47

    :param rules: list of rules in 'int|int'
    :param updates: list of page numbers
    :return: total number of correct updates
    """
    before_map = {}
    after_map = {}
    for rule in rules:
        before, after = rule.split("|")
        update_rule_map(before_map, before, after)
        update_rule_map(after_map, after, before)

    middle_page_number_total = 0
    for update in updates:
        nums = update.split(",")
        valid_update = True
        for i in range(len(nums)):
            num = nums[i]
            before_nums = [] if i == 0 else nums[0:i]
            after_nums = nums[i+1:len(nums)]

            before_valid = True if num not in after_map else set(before_nums).issubset(after_map[num])
            after_valid = True if num not in before_map else set(after_nums).issubset(before_map[num])

            if not (before_valid and after_valid):
                valid_update = False
                break

        if not valid_update:
            middle_idx = int((len(nums)-1)/2)
            nums_set = set(nums)
            for num in nums:
                if num in before_map and len(nums_set.intersection(before_map[num])) == middle_idx:
                    middle_page_number_total += int(num)
                    break

    return middle_page_number_total

if __name__=='__main__':
    rules, updates = parse_input("day5.input")
    valid_updates = get_correct_updates(rules, updates)
    print("Valid Updates: " + str(valid_updates))
