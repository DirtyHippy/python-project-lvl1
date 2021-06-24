from brain_games.cores import core
from brain_games.games import brain_even
from brain_games.games import brain_calc
from brain_games.games import brain_gcd
from brain_games.games import brain_progression
from brain_games.games import brain_prime


def run_even():
    core.run(brain_even)


def run_calc():
    core.run(brain_calc)


def run_gcd():
    core.run(brain_gcd)


def run_progression():
    core.run(brain_progression)


def run_prime():
    core.run(brain_prime)
