import random

AGENTS = [

"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/121",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120",

]


def random_agent():
    return random.choice(AGENTS)