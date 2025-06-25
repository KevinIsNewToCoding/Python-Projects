import pandas as pd


def load_data(csv_path: str) -> pd.DataFrame:
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(csv_path)


def department_salary_mean(df: pd.DataFrame) -> pd.Series:
    """Return the average salary per department."""
    return df.groupby('Department')['Salary'].mean()


def age_summary(df: pd.DataFrame) -> pd.Series:
    """Return descriptive statistics for the Age column."""
    return df['Age'].describe()


def main() -> None:
    df = load_data('sample_data.csv')
    print("Average salary by department:")
    print(department_salary_mean(df))
    print("\nAge statistics:")
    print(age_summary(df))


if __name__ == '__main__':
    main()
