use std::fs;

fn main() {
    let filepath = "../input.txt";

    let contents = fs::read_to_string(filepath)
        .expect("Should have been able to read the file");

    let values: Vec<&str> = contents.lines().collect();

    let mut total = 0;

    let digits: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    for value in values {
        let mut first = false;
        let mut first_number = 0;
        let mut last_number = 0;

        for character in value.chars() {
            if character.is_numeric() {
                if first == false {
                    first = true;
                    first_number = (character.to_digit(10).unwrap_or(0) as i32) * 10;
                }
                last_number = character.to_digit(10).unwrap_or(0) as i32;
            }
        }
        let total_value = first_number + last_number;
        total += total_value;
    }

    println!("{total}");
}
