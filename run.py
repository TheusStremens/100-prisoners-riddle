import argparse
import random

# import matplotlib as plt


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="100 Prisoners Riddle")
    parser.add_argument(
        "--number_prisoners", type=int, default=100, help="Number of prisoners"
    )
    parser.add_argument(
        "--number_runs", type=int, default=1000, help="Number of runs of the experiment"
    )
    return parser.parse_args(argv)


def run_strategy(number_prisoners: int, use_loop: bool = True):
    max_tries = int(number_prisoners / 2)
    # The indices of the vector represents the labels of the boxes in the room.
    # Inside is the paper wth the number. So, open the box of label 1 means
    # access boxes[0].
    boxes = [i for i in range(0, number_prisoners)]
    # The riddle starts with all boxes shuffled.
    random.shuffle(boxes)

    # Stores if each prisoner found its number.
    prisoners_that_found_number = [False for i in range(0, number_prisoners)]
    # For each prisoner.
    for prisoner_number in range(0, number_prisoners):
        found = False
        # Run the Loop strategy of searching by the loop started with its
        # own number.
        if use_loop:
            guess_number = prisoner_number
            for attempt in range(0, max_tries):
                if boxes[guess_number] == prisoner_number:
                    found = True
                    break
                guess_number = boxes[guess_number]
        else:
            # The random strategy.
            possible_choices = [i for i in range(0, number_prisoners)]
            for attempt in range(0, max_tries):
                # Just choose a random box.
                guess_number = random.choice(possible_choices)
                if boxes[guess_number] == prisoner_number:
                    found = True
                    break
                # That box cannot be used again.
                possible_choices.remove(guess_number)
        # Assign the result.
        prisoners_that_found_number[prisoner_number] = found
    return prisoners_that_found_number


def main(args: argparse.Namespace):
    loop_successes = 0
    random_successes = 0
    for i in range(0, args.number_runs):
        prisoners_that_found_number = run_strategy(args.number_prisoners)
        if all(prisoners_that_found_number):
            loop_successes = loop_successes + 1
        prisoners_that_found_number = run_strategy(args.number_prisoners, False)
        if all(prisoners_that_found_number):
            random_successes = random_successes + 1

    print(f"Success with Loop strategy: {loop_successes}")
    print(f"Success with Random strategy: {random_successes}")


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)
