import unittest

from turing.rule import Rule
from turing.tape import Tape
from turing.turing_machine import Turing


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

    def test_multiple_rules(self):
        r = Rule()
        r.set_action("q0", "0", "q1", "1", "R")
        r.set_action("q1", "1", "q2", "0", "L")
        self.assertEqual(r.get_action("q0", "0"), ("q1", "1", "R"))
        self.assertEqual(r.get_action("q1", "1"), ("q2", "0", "L"))


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

    def test_multiple_moves_extend(self):
        t = Tape("1")
        t.move("R")
        t.move("R")
        self.assertEqual(t.read_word(), "_1__")
        self.assertEqual(t._head, 2)

    def test_write_in_new_cell(self):
        t = Tape("1")
        t.move("R")
        t.write_symbol("X")
        self.assertEqual(t.read_word(), "_1X_")


class TestTuring(unittest.TestCase):
    def test_step_and_state_change(self):
        t = Tape("1")
        r = Rule()
        r.set_action("q0", "1", "q1", "0", "R")
        tm = Turing(t, r, "q0")
        result = tm.step()
        self.assertTrue(result)
        self.assertEqual(t.read_symbol(), "_")
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
        while tm.step():
            pass
        self.assertEqual(t.read_word(), "_00_")
        self.assertEqual(tm._state, "halt")

    def test_state_changes_chain(self):
        t = Tape("1")
        r = Rule()
        r.set_action("q0", "1", "q1", "0", "R")
        r.set_action("q1", "_", "q2", "_", "N")
        tm = Turing(t, r, "q0")
        tm.step()
        tm.step()
        self.assertEqual(tm._state, "q2")

    def test_symbol_change_same_state(self):
        t = Tape("1")
        r = Rule()
        r.set_action("q0", "1", "q0", "0", "N")
        tm = Turing(t, r, "q0")
        tm.step()
        self.assertEqual(t.read_word(), "_0_")
        self.assertEqual(tm._state, "q0")


if __name__ == "__main__":
    unittest.main()
