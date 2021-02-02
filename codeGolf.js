function happyNumbers(num) {
    if (typeof num === "number") {
        num = num.toString();
    }

    if (num.length == 1) {
        if (num == 1) {
            return true;
        }
        return false;
    }

    var total = 0;
    for (let i=0;i<num.length;i++) {
        total += num[i]*num[i];
    }
    return happyNumbers(total);
}

// console.log(happyNumbers(4));

function vampireNumbers()