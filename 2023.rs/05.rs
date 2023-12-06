use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

fn main() {
    let example = fs::read_to_string("examples/05.txt").unwrap();
    let input = fs::read_to_string("inputs/05.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 35);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 46);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 107430936);
    assert_eq!(part_two, 23738616);
}

fn parse_input(input: Vec<&str>) -> (Vec<u32>, HashMap<&str, Vec<(u32, u32, u32)>>)
{
    let mut maps: HashMap<&str, Vec<(u32, u32, u32)>> = HashMap::new();
    let mut map_name = "";
    let mut map: Vec<(u32, u32, u32)> = Vec::new();
    let mut numbers_set = HashSet::new();
    let mut seeds: Vec<u32> = Vec::new();
    for (l, line) in input.iter().enumerate() {
        if l == 0 {
            let seed_numbers: Vec<&str> = line.split(':').collect::<Vec<&str>>()[1].split_whitespace().collect();
            seeds = seed_numbers.iter().map(|x| x.parse().unwrap()).collect();
            for seed in &seeds {
                numbers_set.insert(*seed);
            }
        }
        else if line.is_empty() {
            if map_name != "" {
                maps.insert(map_name, map.clone());
            }
        }
        else if line.chars().nth(0).unwrap().is_alphabetic() {
            map_name = line.split(' ').collect::<Vec<&str>>()[0].split('-').collect::<Vec<&str>>()[2];
            map = Vec::new();
        }
        else {
            let numbers: Vec<&str> = line.split_whitespace().collect();
            let numbers: Vec<u32> = numbers.iter().map(|x| x.parse().unwrap()).collect();
            map.push((numbers[0], numbers[1], numbers[2]));
            for number in &numbers {
                numbers_set.insert(*number);
            }
        }
    }
    maps.insert(map_name, map.clone());
    (seeds, maps)
}

fn part_one(input: Vec<&str>) -> u32
{
    let (seeds, maps) = parse_input(input);
    let destination_names = vec!["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"];
    let mut seed_locations: HashMap<u32, u32> = HashMap::new();
    for seed in seeds {
        let mut destination = seed;
        for destination_name in destination_names[1..].iter() {
            for values in maps.get(destination_name).unwrap() {
                let destination_start = values.0;
                let source_start = values.1;
                let source_end = values.1 as u64 + values.2 as u64;
                if source_start <= destination && u64::from(destination) < source_end {
                    destination = destination_start + (destination - source_start);
                    break;
                }
            }
        }
        seed_locations.insert(destination, seed);
    }
    let mut min_location = *seed_locations.keys().next().unwrap();
    for (location, _) in seed_locations.iter() {
        if *location < min_location {
            min_location = *location;
        }
    }
    min_location
}

fn part_two(input: Vec<&str>) -> u32
{
    let (seeds, maps) = parse_input(input);
    let seeds: Vec<(u32, u32)> = seeds.iter().step_by(2).zip(seeds.iter().skip(1).step_by(2)).map(|(a, b)| (*a, *b)).collect();
    let destination_names = vec!["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"];
    let mut min_location = u32::MAX;
    for (seed_start, seed_range) in seeds {
        for seed in seed_start..(seed_start + seed_range) {
            let mut destination = seed;
            for destination_name in destination_names[1..].iter() {
                for values in maps.get(destination_name).unwrap() {
                    let destination_start = values.0;
                    let source_start = values.1;
                    let source_end = values.1 as u64 + values.2 as u64;
                    if source_start <= destination && u64::from(destination) < source_end {
                        destination = destination_start + (destination - source_start);
                        break;
                    }
                }
            }
            if destination < min_location {
                min_location = destination;
            }
        }
    }
    min_location
}
