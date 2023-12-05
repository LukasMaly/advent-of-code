use std::fs;

fn main() {
    let example_1 = fs::read_to_string("examples/01_1.txt").unwrap();
    let example_2 = fs::read_to_string("examples/01_2.txt").unwrap();
    let input = fs::read_to_string("inputs/01.txt").unwrap();

    assert_eq!(part_one(example_1.lines().collect()), 142);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example_2.lines().collect()), 281);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 54630);
    assert_eq!(part_two, 54770);
}

fn part_one(input: Vec<&str>) -> i32
{
    let mut nums: Vec<i32> = Vec::new();
    for line in input {
        let mut num = String::new();
        for c in line.chars() {
            if c.is_digit(10) {
                num.push(c);
            }
        }
        num = format!("{}{}", num.chars().nth(0).unwrap(), num.chars().last().unwrap());
        nums.push(num.parse().unwrap());
    }
    nums.iter().sum()
}

fn part_two(input: Vec<&str>) -> i32
{
    let mut nums: Vec<i32> = Vec::new();
    for line in input {
        let mut num = String::new();
        for i in 0..line.len() {
            if line.chars().nth(i).unwrap().is_digit(10) {
                num.push(line.chars().nth(i).unwrap());
            }
            else if line[i..line.len()].starts_with("one") {
                num.push('1')
            }
            else if line[i..line.len()].starts_with("two") {
                num.push('2')
            }
            else if line[i..line.len()].starts_with("three") {
                num.push('3')
            }
            else if line[i..line.len()].starts_with("four") {
                num.push('4')
            }
            else if line[i..line.len()].starts_with("five") {
                num.push('5')
            }
            else if line[i..line.len()].starts_with("six") {
                num.push('6')
            }
            else if line[i..line.len()].starts_with("seven") {
                num.push('7')
            }
            else if line[i..line.len()].starts_with("eight") {
                num.push('8')
            }
            else if line[i..line.len()].starts_with("nine") {
                num.push('9')
            }
        }
        num = format!("{}{}", num.chars().nth(0).unwrap(), num.chars().last().unwrap());
        nums.push(num.parse().unwrap());
    }
    nums.iter().sum()
}
