This is a great case study for working with JSON and CSV conversions. Here’s an **extension lab** based on it, adding **error handling, data validation, and a dictionary-based JSON output**.

---

# **Lab Extension: Advanced JSON & CSV Processing**

## **Objective**
This extension builds on the **Case Study: Converting JSON Data to CSV**, introducing:
1. **Data Validation**: Ensure all user entries have required fields.
2. **Error Handling**: Handle missing fields, invalid data, and duplicates.
3. **Filtering Data**: Remove users under 30 before writing the CSV.
4. **Transforming Data**: Convert the CSV back to JSON as a **dictionary** (`email` as the key).
5. **Logging Actions**: Log each operation for debugging.

---

## **📌 Step 5: Data Validation**
Ensure that **each user has all required fields** (`id`, `name`, `email`, `age`, `city`) before writing to JSON or CSV.

### **Tasks**
1. Implement a **`validate_user()`** function to check:
   - `id` is an integer.
   - `name` and `email` are non-empty strings.
   - `age` is a positive integer.
   - `city` is a non-empty string.
2. **Skip invalid records** and log errors instead of crashing.

💡 **Hints**
- Use `isinstance(value, int)` to check numbers.
- Use `str.strip()` to ensure names/emails/cities are non-empty.

---

## **📌 Step 6: Prevent Duplicate Users**
When adding a new user:
1. **Check for duplicate emails** before appending.
2. If the email already exists, **skip adding** and log a warning.

💡 **Hints**
- Store emails in a **set** (`existing_emails = {user["email"] for user in users}`).
- Use `if email in existing_emails:` to check duplicates.

---

## **📌 Step 7: Filter Users Before Writing CSV**
Modify the **CSV export** step to **exclude users under 30**.

### **Tasks**
1. Before writing to `users.csv`, remove users with `age < 30`.
2. Log how many users were removed.

💡 **Hints**
- Use `filtered_users = [user for user in users if user["age"] >= 30]`.

---

## **📌 Step 8: Convert CSV to JSON as a Dictionary**
Instead of saving the **CSV back to JSON as a list**, convert it into a **dictionary** with **`email` as the key**.

### **Tasks**
1. Read the CSV file and convert it into a **dictionary** like:
   ```json
   {
     "alice@example.com": { "name": "Alice", "age": 25, "city": "London" },
     "bob@example.com": { "name": "Bob", "age": 32, "city": "New York" }
   }
   ```
2. Save this **dictionary JSON** into `users_by_email.json`.

💡 **Hints**
- Use `json.dump(data, file, indent=4)` for formatting.

---

# **🚀 Solutions (Spoilers)**

<details>
<summary>Click to reveal solutions</summary>

### **Step 5: Data Validation**
```python
import json
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

def validate_user(user):
    """Validate that user has all required fields with correct types."""
    required_fields = ["id", "name", "email", "age", "city"]

    for field in required_fields:
        if field not in user:
            logging.warning(f"Skipping user - missing field: {field}")
            return False

    if not isinstance(user["id"], int) or user["id"] <= 0:
        return False
    if not isinstance(user["name"], str) or not user["name"].strip():
        return False
    if not isinstance(user["email"], str) or "@" not in user["email"]:
        return False
    if not isinstance(user["age"], int) or user["age"] < 0:
        return False
    if not isinstance(user["city"], str) or not user["city"].strip():
        return False

    return True

# Load JSON data
with open("users.json", "r") as file:
    users = json.load(file)

# Filter only valid users
valid_users = [user for user in users if validate_user(user)]

# Save back to JSON
with open("validated_users.json", "w") as file:
    json.dump(valid_users, file, indent=4)

logging.info(f"Validation complete. {len(valid_users)} valid users saved.")
```

---

### **Step 6: Prevent Duplicates**
```python
# Load JSON data
with open("users.json", "r") as file:
    users = json.load(file)

existing_emails = {user["email"] for user in users}

new_user = {"id": 5, "name": "David", "email": "david@example.com", "age": 40, "city": "Berlin"}

if new_user["email"] in existing_emails:
    logging.warning(f"User with email {new_user['email']} already exists. Skipping.")
else:
    users.append(new_user)
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
    logging.info("New user added successfully.")
```

---

### **Step 7: Filter Users Before Writing CSV**
```python
import csv

csv_filename = "users.csv"

# Remove users under 30
filtered_users = [user for user in users if user["age"] >= 30]

with open(csv_filename, "w", newline="") as file:
    fieldnames = ["name", "email", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for user in filtered_users:
        writer.writerow({
            "name": user["name"],
            "email": user["email"],
            "age": user["age"],
            "city": user["city"]
        })

logging.info(f"Filtered users written to {csv_filename}. {len(filtered_users)} users included.")
```

---

### **Step 8: Convert CSV to JSON as a Dictionary**
```python
csv_to_json = {}

with open(csv_filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row["email"]
        csv_to_json[email] = {
            "name": row["name"],
            "age": int(row["age"]),
            "city": row["city"]
        }

# Save dictionary JSON
with open("users_by_email.json", "w") as file:
    json.dump(csv_to_json, file, indent=4)

logging.info("CSV data successfully converted back to JSON with email as key.")
```

</details>

---

## **✅ Summary of Enhancements**
| **Feature** | **What It Improves** |
|-------------|----------------------|
| **Data Validation** | Prevents missing/incomplete users from being added. |
| **Duplicate Prevention** | Avoids duplicate users in `users.json`. |
| **Filtering Before CSV Export** | Excludes users **under 30** for targeted analysis. |
| **CSV to JSON (Dictionary Format)** | Makes JSON structured by **email key** for easier lookups. |
| **Logging** | Tracks actions & prevents silent failures. |

---

## **🚀 Next Steps**
🔹 Add a **CLI** to allow users to select tasks (validate, convert, append, etc.).  
🔹 Implement **unit tests** to check validation logic.  
🔹 Support **command-line arguments** to specify input/output filenames dynamically.  
