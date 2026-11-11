import pandas as pd


def main():
    categories = ['Social', 'Housing', 'Course Info and Exams', 'Campus Facilities and Resources', 'Motivation and Advice', 'Degree Planning', 'Professional Development']
    files = ['annotated_mcgill_new.tsv', 'annotated_mcgill_top.tsv', 'annotated_concordia_new.tsv', 'annotated_concordia_top.tsv']
    df = pd.DataFrame(columns=['Category', 'mcgill_new', 'mcgill_top', 'concordia_new', 'concordia_top'])
    df['Category'] = categories
    for i in range(4):
        temp = pd.read_csv(files[i], sep='\t')
        temp = temp['coding'].value_counts().reindex(categories, fill_value=0)
        df[df.columns[i+1]] = temp.values
    with open('sampling.md', 'w') as f:
        f.write(df.to_markdown(index=False))


if __name__ == '__main__':
    main()
