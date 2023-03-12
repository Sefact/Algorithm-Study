function solution(n) {
    var slice = 6;
    var count = 1;
    while (!Number.isInteger((slice * count) / n)) count += 1;
    return count;
}