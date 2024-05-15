import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = person.merge(
        address,
        left_on = 'personId',
        right_on = 'personId',
        how = 'left'
    )
    return df[['firstName', 'lastName', 'city', 'state']]