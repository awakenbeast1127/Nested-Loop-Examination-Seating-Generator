# Case Study 26: Nested Loop Examination Seating Generator

def generate_seating(students, rows, columns, reserved_seats):
    classroom = []
    student_index = 0

    for row in range(1, rows + 1):
        seat_row = []
        for column in range(1, columns + 1):
            position = (row, column)
            if position in reserved_seats:
                seat_row.append("RES")
            elif (row + column) % 2 == 0 and student_index < len(students):
                seat_row.append(students[student_index])
                student_index += 1
            else:
                seat_row.append("--")
        classroom.append(seat_row)

    unallocated = students[student_index:]
    return classroom, unallocated


def main():
    students = ["A101", "A102", "A103", "A104", "A105", "A106",
                "A107", "A108", "A109", "A110"]
    reserved = [(2, 3)]
    seating, unallocated = generate_seating(students, 4, 5, reserved)

    print("EXAMINATION SEATING PLAN")
    print("RES = Reserved | -- = Unavailable")
    print("       C1     C2     C3     C4     C5")
    for row_number, row in enumerate(seating, start=1):
        print(f"Row {row_number}: " + "  ".join(f"{seat:>5}" for seat in row))
    print(f"Unallocated students: {unallocated if unallocated else 'None'}")


if __name__ == "__main__":
    main()
