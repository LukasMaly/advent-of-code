use std::fs;

fn main() {
    let example = fs::read_to_string("examples/02.txt").unwrap();
    let input = fs::read_to_string("inputs/02.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 8);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 2286);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 2447);
    assert_eq!(part_two, 56322);
}

fn part_one(input: Vec<&str>) -> i32
{
    let mut sum: i32 = 0;
    for line in input {
        let record: Vec<&str> = line.split(':').collect();
        let mut id: i32 = record[0].split(' ').collect::<Vec<&str>>()[1].parse().unwrap();
        let subsets: Vec<&str> = record[1].split(';').collect();
        for subset in subsets {
            let sets: Vec<&str> = subset.split(',').collect();
            for set in sets {
                let set: Vec<&str> = set.trim().split(' ').collect();
                let count: i32 = set[0].parse().unwrap();
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

fn part_two(input: Vec<&str>) -> i32
{
    let mut sum = 0;
    for line in input {
        let record: Vec<&str> = line.split(':').collect();
        let subsets: Vec<&str> = record[1].split(';').collect();
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for subset in subsets {
            let sets: Vec<&str> = subset.split(',').collect();
            for set in sets {
                let set: Vec<&str> = set.trim().split(' ').collect();
                let count: i32 = set[0].parse().unwrap();
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
