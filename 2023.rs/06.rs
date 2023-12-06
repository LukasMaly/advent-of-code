use std::fs;

fn main() {
    let example = fs::read_to_string("examples/06.txt").unwrap();
    let input = fs::read_to_string("inputs/06.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 288);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 71503);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 1195150);
    assert_eq!(part_two, 42550411);
}

fn part_one(input: Vec<&str>) -> u32 {
    let times: Vec<&str> = input[0].split(':').collect::<Vec<&str>>()[1].split_whitespace().collect();
    let times: Vec<u32> = times.iter().map(|x| x.parse().unwrap()).collect();
    let distances: Vec<&str> = input[1].split(':').collect::<Vec<&str>>()[1].split_whitespace().collect();
    let distances: Vec<u32> = distances.iter().map(|x| x.parse().unwrap()).collect();
    let mut record_beats: u32 = 1;
    for (i, time) in times.iter().enumerate() {
        let a: Vec<u32> = (0..(*time + 1)).collect();
        let mut b: Vec<u32> = a.clone();
        b.reverse();
        let c: Vec<u32> = a.iter().zip(b.iter()).map(|(x, y)| x * y).collect();
        record_beats *= c.iter().map(|x| (*x > distances[i]) as u32).sum::<u32>();
    }
    record_beats
}

fn part_two(input: Vec<&str>) -> u32 {
    let times: Vec<&str> = input[0].split(':').collect::<Vec<&str>>()[1].split_whitespace().collect();
    let time: u32 = times.join("").parse().unwrap();
    let distances: Vec<&str> = input[1].split(':').collect::<Vec<&str>>()[1].split_whitespace().collect();
    let distance: u64 = distances.join("").parse().unwrap();
    let a: Vec<u32> = (0..(time + 1)).collect();
    let mut b: Vec<u32> = a.clone();
    b.reverse();
    let c: Vec<u64> = a.iter().zip(b.iter()).map(|(x, y)| (*x as u64) * (*y as u64)).collect();
    let record_beats = c.iter().map(|x| (*x > distance) as u32).sum::<u32>();
    record_beats
}
