from enum import Enum
from enum import auto
from random import random
from typing import Set
from typing import Tuple


class ChipCondition(Enum):
    GOOD = auto()
    BAD = auto()


class Chip:
    def __init__(self, condition: ChipCondition) -> None:
        self.condition = condition


class BadChipStrategy(Enum):
    COIN_FLIP = 0.5
    ALWAYS_REPORT_GOOD = 1.0
    ALWAYS_REPORT_BAD = 0.0

    def report(self) -> ChipCondition:
        return ChipCondition.GOOD if random() < self.value else ChipCondition.BAD


def identify_good_chip(chips: Set, *, strategy: BadChipStrategy = BadChipStrategy.COIN_FLIP) -> Chip:
    """Identifies a good chip in a set of chips containing more good than bad chips.

    Args:
        chips: A set of chips containing more good than bad chips.
        strategy: A strategy that bad chips use when reporting on the condition of another chip.

    Returns:
        One of the good chips from the input set.
    """
    if len(chips) <= 2:
        return chips.pop()
    selected_chips = set()
    while len(chips) > 1:
        first, second = chips.pop(), chips.pop()
        test_result = __test_chips(first, second, strategy=strategy)
        if test_result == (ChipCondition.GOOD, ChipCondition.GOOD):
            selected_chips.add(first)  # second is equally fine here
    if len(chips) == 1 and len(selected_chips) % 2 == 0:
        selected_chips.add(chips.pop())
    return identify_good_chip(selected_chips, strategy=strategy)


def identify_all_good_chips(chips: Set, *, strategy: BadChipStrategy = BadChipStrategy.COIN_FLIP) -> Set:
    """Identifies all good chips in a set of chips that contains more good than bad chips.

    Args:
        chips: A set of chips containing more good than bad chips.
        strategy: A strategy that bad chips use when reporting on the condition of another chip.

    Returns:
        All the good chips from the input set.
    """
    c0 = identify_good_chip(chips.copy(), strategy=strategy)
    chips.remove(c0)
    good_chips = {c0}
    while len(chips) > 0:
        second = chips.pop()
        if __test_chips(c0, second, strategy=strategy) == (ChipCondition.GOOD, ChipCondition.GOOD):
            good_chips.add(second)
    return good_chips


def __test_chips(first: Chip, second: Chip, *, strategy: BadChipStrategy) \
        -> Tuple[ChipCondition, ChipCondition]:
    return (second.condition if first.condition == ChipCondition.GOOD else strategy.report(),
            first.condition if second.condition == ChipCondition.GOOD else strategy.report())
