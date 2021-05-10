def busiest(data):
    num_people = 0
    max_people = 0
    start = 0
    end = 0
    for entry in data:
        if entry["type"] == "enter":
            num_people += entry["count"]
            if num_people > max_people:
                max_people = num_people
                start = entry["timestamp"]
                end = -1
        else:
            num_people -= entry["count"]
            if end == -1:
                end = entry["timestamp"]
    print(start, end)
    return (start, end)

stamp = [
  {"timestamp": 1526579928, "count": 3, "type": "enter"},
  {"timestamp": 1526580382, "count": 2, "type": "exit"},
  {"timestamp": 1526579938, "count": 6, "type": "enter"},
  {"timestamp": 1526579943, "count": 1, "type": "enter"},
  {"timestamp": 1526579944, "count": 0, "type": "enter"},
  {"timestamp": 1526580345, "count": 5, "type": "exit"},
  {"timestamp": 1526580351, "count": 3, "type": "exit"},
]

busiest(stamp)