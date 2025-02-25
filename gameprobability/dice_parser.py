"""Parse a complex dice string and roll dice for it"""
import os
import re
from random import randint

from whiptail import Whiptail

TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

WHIPTAIL_SETTINGS = {
    "title": "Monty Hall",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10,
}

# Terms
# Complex dice string: 4d6-1d4+2
# Simple dice string: 4d6
# Parsed dice: [{'operator': '+', 'die_size': 6, 'number_of_dice': 4}]
# Parsed die: {'operator': '+', 'die_size': 6, 'number_of_dice': 4}

def roll_parsed_die(parsed_die):
    """Roll a parsed die"""
    operator = parsed_die['operator']
    number_of_dice = parsed_die['number_of_dice']
    die_size = parsed_die['die_size']
    total = sum([
        randint(1, die_size)
        for _
        in range(number_of_dice)
    ])
    total = total if operator == '+' else -1 * total
    print(f"{operator}{number_of_dice}D{die_size}: {total}")
    return total

def roll_parsed_dice(parsed_dice):
    """Roll a complex parsed dice string"""
    return sum([roll_parsed_die(parsed_die) for parsed_die in parsed_dice])

def validate_complex_dice_string(dice_string: str):
    """Validate and clean dice string, or raise exception"""
    no_whitespace = re.sub(r'\s', '', dice_string)
    valid = re.fullmatch(r'[\d\+\-dD]+', no_whitespace)
    if not valid:
        raise Exception("Given dice string is not valid")
    first_char = no_whitespace[:1]
    if not (first_char == '+' or first_char == '-'):
        no_whitespace = f'+{no_whitespace}'
    return no_whitespace

def validate_simple_dice_string(dice_string: str):
    """Validates a single term dice string for proper structure"""
    pattern = re.compile(r'[\+\-]\d*D?\d+')
    valid = re.fullmatch(pattern, dice_string)
    if not valid:
        raise Exception("Given dice string is not valid")

def parse_complex_dice_string(dice_string: str):
    """Takes a complex dice string and parses it into a list"""
    clean_dice_string = validate_complex_dice_string(dice_string)
    pattern = re.compile(r'(\+|\-)')
    chunks = [chunk for chunk in re.split(pattern, clean_dice_string)]
    if not chunks[0]:
        # First element is empty
        chunks.pop(0)
    fully_parsed = []
    for index in range(0, len(chunks), 2):
        simple_dice_string = ''.join(chunks[index:index + 2])
        parsed_simple_dice_string = parse_simple_dice_string(simple_dice_string)
        fully_parsed.append(parsed_simple_dice_string)
    print(fully_parsed)
    return fully_parsed

def parse_simple_dice_string(dice_string: str):
    """Parse a simple (1 term) dice string"""
    print(dice_string)
    validate_simple_dice_string(dice_string)
    operator, dice_definition = dice_string[:1], dice_string[1:]
    if 'D' in dice_definition:
        # This is a dice definition (e.g. 2d20)
        die_split = [x for x in dice_definition.split('D')]
        number_of_dice = die_split[0] if len(die_split[0]) > 0 else '1'
        die_size = die_split[1]
    else:
        # This is a constant (e.g. a +2 modifier)
        number_of_dice = dice_definition
        die_size = '1'
    return {
        'operator': operator,
        'number_of_dice': int(number_of_dice),
        'die_size': int(die_size)
    }

def main():
    """Main line logic"""
    wt = Whiptail(**WHIPTAIL_SETTINGS)
    (dice_string, res_code) = wt.inputbox("Input your dice string")
    if res_code == 1:
        exit()
    dice_string = dice_string.upper()
    parsed_dice = parse_complex_dice_string(dice_string)
    total = roll_parsed_dice(parsed_dice)
    print(f'Total: {total}')


if __name__ == '__main__':
    main()
