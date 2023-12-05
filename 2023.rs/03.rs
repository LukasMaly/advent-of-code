use std::fs;

fn main() {
    let example = fs::read_to_string("examples/03.txt").unwrap();
    let input = fs::read_to_string("inputs/03.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 4361);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 467835);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 540025);
    assert_eq!(part_two, 84584891);
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

fn part_one(input: Vec<&str>) -> i32
{
    let height = input.len();
    let width = input[0].len();
    let mut chars: Vec<char> = Vec::with_capacity(height * width);
    for line in input {
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

fn part_two(input: Vec<&str>) -> i32
{
    let height = input.len();
    let width = input[0].len();
    let mut chars: Vec<char> = Vec::with_capacity(height * width);
    for line in input {
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
