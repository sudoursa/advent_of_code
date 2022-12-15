import os
import datetime
from itertools import islice
from functools import reduce
from typing import List, Callable


class Item():
    worry_level: int

    def __init__(self, worry_level):
        self.worry_level = int(worry_level)
    
    def __repr__(self):
        return f"{self.worry_level}"


class Monkey():
    monkey_name: str
    held_items: List[Item]
    worry_mutation: Callable
    total_items_inspected: int
    throw_test_condition: int
    true_monkey_target: int
    false_monkey_target: int
    operation: str   
    monkey_least_common_multiple: int

    def __init__(self, monkey_name, held_items, operation, test, monkey1, monkey2):
        self.monkey_name = monkey_name
        self.held_items = held_items
        self.true_monkey_target = monkey1
        self.false_monkey_target = monkey2
        self._define_worry_mutation(self._define_operation(operation))
        self._define_test(test)
        self.total_items_inspected = 0

    def _define_operation(self, operation) -> str:
        operation_parts = operation.split()
        opperator = operation_parts[3]
        value = "worry_level" if operation_parts[4] == "old" else operation_parts[4]
        lambda_string = f"lambda worry_level: worry_level {opperator} {value}"
        return lambda_string

    def _define_worry_mutation(self, operation: str):
        self.worry_mutation = eval(operation)

    def _inspect_item(self, item: Item) -> None:
        item.worry_level = self.worry_mutation(item.worry_level)
        self.total_items_inspected += 1

    def _define_test(self, test):
        self.test = int(test.split()[-1])

    def make_monkey_aware_of_other_monkies(self, monkies):
        self.all_monkies = monkies
        test_list = []
        for monkey in self.all_monkies:
            test_list.append(monkey.test)
        self.monkey_least_common_multiple = reduce((lambda x, y: x * y), test_list)

    def _throw_item(self, item: Item):
        if item.worry_level % self.test == 0:
            self.all_monkies[self.true_monkey_target].catch_item(item)
        else:
            self.all_monkies[self.false_monkey_target].catch_item(item)

    def _prime_throw_item(self, item: Item):
        # smart evaluate test using prime divisibility rules to reduce calculations
        if self.test == 2:
            if int(str(item.worry_level)[-1]) % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 3:
            string_num = str(item.worry_level)
            list_of_nums = list(map(int, string_num.strip()))
            if sum(list_of_nums)%3 == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 5:
            if str(item.worry_level)[-1] in ["0","5"]:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 7:
            # if self.isDivisibleby7(item.worry_level):
            if item.worry_level % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 11:
            string_num = str(item.worry_level)
            list_of_nums = list(map(int, string_num.strip()))
            if (sum(list_of_nums[::2])-sum(list_of_nums[1::2])) % 11 == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 13:
            # if self.isDivisibleby13(item.worry_level):
            if item.worry_level % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 17:
            # if self.isDivisibleby17(item.worry_level): 
            if item.worry_level % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 19:
            # if self.isDivisibleby19(item.worry_level):
            if item.worry_level % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)
        if self.test == 23:
            # if self.isDivisibleby23(item.worry_level):
            if item.worry_level % self.test == 0:
                self.all_monkies[self.true_monkey_target].catch_item(item)
            else:
                self.all_monkies[self.false_monkey_target].catch_item(item)

    # def isDivisibleby7(self, num):
    #     while len(str(num)) > 3:
    #         last_digit = int(str(num)[-1])
    #         num = int(str(num)[:-1])
    #         num -= last_digit * 2
    #     return (num % 13 == 0)

    # def isDivisibleby13(self, num):
    #     while len(str(num)) > 3:
    #         last_digit = int(str(num)[-1])
    #         num = int(str(num)[:-1])
    #         num += last_digit * 4
    #     return (num % 13 == 0)
   
    # def isDivisibleby17(self, num):
    #     while len(str(num)) > 3:
    #         last_digit = int(str(num)[-1])
    #         num = int(str(num)[:-1])
    #         num -= last_digit * 5
    #     return (num % 17 == 0)
    
    # def isDivisibleby19(self, num):
    #     while len(str(num)) > 3:
    #         last_digits = int(str(num)[-1])
    #         num = int(str(num)[:-1])
    #         num += last_digits * 2
    #     return (num % 19 == 0)

    # def isDivisibleby23(self, num):
    #     while len(str(num)) > 3:
    #         last_digit = int(str(num)[-1])
    #         num = int(str(num)[:-1])
    #         num += last_digit * 7
    #     return (num % 23 == 0)

    def _relief_operation(self, item: Item) -> Item:
        # new_item_worry_level = item.worry_level//3
        item.worry_level %= self.monkey_least_common_multiple
        return item

    def catch_item(self, item: Item) -> None:
        self.held_items.append(item)
        # print(f"Monkey caught item with worry level of {item.worry_level}")

    def complete_turn(self) -> None:
        # start_time = datetime.datetime.now()
        for item in self.held_items:
            self._inspect_item(item)
            self._relief_operation(item)
            # self._throw_item(item)
            self._prime_throw_item(item)
        self.held_items = []
        # end_time = datetime.datetime.now()
        # delta_time = end_time - start_time
        # print(f"It took {self.monkey_name} {delta_time.seconds} seconds")
        
        
def determine_monkey_business(monkey_inspections: List[int]) -> int:
    sorted_inspections = sorted(monkey_inspections)
    return f"{sorted_inspections[-1] * sorted_inspections [-2]}"

def parse_monkey(monkey: List[str]) -> Monkey:
    monkey_name: str = monkey[0].strip()
    held_items: List[Item] = [Item(worry_level=_) for _ in monkey[1].split(": ")[1].strip().split(",")]
    operation: str = monkey[2].split(": ")[1].strip()
    test: str = monkey[3].split(": ")[1].strip()
    monkey1 = int(monkey[4].strip()[-1] )
    monkey2 = int(monkey[5].strip()[-1] )
    monkey= Monkey(monkey_name=monkey_name, held_items=held_items, operation=operation, test=test, monkey1=monkey1, monkey2=monkey2)
    return monkey

def get_monkey_generator(filepath, monkey_length=6):
    with open(f"{filepath}/day11_input.txt") as file:
        for line in file:
            yield [line] + list(islice(file, monkey_length))


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    monkey_gen = get_monkey_generator(dir_path)

    monkies: List[Monkey] = []
    for monkey in monkey_gen:
        monkies.append(parse_monkey(monkey))
    for monkey in monkies:
        monkey.make_monkey_aware_of_other_monkies(monkies)

    for _, round in enumerate(range(10000)):
        # process each round, which is each monkey taking one turn
        # start_time = datetime.datetime.now()
        for monkey in monkies:
            monkey.complete_turn()
        # end_time = datetime.datetime.now()
        # delta_time = end_time - start_time
        # print(f"######### Round {_+1} completed in {delta_time.seconds} seconds ##########")

    monkey_inspections = []
    for number, monkey in enumerate(monkies):
        monkey_inspections.append(monkey.total_items_inspected)
        # print(f"Monkey {number}: {monkey.held_items}")
        print(f"Monkey {number} inspected: {monkey.total_items_inspected}")
    
    print(f"Total Monkey Business was {determine_monkey_business(monkey_inspections)}")
    
