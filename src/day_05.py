from collections import defaultdict, namedtuple


def parse(lines):
    split_index = lines.index("")
    rules = defaultdict(set)
    for rule_line in lines[:split_index]:
        page, page_after = map(int, rule_line.split("|"))
        rules[page].add(page_after)
    updates = [list(map(int, update_line.split(","))) for update_line in lines[split_index + 1:]]
    return rules, updates


def is_correct_order(update, rules):
    for i, page in enumerate(update):
        pages_before = update[:i]
        if any(page_before in rules[page] for page_before in pages_before):
            return False
    return True


def part_1(rules, updates):
    middle_page_total = 0
    for update in updates:
        if not is_correct_order(update, rules):
            continue
        middle_page_total += update[len(update) // 2]
    return middle_page_total


def part_2(rules, updates):
    middle_page_total = 0
    RuleCount = namedtuple("RuleCount", ["page", "count"])
    for update in updates:
        if is_correct_order(update, rules):
            continue
        rule_counts = []
        for page in update:
            # For each page in this update, count the number of rules relevant to the update
            count = sum((page_after in update) for page_after in rules[page])
            rule_counts.append(RuleCount(page, count))
        # Reverse sort the rule counts, higher rule counts indicate the page should be further to the left
        rule_counts.sort(key=lambda rule_count: rule_count.count, reverse=True)
        middle_page_total += rule_counts[len(update) // 2].page
    return middle_page_total
