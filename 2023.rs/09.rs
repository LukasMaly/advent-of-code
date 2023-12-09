use std::fs;

fn main() {
    let example = fs::read_to_string("examples/09.txt").unwrap();
    let input = fs::read_to_string("inputs/09.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 114);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 2);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 1681758908);
    assert_eq!(part_two, 803);
}

fn parse_input(input: Vec<&str>) -> Vec<Vec<i32>> {
    let mut histories: Vec<Vec<i32>> = Vec::new();
    for line in input {
        let numbers: Vec<&str> = line.split_whitespace().collect();
        let numbers: Vec<i32> = numbers.iter().map(|x| x.parse().unwrap()).collect();
        histories.push(numbers);
    }
    histories
}

fn part_one(input: Vec<&str>) -> i32 {
    let histories = parse_input(input);
    let mut next_values_sum = 0;
    for history in histories {
        let mut last_values: Vec<i32> = Vec::new();
        last_values.push(*history.last().unwrap());
        let mut differences= history.iter().zip(history.iter().skip(1)).map(|(x, y)| y - x).collect::<Vec<i32>>();
        last_values.push(*differences.last().unwrap());
        while !(differences.iter().sum::<i32>() == 0 && (differences.iter().min() == differences.iter().max())) {
            differences = differences.iter().zip(differences.iter().skip(1)).map(|(x, y)| y - x).collect::<Vec<i32>>();
            last_values.push(*differences.last().unwrap());
        }
        next_values_sum += last_values.iter().sum::<i32>();
    }
    next_values_sum
}

fn part_two(input: Vec<&str>) -> i32 {
    let histories: Vec<Vec<i32>> = parse_input(input);
    let mut previous_values_sum = 0;
    for history in histories {
        let mut first_values: Vec<i32> = Vec::new();
        first_values.push(*history.first().unwrap());
        let mut differences= history.iter().zip(history.iter().skip(1)).map(|(x, y)| y - x).collect::<Vec<i32>>();
        first_values.push(*differences.first().unwrap());
        while !(differences.iter().sum::<i32>() == 0 && (differences.iter().min() == differences.iter().max())) {
            differences = differences.iter().zip(differences.iter().skip(1)).map(|(x, y)| y - x).collect::<Vec<i32>>();
            first_values.push(*differences.first().unwrap());
        }
        first_values.reverse();
        let mut previous_values: Vec<i32> = Vec::new();
        previous_values.push(0);
        for first_value in first_values {
            previous_values.push(first_value - previous_values.last().unwrap());
        }
        previous_values_sum += previous_values.last().unwrap();
    }
    previous_values_sum
}
