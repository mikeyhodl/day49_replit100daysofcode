# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
while True:
  contents = f.readline().strip()
  
  print(contents)
```

<details> <summary> 👀 Answer </summary>

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)

```
</details>