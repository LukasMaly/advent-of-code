use std::fs;

fn main() {
    assert_eq!(part_one("examples/03.txt"), 4361);
    println!("{}", part_one("inputs/03.txt"));
    assert_eq!(part_two("examples/03.txt"), 467835);
    println!("{}", part_two("inputs/03.txt"));
}

fn search_number(chars: &mut Vec<char>, width: usize, x: usize, y: usize) -> i32
{
    let mut start = x;
    while start > 0 && chars[y * width + start - 1].is_digit(10) {
        start -= 1;
    }
    let mut end = x + 1;
    while end < width && chars[y * width + end].is_digit(10) {
        end += 1;
    }
    let number: i32 = chars[(y * width + start)..(y * width + end)].iter().collect::<String>().parse().unwrap();
    chars[(y * width + start)..(y * width + end)].fill('.');
    number
}

fn part_one(path: &str) -> i32
{
    let contents = fs::read_to_string(path).unwrap();
    let height = contents.lines().count();
    let width = contents.lines().nth(0).unwrap().len();
    let mut chars: Vec<char> = Vec::with_capacity(height * width);
    for line in contents.lines() {
        for char in line.chars() {
            chars.push(char);
        }
    }
    let mut sum = 0;
    for y in 0..height {
        for x in 0..width {
            if chars[y * width + x] != '.' && !chars[y * width + x].is_digit(10) {
                if y > 0 && x > 0 && chars[(y - 1) * width + (x - 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x - 1, y - 1);
                }
                if y > 0 && chars[(y - 1) * width + x].is_digit(10) {
                    sum += search_number(&mut chars, width, x, y - 1);
                }
                if y > 0 && x < width - 1 && chars[(y - 1) * width + (x + 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x + 1, y - 1);
                }
                if x > 0 && chars[y * width + (x - 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x - 1, y);
                }
                if x < width - 1 && chars[y * width + (x + 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x + 1, y);
                }
                if y < height - 1 && x > 0 && chars[(y + 1) * width + (x - 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x - 1, y + 1);
                }
                if y < height - 1 && chars[(y + 1) * width + x].is_digit(10) {
                    sum += search_number(&mut chars, width, x, y + 1);
                }
                if y < height - 1 && x < width - 1 && chars[(y + 1) * width + (x + 1)].is_digit(10) {
                    sum += search_number(&mut chars, width, x + 1, y + 1);
                }
            }
        }
    }
    sum
}

fn part_two(path: &str) -> i32
{
    let contents = fs::read_to_string(path).unwrap();
    let height = contents.lines().count();
    let width = contents.lines().nth(0).unwrap().len();
    let mut chars: Vec<char> = Vec::with_capacity(height * width);
    for line in contents.lines() {
        for char in line.chars() {
            chars.push(char);
        }
    }
    let mut sum = 0;
    for y in 0..height {
        for x in 0..width {
            if chars[y * width + x] == '*' {
                let mut gear_ratio = 1;
                let mut part_numbers = 0;
                if y > 0 && x > 0 && chars[(y - 1) * width + (x - 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x - 1, y - 1);
                    part_numbers += 1;
                }
                if y > 0 && chars[(y - 1) * width + x].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x, y - 1);
                    part_numbers += 1;
                }
                if y > 0 && x < width - 1 && chars[(y - 1) * width + (x + 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x + 1, y - 1);
                    part_numbers += 1;
                }
                if x > 0 && chars[y * width + (x - 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x - 1, y);
                    part_numbers += 1;
                }
                if x < width - 1 && chars[y * width + (x + 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x + 1, y);
                    part_numbers += 1;
                }
                if y < height - 1 && x > 0 && chars[(y + 1) * width + (x - 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x - 1, y + 1);
                    part_numbers += 1;
                }
                if y < height - 1 && chars[(y + 1) * width + x].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x, y + 1);
                    part_numbers += 1;
                }
                if y < height - 1 && x < width - 1 && chars[(y + 1) * width + (x + 1)].is_digit(10) {
                    gear_ratio *= search_number(&mut chars, width, x + 1, y + 1);
                    part_numbers += 1;
                }
                if part_numbers == 2 {
                    sum += gear_ratio;
                }
            }
        }
    }
    sum
}
