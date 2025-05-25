
import pandas as pd
import os

# Define the path to the folder where the CSV file is located
folder_path = os.getcwd()

# Find the first CSV file in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

if len(csv_files) == 0:
    print("No CSV file found in the folder.")
else:
    # Assuming the first CSV file found is the one we want to use
    file_path = os.path.join(folder_path, csv_files[0])
    print(f"Dataset found: {csv_files[0]}")

    try:
        # Load the dataset
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        print(f"Dataset loaded successfully: {file_path}")
    except Exception as e:
        print(f"Failed to load the dataset: {e}")
        exit()

    print(f"Search filters: {list(df.columns)}")

    print("\nEnter your search criteria:")
    print("1. By Squad (Team)")
    print("2. By Country")
    print("3. By Top Team Scorer")
    print("4. By Goal Difference (GD)")
    print("5. Display all teams by a specific country and save them to a CSV file")
    print("6. Compare a team/footballer with others based on a specific area and print position")

    choice = input("\nChoose a search type (1/2/3/4/5/6): ").strip()

    results = pd.DataFrame()

    if choice == '1':
        print("Enter squad names (type 'done' to finish):")
        while True:
            squad = input("Enter squad name: ").strip()
            if squad.lower() == 'done':
                break
            squad_results = df[df['Squad'].str.contains(squad, case=False, na=False)]
            results = pd.concat([results, squad_results])
    elif choice == '2':
        print("Enter country names (type 'done' to finish):")
        while True:
            country = input("Enter country name: ").strip()
            if country.lower() == 'done':
                break
            country_results = df[df['Country'].str.contains(country, case=False, na=False)]
            results = pd.concat([results, country_results])
    elif choice == '3':
        print("Enter player names (type 'done' to finish):")
        while True:
            scorer = input("Enter player name: ").strip()
            if scorer.lower() == 'done':
                break
            scorer_results = df[df['Top Team Scorer'].str.contains(scorer, case=False, na=False)]
            results = pd.concat([results, scorer_results])
    elif choice == '4':
        try:
            min_gd = int(input("Enter the minimum Goal Difference (GD): ").strip())
            results = df[df['GD'] >= min_gd]
        except ValueError:
            print("Invalid input.")
            results = pd.DataFrame()
    elif choice == '5':
        country_name = input("Enter the country name: ").strip()
        country_teams = df[df['Country'].str.contains(country_name, case=False, na=False)]
        if not country_teams.empty:
            print("\nTeams from the specified country:")
            print(country_teams)
            output_file = os.path.join(folder_path, f'teams_in_{country_name}.csv')
            country_teams.to_csv(output_file, index=False)
            print(f"\nTeams from {country_name} saved to {output_file}")
        else:
            print(f"No teams found for the country: {country_name}")
    elif choice == '6':
        print("\nAvailable areas for comparison:")
        print(list(df.columns))
        compare_column = input("Enter the area you want to compare: ").strip()
        if compare_column in df.columns:
            name = input("Enter the name of the team or player: ").strip()
            compare_results = df.sort_values(by=compare_column, ascending=False)
            if not compare_results[compare_results['Squad'].str.contains(name, case=False, na=False)].empty:
                position = (
                    compare_results.reset_index()
                    .reset_index()
                    .loc[compare_results['Squad'].str.contains(name, case=False, na=False), 'level_0']
                    .values[0] + 1
                )
                print(f"\n{name} ranks {position} based on {compare_column}.")
            else:
                print(f"The name '{name}' does not exist in the dataset.")
        else:
            print("Invalid column name for comparison.")
    else:
        print("Invalid choice.")

    if not results.empty:
        print("\nSearch Results:")
        print(results)

        sort_choice = input("\nWould you like to sort the results? (yes/no): ").strip().lower()
        if sort_choice == 'yes':
            print("\nAvailable data for sorting:")
            print(list(results.columns))
            sort_column = input("Enter the data name to sort by: ").strip()
            if sort_column in results.columns:
                sorted_results = results.sort_values(by=sort_column, ascending=False)
                print("\nSorted Results (High to Low):")
                print(sorted_results)
                output_file = os.path.join(folder_path, 'sorted_results.csv')
                sorted_results.to_csv(output_file, index=False)
                print(f"\nSorted results saved to {output_file}")
            else:
                print("Invalid column name for sorting.")
        else:
            print("\nResults not sorted.")

        comparison_file = os.path.join(folder_path, 'comparison_results.csv')
        results.to_csv(comparison_file, index=False)
        print(f"\nComparison results saved to {comparison_file}")
    else:
        print("No matches found for your query.")
