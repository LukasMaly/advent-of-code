use std::{fs, cmp};

fn main() {
    let example = fs::read_to_string("examples/11.txt").unwrap();
    let input = fs::read_to_string("inputs/11.txt").unwrap();

    assert_eq!(calculate_length(example.lines().collect(), 2), 374);
    let part_one = calculate_length(input.lines().collect(), 2);
    println!("{}", part_one);

    assert_eq!(calculate_length(example.lines().collect(), 10), 1030);
    assert_eq!(calculate_length(example.lines().collect(), 100), 8410);
    let part_two = calculate_length(input.lines().collect(), 1_000_000);
    println!("{}", part_two);

    assert_eq!(part_one, 9370588);
    assert_eq!(part_two, 746207878188);
}

fn calculate_length(input: Vec<&str>, expanding_factor: u64) -> u64
{
    let mut image: Vec<bool> = Vec::new();
    let size = input.len();
    for line in input {
        for char in line.chars() {
            if char == '#' {
                image.push(true);
            }
            else {
                image.push(false);
            }
        }
    }
    let mut galaxies: Vec<(usize, usize)> = Vec::new();
    for y in 0..size {
        for x in 0..size {
            if image[y * size + x] {
                galaxies.push((x, y));
            }
        }
    }
    let mut pairs: Vec<(usize, usize)> = Vec::new();
    for i in 0..galaxies.len() {
        for j in i..galaxies.len() {
            if i != j {
                pairs.push((i, j));
            }
        }
    }
    let mut expanding_rows: Vec<usize> = Vec::new();
    let mut expanding_cols: Vec<usize> = Vec::new();
    for x in 0..size {
        let mut expading_row = true;
        let mut expading_col = true;
        for galaxy in &galaxies {
            if galaxy.0 == x {
                expading_row = false;
            }
            if galaxy.1 == x {
                expading_col = false;
            }
        }
        if expading_row {
            expanding_rows.push(x);
        }
        if expading_col {
            expanding_cols.push(x);
        }
    }
    let mut length_sum: u64 = 0;
    for pair in pairs {
        let x_start = cmp::min(galaxies[pair.0].0, galaxies[pair.1].0);
        let x_end = cmp::max(galaxies[pair.0].0, galaxies[pair.1].0);
        let y_start = cmp::min(galaxies[pair.0].1, galaxies[pair.1].1);
        let y_end = cmp::max(galaxies[pair.0].1, galaxies[pair.1].1);
        let mut length: u64 = 0;
        for x in x_start..x_end {
            if expanding_rows.contains(&x) {
                length += expanding_factor;
            }
            else {
                length += 1;
            }
        }
        for y in y_start..y_end {
            if expanding_cols.contains(&y) {
                length += expanding_factor;
            }
            else {
                length += 1;
            }
        }
        length_sum += length;
    }
    length_sum
}
