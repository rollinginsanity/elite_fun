# Just some experiments with the log files from elite dangerous.
# Reece Payne, Dec 2017

import os
import elite_fun
from elite_fun.elite_journal import EliteJournal
import pprint

logs_folder_location = "logs/" # Create this directory or set it to where ever your logs are stored.

script_path = os.path.realpath(__file__)
logs_path = os.path.realpath(logs_folder_location)

elite_journal = EliteJournal("Aton Keller", logs_path)
elite_journal.load_journal()

print(elite_journal)

FSD_jumps = elite_journal.filter_entries("FSDJump")

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(FSD_jumps[0])