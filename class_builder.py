import json

class Encoding:

    type_ = "object"

    def __init__(self):
        self.encoding = {}

    def channel(self, string):
        if string not in ["x", "y", "color"]:
            raise KeyError("Name of channel not specified")
        self.current = string
        return self
    
    def field(self, fieldstr):
        self.encoding[self.current] = fieldstr
        return self
    
    def to_dict(self):
        return self.encoding
    
class visualization:
    def __init__(self):
        self._viz = {
            "type": "visualization",
            "mark": None,
            "encoding": {}
        }

    def mark(self, stringchannel):
        if stringchannel not in ["bar", "line", "point", "area"]:
            raise KeyError("Name of channel not specified")
        self._viz["mark"] = stringchannel
        return self

    def add_encoding(self, encoding):
        self._viz["encoding"].update(encoding.to_dict())
        return self

    def to_dict(self):
        return self._viz


class layout:
    def __init__(self):
        self._layout = {
            "type": "layout",
            "children": [],
            "direction": None,
            "gap": None
        }

    def direction(self, direction: str):
        self._layout["direction"] = direction
        return self

    def gap(self, gap: str):
        self._layout["gap"] = gap
        return self

    def add_child(self, node):
        self._layout["children"].append(node.to_dict())
        return self

    def to_dict(self):
        return self._layout


example_one_test = (
    visualization()
    .mark("bar")
    .add_encoding(
        Encoding()
        .channel("x").field("-25")
        .channel("y").field("30")
        .channel("color").field("red")
    )
)

example_two_test = (
    layout()
    .direction("vertical")
    .gap("20")
    .add_child(
        visualization()
        .mark("bar")
        .add_encoding(
            Encoding()
            .channel("x").field("-25")
            .channel("y").field("30")
            .channel("color").field("red")
        )
    )
)



def main():
    file_path = "python_generated_test_two.json"

    with open(file_path, "w") as json_file:
        json.dump(example_two_test.to_dict(), json_file, indent=4)



if __name__ == "__main__":
    main()

