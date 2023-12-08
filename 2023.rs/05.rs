use std::cmp;
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

fn parse_input(input: Vec<&str>) -> (Vec<u64>, HashMap<&str, Vec<(u64, u64, u64)>>)
{
    let mut maps: HashMap<&str, Vec<(u64, u64, u64)>> = HashMap::new();
    let mut map_name = "";
    let mut map: Vec<(u64, u64, u64)> = Vec::new();
    let mut numbers_set = HashSet::new();
    let mut seeds: Vec<u64> = Vec::new();
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
            let numbers: Vec<u64> = numbers.iter().map(|x| x.parse().unwrap()).collect();
            map.push((numbers[0], numbers[1], numbers[2]));
            for number in &numbers {
                numbers_set.insert(*number);
            }
        }
    }
    maps.insert(map_name, map.clone());
    (seeds, maps)
}

fn part_one(input: Vec<&str>) -> u64
{
    let (seeds, maps) = parse_input(input);
    let destination_names = vec!["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"];
    let mut seed_locations: HashMap<u64, u64> = HashMap::new();
    for seed in seeds {
        let mut destination = seed;
        for destination_name in destination_names.iter() {
            for values in maps.get(destination_name).unwrap() {
                let destination_start = values.0;
                let source_start = values.1;
                let source_end = values.1 + values.2;
                if source_start <= destination && destination < source_end {
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

fn part_two(input: Vec<&str>) -> u64
{
    let (seeds, maps) = parse_input(input);
    let seeds: Vec<(u64, u64)> = seeds.iter().step_by(2).zip(seeds.iter().skip(1).step_by(2)).map(|(a, b)| (*a, *b)).collect();
    let destination_names = vec!["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"];
    let mut locations: Vec<u64> = Vec::new();
    for (seed_start, seed_len) in &seeds {
        let mut ranges: Vec<(u64, u64)> = Vec::new();
        ranges.push((*seed_start, *seed_start + *seed_len));
        for destination_name in destination_names.iter() {
            let mut inter_ranges: Vec<(u64, u64)> = Vec::new();
            for (dst_start, src_start, len) in maps.get(destination_name).unwrap() {
                let mut new_ranges: Vec<(u64, u64)> = Vec::new();
                while !ranges.is_empty() {
                    let (start, end) = ranges.pop().unwrap();
                    let src_end = *src_start + *len;
                    let before = (start, cmp::min(end, *src_start));
                    let inter = (cmp::max(start, *src_start), cmp::min(end, src_end));
                    let after = (cmp::max(start, src_end), end);
                    if before.1 > before.0 {
                        new_ranges.push(before);
                    }
                    if inter.1 > inter.0 {
                        inter_ranges.push((inter.0 - *src_start + *dst_start, inter.1 - *src_start + *dst_start));
                    }
                    if after.1 > after.0 {
                        new_ranges.push(after);
                    }
                }
                ranges = new_ranges;
            }
            ranges.append(&mut inter_ranges);
        }
        locations.push(ranges.iter().min_by_key(|(x, _)| *x).unwrap().0);
    }
    return *locations.iter().min_by_key(|x| *x).unwrap();
}
