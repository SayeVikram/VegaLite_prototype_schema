import json
import filecmp

class Encoding:

    type_ = "object"

    def __init__(self):
        self.encoding = {}

    def channel(self, string):
        if string not in ["x", "y", "color"]:
            raise KeyError("Name of channel not specified")
        self.current = string
        return self
        #setting a current field so that when we call field that current field is updated
    
    def field(self, fieldstr):
        self.encoding[self.current] = fieldstr
        return self
    
    def to_dict(self):
        return self.encoding
    #to_dict to receiving the encoding attribute
    
class visualization:
    def __init__(self):
        self._viz = {
            "type": "visualization",
            "mark": None,
            "encoding": {}
        }
        #default initializer

    def mark(self, stringchannel):
        if stringchannel not in ["bar", "line", "point", "area"]:
            raise KeyError("Name of channel not specified")
        self._viz["mark"] = stringchannel
        return self

    def add_encoding(self, encoding):
        self._viz["encoding"].update(encoding.to_dict())
        return self
        #updating the dictionary

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
        #appropriate setter for direction
        return self

    def gap(self, gap: str):
        self._layout["gap"] = gap
        #setter for gap
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
        .channel("y").field("-30")
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
            .channel("y").field("-30")
            .channel("color").field("red")
        )
    )
)
#creating the object according to the specifications


def same_file(file1, file2):
    with open(file1, "r") as f1:
        file1_contents = "".join(f1.read().split())
    with open(file2, "r") as f2:
        file2_contents = "".join(f2.read().split())
    
    return file1_contents == file2_contents
    #since the contents of the file are fairly small, i just converted them to strings and compared directly


def main():
    file_path_two = "python_generated_test_two.json"
    file_path_one = "python_gen_test.json"
    #Two unit tests that are generating the json files necessary for comparison

    with open(file_path_two, "w") as json_file:
        json.dump(example_two_test.to_dict(), json_file, indent=4)

    with open(file_path_one, "w") as json_file:
        json.dump(example_one_test.to_dict(), json_file, indent=4)
    
    assert same_file(file_path_one, 'example-json-1.json') #comparison checks
    assert same_file(file_path_two, 'example-json-2.json')



if __name__ == "__main__":
    main()
    print("Asserted both files are the same")

