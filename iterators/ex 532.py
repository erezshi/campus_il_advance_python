class MusicNotes:
    def __init__(self):
        self._notes_fcs = [55,61.74,65.41,73.42,82.41,87.31,98]
        self.eml_index = -1
        self._counter = 0
        self._counter_total = len(self._notes_fcs) * 5

    def get_notes(self):
        return self._notes_fcs

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter >= self._counter_total:
            raise StopIteration()
        if self.eml_index >= len(self._notes_fcs) -1:
            self._notes_fcs = list(map(lambda x: x * 2, self._notes_fcs))
            self.eml_index = -1
        self._counter += 1
        self.eml_index += 1

        return self._notes_fcs[self.eml_index]

notes_fc = MusicNotes()
for fc in notes_fc:
    print(fc)

