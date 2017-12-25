# A class object for handling elite logs/journals.
import json
import os

class EliteJournal():
    loaded_journals = 0

    # Set a few things, like the commander's name, and the log file path.
    def __init__(self, cmdr_name, log_path):
        self.cmdr_name = cmdr_name
        self.log_path = log_path

    # Loaded all the log files and parse in to the journal.
    def load_journal(self):
        # Loads all the events into a giant array.
        journal = []
        logfiles = self.list_log_files(printout=False)
        # Loop through each file (which are newline terminated JSON, a little janky)
        for logfile in logfiles:
            with open(self.log_path + "/" + logfile) as logfh:
                print("Scanning: " + (self.log_path + "/" + logfile))
                for row in logfh:
                    log = json.loads(row)
                    journal.append(log)
        self.loaded_journals = len(journal)
        self.journal = journal

    #List all the log files.
    def list_log_files(self, printout=True):
        # Lists all files in the logs folder.
        logfiles = []
        for logfile in os.listdir(self.log_path):
            if printout:
                print(logfile)
            logfiles.append(logfile)
        return logfiles

    def filter_entries(self, entry_type):
        # Filter entries so that only a specific type shows up.
        filtered_journal_entries = []
        for journal_entry in self.journal:
            if journal_entry["event"] == entry_type:
                filtered_journal_entries.append(journal_entry)
        return filtered_journal_entries


    #Something to show.
    def __repr__(self):
        return "Journal for CMDR "+self.cmdr_name+" with "+str(self.loaded_journals)+" entries loaded."