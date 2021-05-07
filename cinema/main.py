import sqlite3

## Create a Table
table_creation_string = """
CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
);
"""


def create_table(db_location, db_query):
    con = sqlite3.connect(db_location)
    con.execute(db_query)
    con.commit()
    con.close()


# create_table("cinema.db", table_creation_string)

## Add Some Records
## open the db connection
con = sqlite3.connect("cinema.db")

## write a single record to the open connection
def insert_record(seat_id, taken, price):
    con.execute(
        f"""
        INSERT INTO "Seat" ("seat_id", "taken", "price")
        VALUES ("{seat_id}", "{taken}", "{price}")
        """
    )
    con.commit()
    print(
        f"Record Inserted Successfully!:\nseat_id: {seat_id}\ttaken: {taken}\tprice: {price}"
    )


# make records
records = {"seat_id": ["A1", "A2", "A3"], "taken": [0, 1, 0], "price": [90, 100, 80]}

# push records to the database
for i in range(len(records)):
    insert_record(records["seat_id"][i], records["taken"][i], records["price"][i])

# close the connection
con.close()

# SELECT
def select_all():
    con = sqlite3.connect("cinema.db")
    # cursor is read only
    cursor = con.cursor()
    cursor.execute(
        """
        SELECT * FROM "Seat"
        """
    )
    result = cursor.fetchall()
    con.close()
    return result


def select_column(column_list):
    con = sqlite3.connect("cinema.db")
    # cursor is read only
    cursor = con.cursor()
    cursor.execute(
        f"""
        SELECT {', '.join(column_list)} FROM "Seat"
        """
    )
    result = cursor.fetchall()
    con.close()
    return result


def select_with_condition(column_list, conditions_str):
    con = sqlite3.connect("cinema.db")
    # cursor is read only
    cursor = con.cursor()
    cursor.execute(
        f"""
        SELECT {', '.join(column_list)} FROM "Seat"
        WHERE {conditions_str}
        """
    )
    result = cursor.fetchall()
    con.close()
    return result


print(select_column(["seat_id", "taken"]))

print(select_with_condition(["seat_id", "price"], '"price" > 80 AND "price" < 100'))

# update value
def update_value(id, value, new_value):
    con = sqlite3.connect("cinema.db")
    con.execute(
        f"""
        UPDATE "Seat" SET "{value}" = ? WHERE "seat_id" = ?
        """,
        [new_value, id],
    )
    con.commit()
    con.close()


update_value("A2", "taken", 0)

# delete record
def delete_record(id):
    con = sqlite3.connect("cinema.db")
    con.execute(
        f"""
        DELETE FROM "Seat" WHERE "seat_id" = "{id}"
        """
    )
    con.commit()
    con.close()


delete_record("A3")
