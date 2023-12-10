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

fn get_neighbors() -> Vec<(i32, i32)>
{
    let mut neighbors: Vec<(i32, i32)> = Vec::new();
    for y in -1..=1 {
        for x in -1..=1 {
            if x != 0 || y != 0 {
                neighbors.push((x, y));
            }
        }
    }
    neighbors
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
                for neighbor in get_neighbors() {
                    if y as i32 + neighbor.1 >= 0 && y as i32 + neighbor.1 < height as i32 && x as i32 + neighbor.0 >= 0 && x as i32 + neighbor.0 < width as i32 {
                        if chars[((y as i32 + neighbor.1) * width as i32 + (x as i32 + neighbor.0)) as usize].is_digit(10) {
                            sum += search_number(&mut chars, width, (x as i32 + neighbor.0) as usize, (y as i32 + neighbor.1) as usize);
                        }
                    }
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
                for neighbor in get_neighbors() {
                    if y as i32 + neighbor.1 >= 0 && y as i32 + neighbor.1 < height as i32 && x as i32 + neighbor.0 >= 0 && x as i32 + neighbor.0 < width as i32 {
                        if chars[((y as i32 + neighbor.1) * width as i32 + (x as i32 + neighbor.0)) as usize].is_digit(10) {
                            gear_ratio *= search_number(&mut chars, width, (x as i32 + neighbor.0) as usize, (y as i32 + neighbor.1) as usize);
                            part_numbers += 1;
                        }
                    }
                }
                if part_numbers == 2 {
                    sum += gear_ratio;
                }
            }
        }
    }
    sum
}
