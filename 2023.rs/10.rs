use std::fs;

fn main() {
    let example_1a = fs::read_to_string("examples/10_1a.txt").unwrap();
    let example_1b = fs::read_to_string("examples/10_1b.txt").unwrap();
    let example_2a = fs::read_to_string("examples/10_2a.txt").unwrap();
    let example_2b = fs::read_to_string("examples/10_2b.txt").unwrap();
    let example_2c = fs::read_to_string("examples/10_2c.txt").unwrap();
    let example_2d = fs::read_to_string("examples/10_2d.txt").unwrap();
    let input = fs::read_to_string("inputs/10.txt").unwrap();

    assert_eq!(part_one(example_1a.lines().collect()), 4);
    assert_eq!(part_one(example_1b.lines().collect()), 8);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example_2a.lines().collect()), 4);
    assert_eq!(part_two(example_2b.lines().collect()), 4);
    assert_eq!(part_two(example_2c.lines().collect()), 8);
    assert_eq!(part_two(example_2d.lines().collect()), 10);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);
    
    assert_eq!(part_one, 6786);
    assert_eq!(part_two, 495);
}

fn parse_input(input: Vec<&str>) -> Vec<char> {
    let height = input.len();
    let width = input[0].len();
    let mut grid: Vec<char> = Vec::with_capacity(height * width);
    for line in input {
        for char in line.chars() {
            grid.push(char);
        }
    }
    grid
}

fn get_neighbors() -> Vec<(i32, i32)>
{
    let mut neighbors: Vec<(i32, i32)> = Vec::new();
    for y in -1..=1 {
        for x in -1..=1 {
            if x != 0 || y != 0 {
                neighbors.push((x, y));
            }
        }
    }
    neighbors
}

fn get_pipe_positions(grid: Vec<char>, height: usize, width: usize) -> Vec<(usize, usize)>
{
    let mut pipe: Vec<(usize, usize)> = Vec::new();
    let mut start: (usize, usize) = (0, 0);
    for y in 0..height {
        for x in 0..width {
            if grid[y * width + x] == 'S' {
                start = (x, y);
            }
        }
    }
    let mut next: (i32, i32) = (0, 0);
    for neighbor in get_neighbors() {
        if start.1 as i32 + neighbor.1 >= 0 && start.1 as i32 + neighbor.1 < height as i32 && start.0 as i32 + neighbor.0 >= 0 && start.0 as i32 + neighbor.0 < width as i32 {
            let (x, y) = ((start.0 as i32 + neighbor.0) as usize, (start.1 as i32 + neighbor.1) as usize);
            match grid[y * width + x] {
                '|' => {
                    match neighbor {
                        (0, -1) => {
                            next = neighbor;
                            break;
                        },
                        (0, 1) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                '-' => {
                    match neighbor {
                        (-1, 0) => {
                            next = neighbor;
                            break;
                        },
                        (1, 0) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                'L' => {
                    match neighbor {
                        (-1, 0) => {
                            next = neighbor;
                            break;
                        },
                        (0, 1) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                'J' => {
                    match neighbor {
                        (1, 0) => {
                            next = neighbor;
                            break;
                        },
                        (0, 1) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                '7' => {
                    match neighbor {
                        (1, 0) => {
                            next = neighbor;
                            break;
                        },
                        (0, -1) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                'F' => {
                    match neighbor {
                        (-1, 0) => {
                            next = neighbor;
                            break;
                        },
                        (0, -1) => {
                            next = neighbor;
                            break;
                        },
                        _ => {
                            continue;
                        },
                    }
                },
                _ => {
                    continue;
                },
            }
        }
    }
    pipe.push(start);
    let (mut x, mut y) = start;
    while grid[(y as i32 + next.1) as usize * width + (x as i32 + next.0) as usize] != 'S' {
        (x, y) = ((x as i32 + next.0) as usize, (y as i32 + next.1) as usize);
        pipe.push((x, y));
        match grid[y * width + x] {
            '|' => {
                match next.1 {
                    1 => {
                        next = (0, 1)
                    },
                    -1 => {
                        next = (0, -1)
                    },
                    _ => {
                        unreachable!()
                    },
                }
            },
            '-' => {
                match next.0 {
                    1 => {
                        next = (1, 0)
                    },
                    -1 => {
                        next = (-1, 0)
                    },
                    _ => {
                        unreachable!()
                    },
                }
            },
            'L' => {
                match next.0 {
                    0 => {
                        next = (1, 0)
                    },
                    _ => {
                        next = (0, -1)
                    },
                }
            },
            'J' => {
                match next.0 {
                    0 => {
                        next = (-1, 0)
                    },
                    _ => {
                        next = (0, -1)
                    },
                }
            },
            '7' => {
                match next.0 {
                    0 => {
                        next = (-1, 0)
                    },
                    _ => {
                        next = (0, 1)
                    },
                }
            },
            'F' => {
                match next.0 {
                    0 => {
                        next = (1, 0)
                    },
                    _ => {
                        next = (0, 1)
                    },
                }
            },
            _ => {
                unreachable!()
            },
        }
    }
    pipe
}

fn part_one(input: Vec<&str>) -> i32 {
    let height = input.len();
    let width = input[0].len();
    let grid = parse_input(input);
    let pipe = get_pipe_positions(grid, height, width);
    (pipe.len() / 2) as i32
}

fn is_vertical_start(previous: (usize, usize), start: (usize, usize), next: (usize, usize)) -> bool {
    // Is start any of these shapes '|', 'L', 'J'?
    let from_previous = (start.0 as i32 - previous.0 as i32, start.1 as i32 - previous.1 as i32);
    let to_next = (next.0 as i32 - start.0 as i32, next.1 as i32 - start.1 as i32);
    // '|'
    if from_previous == (0, 1) && to_next == (0, 1) {
        return true;
    }
    else if from_previous == (0, -1) && to_next == (0, -1) {
        return true;
    }
    // 'L'
    else if from_previous == (0, 1) && to_next == (1, 0) {
        return true;
    }
    else if from_previous == (-1, 0) && to_next == (0, -1) {
        return true;
    }
    // 'J'
    else if from_previous == (1, 0) && to_next == (0, -1) {
        return true;
    }
    else if from_previous == (0, 1) && to_next == (-1, 0) {
        return true;
    }
    false
}

fn part_two(input: Vec<&str>) -> i32 {
    let height = input.len();
    let width = input[0].len();
    let grid = parse_input(input);
    let pipe = get_pipe_positions(grid.clone(), height, width);
    let vertical_start = is_vertical_start(*pipe.last().unwrap(), *pipe.first().unwrap(), pipe[1]);
    let mut area = 0;
    for y in 0..height {
        let mut inside = false;
        let mut vertical_chars = String::from("|LJ");
        if vertical_start {
            vertical_chars.push('S');
        }
        for x in 0..width {
            let is_pipe = pipe.contains(&(x, y));
            if is_pipe && vertical_chars.contains(grid[y * width + x]) {
                inside = !inside;
            }
            if inside && !is_pipe {
                area += 1;
            }
        }
    }
    area
}
