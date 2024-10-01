import pandas as pd
from joblib import Parallel, delayed
from rapidfuzz import fuzz
from itertools import combinations
import recordlinkage
from recordlinkage.preprocessing import clean


def read_dataset(file):
    """Section One: Read Dataset and keep it in df."""
    df = pd.read_excel(file)
    return df


def find_duplicate_id_number(df):
    """Section Two: Duplicate id_number."""
    dup_rows = df[(df['id_doc'].isin([1, 7])) & (df['id_number'].duplicated(keep=False))]
    dup_rows_sorted = dup_rows.sort_values(by=['SB-district', 'SB-cfac_name', 'id_doc', 'id_number'])
    return dup_rows_sorted


def find_duplicate_mobile_number(df):
    """Section Three: Duplicate Mobile Number."""
    dup_mob_rows = df[df['mob'].duplicated(keep=False)]
    dup_mob_rows_sorted = dup_mob_rows.sort_values(by=['SB-district', 'SB-cfac_name', 'mob'])
    dup_mob_rows_filtered = dup_mob_rows_sorted[dup_mob_rows_sorted['mob'] != 7999999999]
    return dup_mob_rows_filtered


def find_q5_a5_error(df):
    """Section Four: Q5/A5 error."""
    hh_head_three = df[(df['A5'] == 0) & (df['HH_head'].astype(str).str.contains('3'))]
    a5_error = hh_head_three.sort_values(by=['SB-district', 'SB-cfac_name'])
    return a5_error


def find_q6_a6_error(df):
    """Section Five: Q6/A6 Error."""
    a6_error = df[((df['A6'] == 1) & (df['child_5Num'] < 4)) | ((df['A6'] == 0) & (df['child_5Num'] > 3))]
    a6_error_sorted = a6_error.sort_values(by=['SB-district', 'SB-cfac_name'])
    return a6_error_sorted


def find_child_under_5_error(df):
    """Section Six: Children Under 5 Error."""
    child_5_error = df[(df['child_5'] == 1) & (df['child_5Num'] == 0)]
    child_5_error_sorted = child_5_error.sort_values(by=['SB-district', 'SB-cfac_name'])
    return child_5_error_sorted


# def find_potential_hoh_duplicates(df):
#     """Section Seven: Potential Head of Household Duplication."""

#     def compare_rows(index_pair, df_block):
#         idx1, idx2 = index_pair
#         row1 = df_block.loc[idx1]
#         row2 = df_block.loc[idx2]

#         name_similarity = fuzz.partial_ratio(str(row1['name_ben']), str(row2['name_ben']))
#         father_similarity = fuzz.partial_ratio(str(row1['ben_fath']), str(row2['ben_fath']))
#         id_similarity = fuzz.partial_ratio(str(row1['id_number']), str(row2['id_number']))

#         if name_similarity >= 85 and father_similarity >= 85 and id_similarity >= 85:
#             return (idx1, idx2)
#         return None

#     df['block_key'] = df['name_ben'].astype(str).str[:2]
#     all_comparisons = []

#     for block_value, block_df in df.groupby('block_key'):
#         index_pairs = list(combinations(block_df.index, 2))

#         results = Parallel(n_jobs=-1)(
#             delayed(compare_rows)(pair, block_df) for pair in index_pairs
#         )

#         results = [result for result in results if result]
#         all_comparisons.extend(results)

#     if all_comparisons:
#         duplicate_indices = list(set([idx for pair in all_comparisons for idx in pair]))
#         duplicate_rows = df.loc[duplicate_indices]
#         return duplicate_rows
#     else:
#         return pd.DataFrame()  # Return empty DataFrame if no duplicates found

def find_potential_hoh_duplicates(df):
    """Section Seven: Potential Head of Household Duplication."""
    # Preprocess the data: clean and normalize strings
    df['name_ben_clean'] = df['name_ben'].astype(str).str.lower().str.strip()
    df['ben_fath_clean'] = df['ben_fath'].astype(str).str.lower().str.strip()
    df['id_number_clean'] = df['id_number'].astype(str).str.lower().str.strip()

    # Indexing: use blocking to reduce the number of comparisons
    indexer = recordlinkage.Index()
    indexer.block('name_ben_clean')
    candidate_pairs = indexer.index(df)

    # Comparison: define comparison criteria
    compare = recordlinkage.Compare()
    compare.string('name_ben_clean', 'name_ben_clean', method='jarowinkler', threshold=0.9, label='name_similarity')
    compare.string('ben_fath_clean', 'ben_fath_clean', method='jarowinkler', threshold=0.9, label='father_similarity')
    compare.string('id_number_clean', 'id_number_clean', method='jarowinkler', threshold=0.9, label='id_similarity')

    # Compute similarities
    features = compare.compute(candidate_pairs, df)

    # Identify potential duplicates where all similarities are above thresholds
    potential_duplicates = features[(features['name_similarity'] == 1) &
                                    (features['father_similarity'] == 1) &
                                    (features['id_similarity'] == 1)].index

    # Extract the duplicate rows
    duplicate_indices = list(set(potential_duplicates.get_level_values(0)).union(
                             set(potential_duplicates.get_level_values(1))))
    duplicate_rows = df.loc[duplicate_indices]

    return duplicate_rows



def add_error_remarks(df, error_type, remarks):
    """Section Eight: Adding Remarks."""
    df['error_type'] = error_type
    df['remarks'] = remarks
    return df


def merge_error_subsets(subsets):
    """Merge error subsets into a single DataFrame."""
    merged_errors = pd.DataFrame(columns=['index', 'error_type', 'remarks'])

    for subset in subsets:
        for idx, row in subset.iterrows():
            index_value = idx
            error_type = row['error_type']
            remark = row['remarks']

            if index_value in merged_errors['index'].values:
                merged_errors.loc[merged_errors['index'] == index_value, 'error_type'] += f", {error_type}"
                merged_errors.loc[merged_errors['index'] == index_value, 'remarks'] += f", {remark}"
            else:
                new_row = pd.DataFrame({
                    'index': [index_value],
                    'error_type': [error_type],
                    'remarks': [remark]
                })
                merged_errors = pd.concat([merged_errors, new_row], ignore_index=True)

    return merged_errors


def produce_final_excel(df, merged_errors):
    """Section Nine: Producing final Excel workbook."""
    error_indices = merged_errors['index'].tolist()

    df_with_errors = df.loc[error_indices]
    df_with_errors = df_with_errors.merge(
        merged_errors, left_index=True, right_on='index', how='left'
    )

    df_without_errors = df.drop(index=error_indices)

    return df_with_errors, df_without_errors
