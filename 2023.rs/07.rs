use std::fs;
use std::collections::HashMap;

fn main() {
    let example = fs::read_to_string("examples/07.txt").unwrap();
    let input = fs::read_to_string("inputs/07.txt").unwrap();

    assert_eq!(part_one(example.lines().collect()), 6440);
    let part_one = part_one(input.lines().collect());
    println!("{}", part_one);

    assert_eq!(part_two(example.lines().collect()), 5905);
    let part_two = part_two(input.lines().collect());
    println!("{}", part_two);

    assert_eq!(part_one, 248105065);
    assert_eq!(part_two, 249515436);
}

fn parse_input(input: Vec<&str>) -> (Vec<&str>, Vec<u32>) {
    let mut hands: Vec<&str> = Vec::new();
    let mut bids: Vec<u32> = Vec::new();
    for line in input {
        hands.push(line.split_whitespace().collect::<Vec<&str>>()[0]);
        bids.push(line.split_whitespace().collect::<Vec<&str>>()[1].parse().unwrap());
    }
    (hands, bids)
}

fn get_card_count(hand: &str) -> HashMap<char, u8> {
    let cards: Vec<char> = hand.chars().collect();
    let card_count = cards
        .iter()
        .fold(HashMap::new(), |mut map, val|{
        *map.entry(*val).or_default() += 1;
        map
    });
    card_count
}

enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind
}

fn argsort<T: Ord>(data: &[T]) -> Vec<usize> {
    // https://stackoverflow.com/a/69764256
    let mut indices = (0..data.len()).collect::<Vec<_>>();
    indices.sort_by_key(|&i| &data[i]);
    indices
}

fn part_one(input: Vec<&str>) -> u32 {
    fn get_card_strength(card: char) -> u8 {
        match card {
            'A' => 14,
            'K' => 13,
            'Q' => 12,
            'J' => 11,
            'T' => 10,
            _ => card.to_digit(10).unwrap() as u8,
        }
    }

    fn get_hand_type(hand: &str) -> HandType {
        let card_count = get_card_count(hand);
        let mut values: Vec<u8> = card_count.values().cloned().collect();
        values.sort();
        match card_count.keys().len() {
            1 => HandType::FiveOfAKind,
            2 => {
                if values[0] == 1 {
                    HandType::FourOfAKind
                }
                else {
                    HandType::FullHouse
                }
            },
            3 => {
                if values[2] == 3 {
                    HandType::ThreeOfAKind
                }
                else {
                    HandType::TwoPair
                }
            },
            4 => HandType::OnePair,
            _ => HandType::HighCard
        }
    }

    fn get_hand_strength(hand: &str) -> u32 {
        let mut strength: String = String::new();
        let hand_type = get_hand_type(hand);
        strength.push_str(&format!("{:x}", hand_type as u8));
        for card in hand.chars() {
            strength.push_str(&format!("{:x}", get_card_strength(card)));
        }
        u32::from_str_radix(&strength, 16).unwrap()
    }

    let (hands, bids) = parse_input(input);
    let strengths: Vec<u32> = hands.iter().map(|x| get_hand_strength(*x)).collect();
    let ranks = argsort(&argsort(&strengths));
    let mut total_winnings = 0;
    for (rank, bid) in ranks.iter().zip(bids.iter()) {
        total_winnings += (*rank as u32 + 1) * *bid;
    }
    total_winnings
}

fn part_two(input: Vec<&str>) -> u32 {

    fn get_card_strength(card: char) -> u8 {
        match card {
            'A' => 13,
            'K' => 12,
            'Q' => 11,
            'T' => 10,
            'J' => 1,
            _ => card.to_digit(10).unwrap() as u8,
        }
    }

    fn get_hand_type(hand: &str) -> HandType {
        let card_count = get_card_count(hand);
        let mut values: Vec<u8> = card_count.values().cloned().collect();
        values.sort();
        match card_count.keys().len() {
            1 => HandType::FiveOfAKind,
            2 => {
                if values[0] == 1 {
                    if card_count.contains_key(&'J') {
                        return HandType::FiveOfAKind
                    }
                    HandType::FourOfAKind
                }
                else {
                    if card_count.contains_key(&'J') {
                        return HandType::FiveOfAKind
                    }
                    HandType::FullHouse
                }
            },
            3 => {
                if values[2] == 3 {
                    if card_count.contains_key(&'J') {
                        return HandType::FourOfAKind
                    }
                    HandType::ThreeOfAKind
                }
                else {
                    if card_count.contains_key(&'J') {
                        if card_count[&'J'] == 1 {
                            return HandType::FullHouse
                        }
                        return HandType::FourOfAKind
                    }
                    HandType::TwoPair
                }
            },
            4 => {
                if card_count.contains_key(&'J') {
                    return HandType::ThreeOfAKind;
                }
                HandType::OnePair
            }
            _ => {
                if card_count.contains_key(&'J')
                {
                    return HandType::OnePair;
                }
                HandType::HighCard
            }
        }
    }

    fn get_hand_strength(hand: &str) -> u32 {
        let mut strength: String = String::new();
        let hand_type = get_hand_type(hand);
        strength.push_str(&format!("{:x}", hand_type as u8));
        for card in hand.chars() {
            strength.push_str(&format!("{:x}", get_card_strength(card)));
        }
        u32::from_str_radix(&strength, 16).unwrap()
    }

    let (hands, bids) = parse_input(input);
    let strengths: Vec<u32> = hands.iter().map(|x| get_hand_strength(*x)).collect();
    let ranks = argsort(&argsort(&strengths));
    let mut total_winnings = 0;
    for (rank, bid) in ranks.iter().zip(bids.iter()) {
        total_winnings += (*rank as u32 + 1) * *bid;
    }
    total_winnings
}
