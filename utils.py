
# main.py
def get_square_names(SQUARE_NUMBERS, SQUARE_LETTERS):
  square_names = []
  for n in SQUARE_NUMBERS:
    for char in SQUARE_LETTERS:
        square_names.append(char + n)
  return square_names