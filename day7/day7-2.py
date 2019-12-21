import intcode
import itertools

code = list(map(int, open("./input.txt", "r").read().split(",")))


def main():
    part2 = 0
    for phase in itertools.permutations(range(5, 10)):
        amps = [intcode.Intcode(code, [phase[i]]) for i in range(5)]
        previous_output = 0
        while all(not amp.halted for amp in amps):
            for amp in amps:
                amp.input(previous_output)
                output = amp.run()
                if not amp.halted:
                    previous_output = output
        part2 = max(part2, previous_output)
    print(part2)


main()


def part1Alt():
    part1 = 0
    for phase in itertools.permutations(range(5)):
        amps = [intcode.Intcode(code, [phase[i]]) for i in range(5)]
        previous_output = 0
        for amp in amps:
            amp.input(previous_output)
            previous_output = amp.execute()
        part1 = max(part1, previous_output)
    print(part1)
