pub fn q3_sol() {
    let na1_pairs = read_data();

    let solutions: Vec<String> = na1_pairs
        .into_iter()
        .map(|na1_pair| {
            println!("{:?}", na1_pair);
            return sum_even_seats(&na1_pair);
        })
        .collect();
    let solution = solutions.join("\n");
    std::fs::write("q3_out.txt", solution).expect("Unable to write");
}

fn read_data() -> Vec<[isize; 2]> {
    use std::fs::read_to_string;

    let data = read_to_string("q3_in.txt").expect("File could not be read.");
    let na1_str_pairs: Vec<&str> = data.lines().collect();
    return na1_str_pairs
        .into_iter()
        .map(|na1_str_pair| {
            let na1_str_vec: Vec<&str> = na1_str_pair.split_whitespace().collect();
            let n: isize = na1_str_vec[0].parse::<isize>().unwrap();
            let a1: isize = na1_str_vec[1].parse::<isize>().unwrap();
            return [n, a1];
        })
        .collect();
}

fn sum_even_seats(&na_1: &[isize; 2]) -> String {
    let [n, a_1] = na_1;

    let mut seat_pairs = initialize_seat_heap(&n, &a_1);
    let mut sitting_order = vec![0; (n - 1) as usize];

    for i in 0..(n - 1) as usize {
        let farthest_seat_pair = seat_pairs.pop().unwrap();
        let [left_seat, right_seat] = farthest_seat_pair.1;

        if left_seat <= 0 {
            sitting_order[i] = 1;
            seat_pairs.push(get_seat_pair(&1, &a_1));
        } else if right_seat >= n + 1 {
            sitting_order[i] = n;
            seat_pairs.push(get_seat_pair(&a_1, &n));
        } else {
            let new_seat_ind = left_seat + farthest_seat_pair.0;
            sitting_order[i] = new_seat_ind;
            seat_pairs.push(get_seat_pair(&left_seat, &new_seat_ind));
            seat_pairs.push(get_seat_pair(&new_seat_ind, &right_seat));
        }
    }

    return format!(
        "{:.0}",
        sitting_order
            .iter()
            .filter(|&x| x % 2 == 0)
            .cloned()
            .collect::<Vec<isize>>()
            .iter()
            .sum::<isize>()
    );
}

fn initialize_seat_heap(
    &n: &isize,
    &a_1: &isize,
) -> std::collections::BinaryHeap<(isize, [isize; 2])> {
    use std::collections::BinaryHeap;

    let seat_pairs = vec![
        get_seat_pair(&(2 - a_1), &a_1),
        get_seat_pair(&a_1, &(2 * n - a_1)),
    ];
    let heap: BinaryHeap<(isize, [isize; 2])> = BinaryHeap::from(seat_pairs);

    return heap;
}

fn get_seat_pair(&left_seat: &isize, &right_seat: &isize) -> (isize, [isize; 2]) {
    return ((right_seat - left_seat) / 2, [left_seat, right_seat]);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, 2 + 2);
    }
}
