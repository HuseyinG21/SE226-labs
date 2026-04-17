import geometry_utils

def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    operation = input("Enter the operation you want to perform: ").strip()

    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    try:
        if operation not in operations:
            raise ValueError("Invalid operation selected.")

        func = operations[operation]

        if "circle" in operation:
            r = float(input("Enter radius: "))
            result = func(r)

        elif "rectangle" in operation:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = func(w, h)

        elif "triangle" in operation:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = func(b, h)

        print(f"Result: {round(result, 2)}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception:
        print("Unexpected error occurred.")

if __name__ == "__main__":
    main()