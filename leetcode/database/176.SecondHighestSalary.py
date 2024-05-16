import pandas as pd

# Write a solution to find the second highest salary from the Employee table. 
# If there is no second highest salary, return null (return None in Pandas).

# passes the run but not submit
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee) < 2:
        return pd.DataFrame([{'SecondHighestSalary':None}])
    else:
        return pd.DataFrame(
            employee['salary'].sort_values().tail(2).head(1)
            ).rename(
                columns={'salary':'SecondHighestSalary'}
                )


# correct one, submitted, accepted
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee['salary'].drop_duplicates()) < 2:
        return pd.DataFrame([{'SecondHighestSalary':None}])
    else:
        return pd.DataFrame(
            employee['salary'].drop_duplicates().sort_values().tail(2).head(1)
            ).rename(
                columns={'salary':'SecondHighestSalary'}
                )