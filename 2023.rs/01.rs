use std::fs;

fn main() {
    part_one("examples/01_1.txt");
    part_one("inputs/01.txt");
    part_two("examples/01_2.txt");
    part_two("inputs/01.txt");
}

fn part_one(path: &str)
{
    let contents = fs::read_to_string(path)
        .expect("Something went wrong reading the file");

    let mut nums: Vec<i32> = Vec::new();

    for line in contents.lines() {
        let mut num = String::new();
        for c in line.chars() {
            if c.is_digit(10) {
                num.push(c);
            }
        }
        num = format!("{}{}", num.chars().nth(0).unwrap(), num.chars().last().unwrap());
        nums.push(num.parse().unwrap());
    }

    let sum: i32 = nums.iter().sum();

    println!("{}", sum);
}

fn part_two(path: &str)
{
    let contents = fs::read_to_string(path)
        .expect("Something went wrong reading the file");

    let mut nums: Vec<i32> = Vec::new();

    for line in contents.lines() {
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

    let sum: i32 = nums.iter().sum();
    
    println!("{}", sum);
}