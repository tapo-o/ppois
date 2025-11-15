import sys
from turing.tape import Tape
from turing.rule import Rule
from turing.turing_machine import Turing

MAX_STEPS = 10000

def load_program(path: str):
    tape_content = None
    start_state = None
    rules = Rule()

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("tape="):
                tape_content = line.split("=", 1)[1]
            elif line.startswith("start="):
                start_state = line.split("=", 1)[1]
            elif line.startswith("rule"):
                parts = line.split()
                # rule state symbol new_state new_symbol direction
                _, state, symbol, new_state, new_symbol, direction = parts
                rules.set_action(state, symbol, new_state, new_symbol, direction)

    if tape_content is None or start_state is None:
        raise ValueError("Файл должен содержать tape=... и start=...")

    return Tape(tape_content), rules, start_state


def main():
    if len(sys.argv) < 2:
        print("Использование: python client.py <program_file> [-log]")
        sys.exit(1)

    program_file = sys.argv[1]
    log_mode = "-log" in sys.argv

    tape, rules, start_state = load_program(program_file)
    tm = Turing(tape, rules, start_state)

    step_count = 0
    while tm.step() | step_count<= MAX_STEPS:
        step_count += 1
        if log_mode:
            print(f"Шаг {step_count}: состояние={tm._state}, лента={tape.read_word()}, головка={tape._head}")

    print("Результат:", tape.read_word())


if __name__ == "__main__":
    main()
