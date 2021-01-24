

class MusicalNotes:

    def __init__(self):
        # self._notes = {
        #     "La": 55,
        #     "Si": 61.74,
        #     "Do": 65.41,
        #     "Re": 73.42,
        #     "Mi": 82.41,
        #     "Fa": 87.31,
        #     "Sol": 98
        # }
        self._notes = [
            ("La", 55),
            ("Si", 61.74),
            ("Do", 65.41),
            ("Re", 73.42),
            ("Mi", 82.41),
            ("Fa", 87.31),
            ("Sol", 98)
        ]
        
    def get_note_frequency(self,note):
        return self._notes[self.eml_index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.eml_index >= len(self._employee_lst) -1:
            raise StopIteration()
        self.eml_index += 1
        return self._employee_lst[self.eml_index].get_name()
    





# notes = {
#             "La": 55,
#             "Si": 61.74,
#             "Do": 65.41,
#             "Re": 73.42,
#             "Mi": 82.41,
#             "Fa": 87.31,
#             "Sol": 98
#         }

# print(notes["La"])

# L = [
#     ("La", 55),
#     ("Si", 61.74),
#     ("Do", 65.41),
#     ("Re", 73.42),
#     ("Mi", 82.41),
#     ("Fa", 87.31),
#     ("Sol", 98)
# ]

# print(L[3][0])

# # for k, v in notes.items():
# #     print(k)

# # for key in notes:
# #     print(notes[key])

# mo = map(lambda key: notes[key] * 2, notes)
# # print(next(mo))
# # print(next(mo))
# # print(next(mo))
# # print(next(mo))
# # print(next(mo))
# # print(next(mo))
# for val in mo:
#     print(val)