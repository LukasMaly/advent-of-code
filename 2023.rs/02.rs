use std::fs;

fn main() {
    let answer = part_one("examples/02.txt");
    assert!(answer == 8);
    let answer = part_one("inputs/02.txt");
    println!("{}", answer);
    let answer = part_two("examples/02.txt");
    assert!(answer == 2286);
    let answer = part_two("inputs/02.txt");
    println!("{}", answer);
}

fn part_one(path: &str) -> u32
{
    let contents = fs::read_to_string(path).unwrap();
    let mut sum = 0;
    for line in contents.lines() {
        let record: Vec<&str> = line.split(':').collect();
        let mut id: u32 = record[0].split(' ').collect::<Vec<&str>>()[1].parse().unwrap();
        let subsets: Vec<&str> = record[1].split(';').collect();
        for subset in subsets {
            let sets: Vec<&str> = subset.split(',').collect();
            for set in sets {
                let set: Vec<&str> = set.trim().split(' ').collect();
                let count: u32 = set[0].parse().unwrap();
                let color: &str = set[1];
                if (color == "red" && count > 12) || (color == "green" && count > 13) || (color == "blue" && count > 14) {
                    id = 0;
                }
            }
        }
        sum += id;
    }
    sum
}

fn part_two(path: &str) -> u32
{
    let contents = fs::read_to_string(path).unwrap();
    let mut sum = 0;
    for line in contents.lines() {
        let record: Vec<&str> = line.split(':').collect();
        let subsets: Vec<&str> = record[1].split(';').collect();
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for subset in subsets {
            let sets: Vec<&str> = subset.split(',').collect();
            for set in sets {
                let set: Vec<&str> = set.trim().split(' ').collect();
                let count: u32 = set[0].parse().unwrap();
                let color: &str = set[1];
                if color == "red" {
                    if count > red {
                        red = count;
                    }
                } else if color == "green" {
                    if count > green {
                        green = count;
                    }
                } else if color == "blue" {
                    if count > blue {
                        blue = count;
                    }
                }
            }
        }
        let power = red * green * blue;
        sum += power;
    }
    sum
}
