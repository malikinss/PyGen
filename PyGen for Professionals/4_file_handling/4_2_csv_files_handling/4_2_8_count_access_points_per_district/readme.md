# Wi-Fi Access Points in Moscow Districts

## Description 📝

This program reads a `CSV` file containing data about Wi-Fi access points in various districts of Moscow.
It calculates the total number of access points in each district and outputs the results in descending order of access point count.
If two districts have the same number of access points, they are sorted lexicographically by their names.

## Purpose 🎯

The purpose of this program is to:

-   Read a `CSV` file containing Wi-Fi access point data for Moscow districts.
-   Calculate the total number of access points in each district.
-   Print the districts along with their corresponding number of access points.
-   Sort the districts by the number of access points in descending order, and lexicographically when the counts are equal.

## How It Works 🔍

1. The function `read_csv()` reads the original `CSV` file containing district Wi-Fi data. Each row includes information about the district, area, address, and the number of access points at that address.
2. The function `count_access_points_per_district()` processes the data to count the total number of access points for each district.
3. The function `print_access_points_per_district()` sorts the districts by access point count (in descending order), and lexicographically in case of a tie, and then prints the result.

## Output 📜

The program outputs the districts and their corresponding number of access points in the following format:

```
District Name: Number of Access Points
...
```

The districts are listed in descending order of the total number of access points. If two or more districts have the same count, they are sorted alphabetically by district name.

## Usage 📦

1. Ensure you have a `wifi.csv` file with the format:

    ```
    adm_area;district;location;number_of_access_points
    Central Administrative District;Yakimanka District;Moscow, Serafimovich Street, Building 5/16;5
    Central Administrative District;Yakimanka District;Moscow, Bolotnaya Embankment, Building 11, Building 1;2
    ...
    ```

2. Run the program. It will:
    - Read the `wifi.csv` file.
    - Calculate the number of access points per district.
    - Output the results in the specified format.

### Example:

If the `wifi.csv` file contains the following data:

```
adm_area;district;location;number_of_access_points
Central Administrative District;Yakimanka District;Moscow, Serafimovich Street, Building 5/16;5
Central Administrative District;Yakimanka District;Moscow, Bolotnaya Embankment, Building 11, Building 1;2
Southern Administrative District;Biryulyovo Zapadnoye;Moscow, Biryulyovo East, Building 14;4
Southern Administrative District;Biryulyovo Zapadnoye;Moscow, Biryulyovo East, Building 20;2
```

The output will be:

```
Central Administrative District: 7
Southern Administrative District: 6
```

## Conclusion 🚀

This program allows for easy and efficient analysis of Wi-Fi access point distribution across Moscow's districts.
It provides clear, sorted results, making it useful for urban planning or any related research.
