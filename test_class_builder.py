import pytest
import json
from class_builder import Encoding, visualization, layout


def same_file(file1, file2):

    with open(file1, "r") as f1:
        file1_contents = "".join(f1.read().split())
    with open(file2, "r") as f2:
        file2_contents = "".join(f2.read().split())
    
    return file1_contents == file2_contents


def test_example_one_visualization():

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
    
    # Generate the JSON file
    file_path_one = "python_gen_test.json"
    with open(file_path_one, "w") as json_file:
        json.dump(example_one_test.to_dict(), json_file, indent=4)
    
    # Compare with expected output
    assert same_file(file_path_one, 'example-json-1.json'), \
        "Generated JSON does not match expected example-json-1.json"


def test_example_two_layout():


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
    
    # Generate the JSON file
    file_path_two = "python_generated_test_two.json"
    with open(file_path_two, "w") as json_file:
        json.dump(example_two_test.to_dict(), json_file, indent=4)
    
    # Compare with expected output
    assert same_file(file_path_two, 'example-json-2.json'), \
        "Generated JSON does not match expected example-json-2.json"
