import os
import json

def load_events(logs_path):
    # Loads all the events into a giant array.
    events = []
    logfiles = list_log_files(logs_path, printout=False)
    # Loop through each file (which are newline terminated JSON, a little janky)
    for logfile in logfiles:
        with open(logs_path+"/"+logfile) as logfh:
            print("Scanning: "+(logs_path+"/"+logfile))
            for row in logfh:
                log = json.loads(row)
                events.append(log)
    print("Loaded "+str(len(events))+" event entries from log files.")
    return events

def enumerate_event_types(logs_path):
    event_types = []
    all_events = load_events(logs_path)

    for event in all_events:
        event_types.append(event["event"])

    return set(event_types)


def list_log_files(logs_path, printout=True):
    # Lists all files in the logs folder.
    logfiles = []
    for logfile in os.listdir(logs_path):
        if printout:
            print(logfile)
        logfiles.append(logfile)
    return logfiles


def show_event_type_detail(logs_path, event_type):
    logfiles = list_log_files(logs_path, printout=False)
    events = []
    for logfile in logfiles:
        with open(logs_path + "/" + logfile) as logfh:
            print("Scanning: " + (logs_path + "/" + logfile))
            for row in logfh:
                log = json.loads(row)
                if log["event"] == event_type:
                    events.append(log)
    return events