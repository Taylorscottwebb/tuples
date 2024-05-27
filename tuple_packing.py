# 2. Python Data Structure Challenges in Real-World Scenarios
# Objective:
# This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.


library_collection = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def library_management(library):
    for books, title in library_collection:
        if library[0] == books:
            print("We already have that book!")
            return library_collection
        
    library_collection.append(library)
    return library_collection
    
print(library_management(("Eragon", "Christopher Paolini")))
print(library_management(("City of bones","Cassandra Clare")))
print(library_management(("Eragon", "Christopher Paolini")))