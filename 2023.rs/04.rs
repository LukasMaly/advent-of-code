use std::fs;

fn main() {
    assert_eq!(part_one("examples/04.txt"), 13);
    println!("{}", part_one("inputs/04.txt"));
    assert_eq!(part_two("examples/04.txt"), 30);
    println!("{}", part_two("inputs/04.txt"));
}

fn part_one(path: &str) -> i32
{
    let contents = fs::read_to_string(path).unwrap();
    let mut sum = 0;
    for line in contents.lines() {
        let numbers = line.split(':').collect::<Vec<&str>>()[1].split('|').collect::<Vec<&str>>();
        let winning_numbers = numbers[0].split_whitespace().collect::<Vec<&str>>();
        let winning_numbers: Vec<i32> = winning_numbers.iter().map(|x| x.parse::<i32>().unwrap()).collect();
        let my_numbers = numbers[1].split_whitespace().collect::<Vec<&str>>();
        let my_numbers: Vec<i32> = my_numbers.iter().map(|x| x.parse::<i32>().unwrap()).collect();
        let mut matches = 0;
        for my_number in my_numbers {
            for winning_number in &winning_numbers {
                if my_number == *winning_number {
                    matches += 1;
                }
            }
        }
        if matches > 0 {
            sum += i32::pow(2, matches - 1);
        }
    }
    sum
}

fn part_two(path: &str) -> i32
{
    let contents = fs::read_to_string(path).unwrap();
    let mut match_counts = vec![0; contents.lines().count()];
    for (l, line ) in contents.lines().enumerate() {
        let numbers = line.split(':').collect::<Vec<&str>>()[1].split('|').collect::<Vec<&str>>();
        let winning_numbers = numbers[0].split_whitespace().collect::<Vec<&str>>();
        let winning_numbers: Vec<i32> = winning_numbers.iter().map(|x| x.parse::<i32>().unwrap()).collect();
        let my_numbers = numbers[1].split_whitespace().collect::<Vec<&str>>();
        let my_numbers: Vec<i32> = my_numbers.iter().map(|x| x.parse::<i32>().unwrap()).collect();
        for my_number in my_numbers {
            for winning_number in &winning_numbers {
                if my_number == *winning_number {
                    match_counts[l] += 1;
                }
            }
        }
    }
    let mut card_counts = vec![1; match_counts.len()];
    for (m, match_count) in match_counts.iter().enumerate() {
        let num_copies = card_counts[m];
        card_counts[(m + 1)..(m + match_count + 1)].iter_mut().for_each(|x| *x += num_copies);
    }
    card_counts.iter().sum()
}
