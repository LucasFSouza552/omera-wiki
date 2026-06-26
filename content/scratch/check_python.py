import os
print("Current Working Directory:", os.getcwd())
try:
    with open("test_write.txt", "w") as f:
        f.write("test")
    print("Write test successful!")
    os.remove("test_write.txt")
except Exception as e:
    print("Write test failed:", e)
