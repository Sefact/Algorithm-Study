function solution(array) {
    var answer = [];
    var object = {};

    array.forEach((item) => {
        if (object[item]) object[item] += 1;
        else object[item] = 1; 
    });

    for (let item in object) {
        answer.push([item, object[item]]);
    }

    answer.sort((a, b) => b[1] - a[1]);

    if (answer.length > 1 && answer[0][1] === answer[1][1]) return -1;

    return Number(answer[0][0]);
}