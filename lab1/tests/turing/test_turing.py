import unittest
import os
import tempfile

from turing.rule import Rule
from turing.tape import Tape
from turing.turing_machine import Turing
from turing.cli import load_program


class TestRule(unittest.TestCase):
    def test_set_and_get_action(self):
        r = Rule()
        r.set_action("q0", "1", "q1", "0", "R")
        self.assertEqual(r.get_action("q0", "1"), ("q1", "0", "R"))

    def test_get_action_none(self):
        r = Rule()
        self.assertIsNone(r.get_action("q0", "X"))

    def test_overwrite_action(self):
        r = Rule()
        r.set_action("q0", "1", "q1", "0", "R")
        r.set_action("q0", "1", "q2", "1", "L")
        self.assertEqual(r.get_action("q0", "1"), ("q2", "1", "L"))


class TestTape(unittest.TestCase):
    def test_read_and_write_symbol(self):
        t = Tape("101")
        self.assertEqual(t.read_symbol(), "1")
        t.write_symbol("0")
        self.assertEqual(t.read_symbol(), "0")

    def test_move_right_extend(self):
        t = Tape("1")
        t.move("R")
        self.assertEqual(t.read_symbol(), "_")
        self.assertEqual(t._head, 1)

    def test_move_left_extend(self):
        t = Tape("1")
        t.move("L")
        self.assertEqual(t.read_symbol(), "_")
        self.assertEqual(t._head, 0)

    def test_move_noop(self):
        t = Tape("1")
        t.move("N")
        self.assertEqual(t.read_symbol(), "1")

    def test_invalid_direction(self):
        t = Tape("1")
        with self.assertRaises(ValueError):
            t.move("X")

    def test_clear(self):
        t = Tape("111")
        t.clear()
        self.assertEqual(t.read_word(), "_")
        self.assertEqual(t._head, 0)

    def test_read_word_after_moves(self):
        t = Tape("10")
        t.move("R")
        t.write_symbol("1")
        self.assertEqual(t.read_word(), "_11_")


class TestTuring(unittest.TestCase):
    def test_step_and_state_change(self):
        t = Tape("1")
        r = Rule()
        r.set_action("q0", "1", "q1", "0", "R")
        tm = Turing(t, r, "q0")
        result = tm.step()
        self.assertTrue(result)
        self.assertEqual(t.read_symbol(), "_")  # после движения вправо
        self.assertEqual(tm._state, "q1")

    def test_stop_when_no_rule(self):
        t = Tape("1")
        r = Rule()
        tm = Turing(t, r, "q0")
        self.assertFalse(tm.step())

    def test_multiple_steps(self):
        t = Tape("11")
        r = Rule()
        r.set_action("q0", "1", "q0", "0", "R")
        r.set_action("q0", "_", "halt", "_", "N")
        tm = Turing(t, r, "q0")
        tm.step()
        tm.step()
        self.assertEqual(t.read_word(), "_00_")

    def test_direction_noop(self):
        t = Tape("1")
        r = Rule()
        r.set_action("q0", "1", "halt", "0", "N")
        tm = Turing(t, r, "q0")
        tm.step()
        self.assertEqual(t.read_word(), "_0_")
        self.assertEqual(tm._state, "halt")


class TestLoadProgram(unittest.TestCase):
    def test_load_program_success(self):
        content = """tape=101
start=q0
rule q0 1 q1 0 R
"""
        with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
            f.write(content)
            fname = f.name
        tape, rules, start_state = load_program(fname)
        os.unlink(fname)
        self.assertEqual(tape.read_word(), "_101_")
        self.assertEqual(start_state, "q0")
        self.assertEqual(rules.get_action("q0", "1"), ("q1", "0", "R"))

    def test_load_program_missing(self):
        content = """tape=101"""
        with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
            f.write(content)
            fname = f.name
        with self.assertRaises(ValueError):
            load_program(fname)
        os.unlink(fname)

    def test_load_program_with_comments_and_blank_lines(self):
        content = """# This is a comment
tape=101

start=q0
rule q0 1 q1 0 R
"""
        with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
            f.write(content)
            fname = f.name
        tape, rules, start_state = load_program(fname)
        os.unlink(fname)
        self.assertEqual(tape.read_word(), "_101_")
        self.assertEqual(start_state, "q0")
        self.assertEqual(rules.get_action("q0", "1"), ("q1", "0", "R"))


if __name__ == "__main__":
    unittest.main()
