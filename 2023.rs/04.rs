use std::fs;

fn main() {
    let example = fs::read_to_string("examples/04.txt").unwrap();
    let input = fs::read_to_string("inputs/04.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 13);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 30);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 18653);
    assert_eq!(part_two, 5921508);
}

fn part_one(input: Vec<&str>) -> i32
{
    let mut sum = 0;
    for line in input {
        let numbers: Vec<&str> = line.split(':').collect::<Vec<&str>>()[1].split('|').collect();
        let winning_numbers: Vec<&str> = numbers[0].split_whitespace().collect();
        let winning_numbers: Vec<i32> = winning_numbers.iter().map(|x| x.parse().unwrap()).collect();
        let my_numbers: Vec<&str> = numbers[1].split_whitespace().collect::<Vec<&str>>();
        let my_numbers: Vec<i32> = my_numbers.iter().map(|x| x.parse().unwrap()).collect();
        let mut matches = 0;
        for my_number in &my_numbers {
            for winning_number in &winning_numbers {
                if my_number == winning_number {
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

fn part_two(input: Vec<&str>) -> i32
{
    let mut match_counts = vec![0; input.len()];
    for (l, line) in input.iter().enumerate() {
        let numbers: Vec<&str> = line.split(':').collect::<Vec<&str>>()[1].split('|').collect();
        let winning_numbers: Vec<&str> = numbers[0].split_whitespace().collect();
        let winning_numbers: Vec<i32> = winning_numbers.iter().map(|x| x.parse().unwrap()).collect();
        let my_numbers: Vec<&str> = numbers[1].split_whitespace().collect::<Vec<&str>>();
        let my_numbers: Vec<i32> = my_numbers.iter().map(|x| x.parse().unwrap()).collect();
        for my_number in &my_numbers {
            for winning_number in &winning_numbers {
                if my_number == winning_number {
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
