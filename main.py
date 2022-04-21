def main():
    import pandas as pd
    file_path = 'C:/Users/palme/Desktop/Spring 2022/energy_use_terrawatthours.csv'
    energy_use = pd.read_csv(file_path)
    print(energy_use)
    year = energy_use.loc[:, 'year']
    power_source = energy_use.loc[:, "variable"]
    generated = energy_use.loc[:, "generation_twh"]
    for x in range(len(year)):
        if year[x] == 2000:
            print("Energy from", power_source[x], "accounts for", generated[x], "twh of world power generation in the "
                                                                                "year", year[x])

    print("\n\n\n")
    for x in range(len(year)):
        if (year[x] >= 200) and (year[x] <= 2021) and (power_source[x] == "Clean"):
            print("Energy from", power_source[x], "accounts for", generated[x], "twh of world power generation in the "
                                                                                "year", year[x])

    print("\n\n\n")
    for x in range(len(year)):
        if (year[x] >= 200) and (year[x] <= 2021) and (power_source[x] == "Fossil"):
            print("Energy from", power_source[x], "accounts for", generated[x], "twh of world power generation in the "
                                                                                "year", year[x])


if __name__ == "__main__":
    main()
