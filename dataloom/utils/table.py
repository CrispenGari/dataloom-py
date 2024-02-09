def print_pretty_table(headers: list[str], data: list[list]) -> None:
    # Calculate the maximum width for each column
    num_columns = len(data[0])
    column_widths = [max(len(str(row[i])) for row in data) for i in range(num_columns)]

    # Adjust column widths if headers are longer
    for i, header in enumerate(headers):
        column_widths[i] = max(column_widths[i], len(header))

    # Print the headers
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()
    for i, header in enumerate(headers):
        print(f"| {header:<{column_widths[i]}} ", end="")
    print("|")

    # Print the separator
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()

    # Print the data rows
    for row in data:
        for i, cell in enumerate(row):
            print(f"| {str(cell):<{column_widths[i]}} ", end="")
        print("|")

    # Print the bottom line
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()
