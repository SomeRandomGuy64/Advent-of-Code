use std::fs;

fn main() {
    let filepath = "../input.txt";

    let contents = fs::read_to_string(filepath)
        .expect("Should have been able to read the file");

    let values: Vec<&str> = contents.lines().collect();

    let mut total = 0;

    let digits: [(i32, &str); 9] = [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"), (8, "eight"), (9, "nine")];

    for value in values {
        let first = false;
        let mut first_number = 0;
        let mut last_number = 0;
        let word_digit = String::new();

        check_for_numbers(value, word_digit, digits, first, &mut first_number, &mut last_number);
        let total_value = first_number + last_number;
        total += total_value;
    }

    println!("{total}");
}

fn check_for_numbers(value: &str, mut word_digit: String, digits: [(i32, &str); 9], mut first: bool, first_number: &mut i32, last_number: &mut i32) {
    for character in value.chars() {
        if !character.is_numeric() {
            word_digit.push_str(character.to_string().as_str());

            check_word_number(&mut word_digit, digits, &mut first, first_number, last_number);

        } else {
            if first == false {
                first = true;
                word_digit.clear();
                *first_number = (character.to_digit(10).unwrap_or(0) as i32) * 10;
            }
            *last_number = character.to_digit(10).unwrap_or(0) as i32;
        }
    }
}

fn check_word_number(word_digit: &mut String, digits: [(i32, &str); 9], first: &mut bool, first_number: &mut i32, last_number: &mut i32) {
    let digit_tuple = string_contains_any(word_digit.clone(), &digits);
        
    if digit_tuple.0 {
        let last_character = word_digit.chars().last().unwrap().to_string();
        word_digit.clear();
        word_digit.push_str(last_character.as_str());

        if *first == false {
            *first = true;
            *first_number = digit_tuple.1 * 10;
        } else {
            *last_number = digit_tuple.1;
        }
    }
}

fn string_contains_any(word_digit: String, digits: &[(i32, &str)]) -> (bool, i32) {
    for (num, word) in digits.iter() {
        if word_digit.contains(*word) {
            return (true, *num);
        }
    }
    (false, 0)
}