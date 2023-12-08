use std::fs;
use std::collections::HashMap;

fn main() {
    let example_1 = fs::read_to_string("examples/08_1.txt").unwrap();
    let example_2 = fs::read_to_string("examples/08_2.txt").unwrap();
    let input = fs::read_to_string("inputs/08.txt").unwrap();

    assert_eq!(part_one(example_1.lines().collect()), 6);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example_2.lines().collect()), 6);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 22411);
    assert_eq!(part_two, 11188774513823);
}

fn parse_input(input: Vec<&str>) -> (Vec<u8>, HashMap<&str, (&str, &str)>) {
    let mut nodes: HashMap<&str, (&str, &str)> = HashMap::new();
    let instructions: Vec<u8> = input[0].chars().map(|x| {
        match x {
            'L' => 0,
            _ => 1
        }
    }).collect();
    for line in &input[2..] {
        let name = &line[0..3];
        let left = &line[7..10];
        let right = &line[12..15];
        nodes.insert(name, (left, right));
    }
    (instructions, nodes)
}

fn part_one(input: Vec<&str>) -> u32 {
    let (instructions, nodes) = parse_input(input);
    let mut steps: u32 = 0;
    let mut current_node = "AAA";
    while current_node != "ZZZ" {
        let instruction = instructions[steps as usize % instructions.len()];
        match instruction {
            0 => current_node = nodes[current_node].0,
            _ => current_node = nodes[current_node].1
        }
        steps += 1;
    }
    return steps;
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn lcm(a: u64, b: u64) -> u64 {
    return a * b / gcd(a, b)
}

fn part_two(input: Vec<&str>) -> u64 {
    let (instructions, nodes) = parse_input(input);
    let start_nodes = nodes.keys().filter(|x| x.chars().nth(2).unwrap().eq(&'A')).collect::<Vec<&&str>>();
    let mut min_steps: Vec<u64> = vec![0; start_nodes.len()];
    for (i, start_node) in start_nodes.into_iter().enumerate() {
        let mut steps: u32 = 0;
        let mut current_node = *start_node;
        while !current_node.ends_with("Z") {
            let instruction = instructions[steps as usize % instructions.len()];
            match instruction {
                0 => current_node = nodes[current_node].0,
                _ => current_node = nodes[current_node].1
            }
            steps += 1;
        }
        min_steps[i] = steps as u64;
    }
    let result: u64 = min_steps.into_iter().reduce(|acc, e| lcm(acc, e)).unwrap();
    result
}
