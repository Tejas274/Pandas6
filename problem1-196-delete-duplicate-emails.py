import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

    min_ids = person.groupby("email")["id"].transform('min')
    ids_to_delete = person[person['id'] != min_ids]
    person.drop(ids_to_delete.index,inplace=True)