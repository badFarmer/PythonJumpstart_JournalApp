import os


def load(name):
    # todo: populate from file if it exists
    return[]


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl' ))
    print("..... saving to {}".format(filename))

    with open(filename, 'w') as file_out:

        for entry in journal_data:
            file_out.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)