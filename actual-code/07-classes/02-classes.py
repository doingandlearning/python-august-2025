user1= {
  "name": "Adam",
  "location": "Salford",
  "job": ["Data analysis", "apprentice"]
}

user2 = {
  "name": "Anya",
  "location": "Clapham",
  "job": ["JS", "Search team"]
}

def describe_user(user):
  return f"{user["name"]} lives in {user["location"]} and has a job that involves {", ".join(user["job"])}"

print(describe_user(user1))
print(describe_user(user2))

class User:  # __ dunder methods ... __init__, __str__, __repr__
  def __init__(self, name, location, job):
    self.name = name
    self.location = location
    self.job = job

  def __repr__(self):
    return f"User(name={self.name}, location={self.location}, job={self.job})"

  def describe(self):
    return f"{self.name} lives in {self.location} and has a job that involves {", ".join(self.job)}" 
    

user3 = User("Adam", "Salford", ["Data analysis", "apprentice"])  # instantiate a class
user4 = User("Anya", "Clapham", ["JS", "Search team"])

# Encapsulation
print(user3.describe())
print(user4.describe())

print([user1, user2, user3, user4])