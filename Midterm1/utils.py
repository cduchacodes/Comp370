def avg_cols(source, table, column):
    values = table[column]
    clean = [ v for v in values if v is not None ]
    dropped = len(values) - len(clean)
    print(f"{source}: n={len(clean)}, dropped={dropped}, mean=(sum(clean)/len(clean))")




if __name__ == '__main__':
    table = {ratings: [1, 5, 9, None, None]}
    avg_cols(__name__, table, 'ratings')
